"""Fase 4 — análisis de la velocidad SBAS: perfiles radiales alrededor de la operación, series antes/después
del arranque industrial y volumen de subsidencia; genera figuras en docs/img/ y data/fase4_insar_<sitio>.json.

Uso: python scripts/fase4_analisis.py uyuni|atacama
"""
import datetime as dt
import json
import pathlib
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CACHE = RAIZ / ".cache"
IMG = RAIZ / "docs" / "img"

CONF = {
    # centro de la operación (pozas/pozos), caja que excluye las pozas mismas, fecha de corte
    "uyuni": {"centro": (-67.38, -20.545), "pozas": (-67.43, -20.60, -67.33, -20.49), "corte": "20231215",
              "etiqueta": "Salar de Uyuni — complejo YLB Llipi (marco 156D_11028_131313)"},
    "atacama": {"centro": None, "pozas": None, "corte": "20190101",
                "etiqueta": "Salar de Atacama — control positivo (marco 156D_11424_131313)"},
}


def fecha(s):
    return dt.datetime.strptime(str(s), "%Y%m%d").date()


def tasa(t, y):
    ok = np.isfinite(y)
    if ok.sum() < 6:
        return None, None
    t, y = t[ok], y[ok]
    X = np.vstack([t, np.ones_like(t)]).T
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    r1 = np.clip(np.sum(r[1:] * r[:-1]) / np.sum(r**2), 0, 0.99)
    neff = len(t) * (1 - r1) / (1 + r1)
    se = np.sqrt(np.sum(r**2) / max(neff - 2, 1) / np.sum((t - t.mean()) ** 2) * len(t) / max(neff, 3))
    return float(b[0]), float(se)


def main(sitio):
    cf = CONF[sitio]
    z = np.load(CACHE / f"sbas_{sitio}.npz")
    lon, lat, ep, t, serie, vel, err, U = (z[k] for k in ["lon", "lat", "epocas", "t", "serie", "vel", "err", "U"])
    vup, eup = vel / U, err / U
    serie_up = serie / U
    LON, LAT = np.meshgrid(lon, lat)
    if cf["centro"] is None:  # control: centro = mínimo suavizado de velocidad
        from scipy.ndimage import uniform_filter
        s = uniform_filter(np.nan_to_num(vup, nan=0.0), 9)
        i, j = np.unravel_index(np.argmin(s), s.shape)
        cf["centro"] = (float(lon[j]), float(lat[i]))
    cx, cy = cf["centro"]
    dkm = np.hypot((LON - cx) * 111.32 * np.cos(np.radians(cy)), (LAT - cy) * 110.57)
    en_pozas = np.zeros_like(dkm, bool)
    if cf["pozas"]:
        x0, y0, x1, y1 = cf["pozas"]
        en_pozas = (LON >= x0) & (LON <= x1) & (LAT >= y0) & (LAT <= y1)
    fuera = np.isfinite(vup) & ~en_pozas
    # perfil radial
    perfil = []
    for r0 in range(0, 40, 2):
        m = fuera & (dkm >= r0) & (dkm < r0 + 2)
        if m.sum() > 20:
            perfil.append({"r_km": r0 + 1, "v_up_mm_anio_mediana": float(np.nanmedian(vup[m])),
                           "p10": float(np.nanpercentile(vup[m], 10)), "n": int(m.sum())})
    # ruido: dispersión de la velocidad lejos (> 20 km)
    lejos = fuera & (dkm > 20)
    sigma = float(np.nanstd(vup[lejos]))
    # volumen de subsidencia significativa dentro de 20 km (excluyendo pozas)
    pix_km2 = (abs(lon[1] - lon[0]) * 111.32 * np.cos(np.radians(cy))) * (abs(lat[1] - lat[0]) * 110.57)
    sig = fuera & (dkm <= 20) & (vup < -3 * sigma)
    vol = float(np.nansum(vup[sig]) * 1e-3 * pix_km2 * 1e6)  # m3/año
    # series promedio por anillo y tasas antes/después del corte
    tc = (fecha(cf["corte"]) - fecha(ep[0])).days / 365.25
    anillos = {}
    for nombre, (a, b) in {"0-3 km": (0, 3), "3-8 km": (3, 8), "8-15 km": (8, 15), "> 25 km": (25, 99)}.items():
        m = fuera & (dkm >= a) & (dkm < b)
        if m.sum() < 10:
            continue
        y = np.nanmedian(serie_up[:, m], axis=1)
        anillos[nombre] = {"serie": y, "total": tasa(t, y), "antes": tasa(t[t < tc], y[t < tc]),
                           "despues": tasa(t[t >= tc], y[t >= tc]), "n": int(m.sum())}

    # métrica diferencial local (cancela rampas atmosféricas/orbitales de gran escala):
    # mediana 0-8 km (fuera de las pozas) menos mediana del anillo 10-20 km
    cerca = fuera & (dkm < 8)
    anillo = fuera & (dkm >= 10) & (dkm < 20)
    dif = np.nanmedian(serie_up[:, cerca], axis=1) - np.nanmedian(serie_up[:, anillo], axis=1)
    diferencial = {"total": tasa(t, dif), "antes": tasa(t[t < tc], dif[t < tc]),
                   "despues": tasa(t[t >= tc], dif[t >= tc]),
                   "umbral_3sigma_total": 3 * tasa(t, dif)[1]}

    # figuras
    IMG.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.5))
    lim = max(5, float(np.nanpercentile(np.abs(vup), 99)))
    im = ax[0].imshow(vup, extent=[lon[0], lon[-1], lat[-1], lat[0]], cmap="RdBu", vmin=-lim, vmax=lim)
    ax[0].plot(cx, cy, "k+", ms=12)
    if cf["pozas"]:
        x0, y0, x1, y1 = cf["pozas"]
        ax[0].plot([x0, x1, x1, x0, x0], [y0, y0, y1, y1, y0], "k--", lw=0.8)
    plt.colorbar(im, ax=ax[0], label="velocidad vertical (mm/año)")
    ax[0].set_title(f"{cf['etiqueta']}\n{ep[0]}-{ep[-1]}", fontsize=9)
    fechas = [fecha(e) for e in ep]
    for nombre, d in anillos.items():
        ax[1].plot(fechas, d["serie"], ".-", ms=2, lw=0.7, label=f"{nombre} ({d['total'][0]:+.1f} mm/año)")
    ax[1].axvline(fecha(cf["corte"]), color="k", ls=":", lw=0.8)
    ax[1].set_ylabel("desplazamiento vertical acumulado (mm)")
    ax[1].legend(fontsize=8)
    ax[1].grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(IMG / f"fase4_insar_{sitio}.png", dpi=110)

    res = {"sitio": sitio, "marco_epocas": [str(ep[0]), str(ep[-1])], "n_epocas": int(len(ep)),
           "centro_lon_lat": cf["centro"], "sigma_v_up_lejos_mm_anio": sigma,
           "v_up_min_suavizado_dentro_10km": float(np.nanpercentile(vup[fuera & (dkm < 10)], 1)),
           "volumen_subsidencia_significativa_m3_anio": vol, "pixeles_significativos": int(sig.sum()),
           "perfil_radial": perfil, "fecha_corte": cf["corte"], "diferencial_0-8_menos_10-20km": diferencial,
           "anillos": {k: {kk: vv for kk, vv in v.items() if kk != "serie"} for k, v in anillos.items()}}
    (RAIZ / "data" / f"fase4_insar_{sitio}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k != "perfil_radial"}, indent=1, ensure_ascii=False))
    for p in perfil[:12]:
        print(p)


if __name__ == "__main__":
    main(sys.argv[1])
