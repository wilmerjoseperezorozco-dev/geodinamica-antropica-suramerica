"""Disponibilidad de escenas Sentinel-1 IW SLC sobre los sitios de estudio (API pública de ASF, sin cuenta).

Salida: data/asf_s1_slc_2015-2026.json
Uso: python scripts/s1_disponibilidad_asf.py
"""
import collections
import csv
import datetime
import io
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

SITIOS = {
    "Atacama (control)": (-68.30, -23.55),
    "Uyuni (Colcha K)": (-67.70, -20.40),
    "Cerro de Pasco": (-76.25, -10.68),
    "Cerrejon": (-72.65, 11.05),
    "Bajo Cauca (El Bagre)": (-74.80, 7.60),
}
INICIO, FIN = "2015-01-01T00:00:00Z", "2026-09-01T00:00:00Z"
SALIDA = pathlib.Path(__file__).resolve().parent.parent / "data" / "asf_s1_slc_2015-2026.json"


def consultar(lon, lat):
    q = {
        "platform": "S1", "processingLevel": "SLC", "beamMode": "IW",
        "intersectsWith": f"POINT({lon} {lat})", "start": INICIO, "end": FIN, "output": "csv",
    }
    url = "https://api.daac.asf.alaska.edu/services/search/param?" + urllib.parse.urlencode(q)
    for intento in range(4):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                return list(csv.DictReader(io.StringIO(r.read().decode("utf-8", "replace"))))
        except (ConnectionError, TimeoutError, urllib.error.URLError):
            if intento == 3:
                raise
            time.sleep(5 * (intento + 1))


def resumir(filas):
    por_direccion = collections.Counter()
    por_pista = collections.Counter()
    fechas = collections.defaultdict(set)
    for f in filas:
        d = f["Ascending or Descending?"]
        pista = (d, f["Path Number"])
        por_direccion[d] += 1
        por_pista[pista] += 1
        fechas[pista].add(f["Start Time"][:10])
    mejor = max(fechas, key=lambda k: len(fechas[k])) if fechas else None
    saltos = []
    if mejor:
        ds = sorted(datetime.date.fromisoformat(x) for x in fechas[mejor])
        saltos = sorted((b - a).days for a, b in zip(ds, ds[1:]))
    return {
        "escenas_slc": len(filas),
        "por_direccion": dict(por_direccion),
        "pistas": {f"{k[0]} {k[1]}": v for k, v in por_pista.most_common()},
        "pista_mas_densa": f"{mejor[0]} {mejor[1]}" if mejor else None,
        "fechas_pista_mas_densa": len(fechas[mejor]) if mejor else 0,
        "intervalo_mediano_dias": saltos[len(saltos) // 2] if saltos else None,
        "intervalo_maximo_dias": saltos[-1] if saltos else None,
    }


if __name__ == "__main__":
    resultado = {}
    for nombre, (lon, lat) in SITIOS.items():
        resultado[nombre] = {"lon": lon, "lat": lat, **resumir(consultar(lon, lat))}
        print(nombre, resultado[nombre]["escenas_slc"], flush=True)
    SALIDA.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
