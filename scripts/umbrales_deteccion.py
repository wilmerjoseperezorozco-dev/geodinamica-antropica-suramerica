"""Umbrales de detección empíricos para GRACE (serie de La Guajira, data/grace_la_guajira_2002-2026.csv) y para
series GNSS verticales SIRGAS (archivos NEU públicos), y señal esperada de las extracciones sobre un mascon de 3°.

Método: mínimos cuadrados con error estándar corregido por autocorrelación de lag 1 (n_eff = n(1-r)/(1+r));
umbral de detección = 3 × error estándar efectivo. Se excluye la ventana feb-jun 2023 en las series GNSS
(salto de marco de referencia, ver docs/paises/01-colombia.md §6.7).

Salida por pantalla y data/umbrales_deteccion_2026-09.json.  Uso: python scripts/umbrales_deteccion.py
"""
import csv
import datetime
import json
import math
import pathlib
import urllib.request

import numpy as np

RAIZ = pathlib.Path(__file__).resolve().parent.parent
R_TIERRA_KM = 6371.0


def ajustar(t, y, escalones=()):
    n = len(t)
    cols = [t - t.mean(), np.ones(n)] + [(t >= s).astype(float) for s in escalones]
    A = np.vstack(cols).T
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ c
    sd = res.std(ddof=A.shape[1])
    cov = sd ** 2 * np.linalg.inv(A.T @ A)
    r1 = float(np.corrcoef(res[:-1], res[1:])[0, 1])
    n_eff = n * (1 - r1) / (1 + r1)
    se_ef = math.sqrt(cov[0, 0]) * math.sqrt(n / n_eff)
    return {"n": n, "tendencia": round(float(c[0]), 3), "rms": round(float(sd), 2), "AR1": round(r1, 2),
            "n_efectivo": round(n_eff), "se_efectivo": round(se_ef, 3), "umbral_3sigma": round(3 * se_ef, 3)}


def serie_neu(codigo):
    txt = urllib.request.urlopen(f"https://www.sirgas.org/fileadmin/docs/SIRGAS_TS/{codigo}.NEU", timeout=60).read().decode("latin-1")
    filas = []
    for linea in txt.splitlines():
        p = linea.split()
        if len(p) >= 12 and p[0][:2] in ("19", "20") and "." in p[0]:
            try:
                filas.append((float(p[0]), p[1], float(p[8]) * 1000.0))
            except ValueError:
                pass
    return [f for f in filas if not ("2023-02-01" <= f[1] <= "2023-06-15")]


def area_mascon_km2(lat):
    return (3 * math.pi / 180 * R_TIERRA_KM) ** 2 * math.cos(math.radians(lat))


if __name__ == "__main__":
    filas = list(csv.reader(open(RAIZ / "data" / "grace_la_guajira_2002-2026.csv", encoding="utf-8")))[1:]
    t = np.array([datetime.date.fromisoformat(f[0]).toordinal() / 365.25 for f in filas])
    y = np.array([float(f[1]) for f in filas])
    grace = ajustar(t, y)
    umbral_grace = grace["umbral_3sigma"]
    casos = {"Atacama (52 Mm3/año)": (52e6, -23.5), "Uyuni (29 Mm3/año)": (29e6, -20.3),
             "Cerrejón (6.2 Mm3/año)": (6.2e6, 11.05), "Bogotá (100 Mm3/año, cota alta)": (100e6, 4.6)}
    senal = {}
    for nombre, (volumen, lat) in casos.items():
        a_m2 = area_mascon_km2(lat) * 1e6
        ewh = volumen / a_m2 * 100.0
        senal[nombre] = {"area_mascon_km2": round(a_m2 / 1e6), "EWH_cm_ano": round(ewh, 4), "umbral_sobre_senal": round(umbral_grace / ewh)}
    gnss = {}
    for cod, escalones in [("UYNI", (2014.25,)), ("HC03", ()), ("JU03", ()), ("TPZA", ())]:
        s = serie_neu(cod)
        tt = np.array([x[0] for x in s])
        yy = np.array([x[2] for x in s])
        gnss[cod] = ajustar(tt, yy, escalones)
        if cod == "UYNI":
            m = tt >= 2015.0
            gnss["UYNI_2015-2026_sin_escalon"] = ajustar(tt[m], yy[m])
    salida = {"GRACE_La_Guajira": grace, "senal_esperada_sobre_mascon_3grados": senal, "GNSS_vertical_mm_ano": gnss}
    (RAIZ / "data" / "umbrales_deteccion_2026-09.json").write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(salida, indent=1, ensure_ascii=False))
