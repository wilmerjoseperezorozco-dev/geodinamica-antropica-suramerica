"""Cobertura de productos InSAR abiertos COMET-LiCSAR sobre los sitios de estudio.

Para cada sitio: (1) descubre las pistas Sentinel-1 que lo cubren (ASF), (2) ubica los marcos LiCSAR cuyo polígono
contiene el sitio, (3) cuenta épocas e interferogramas ya procesados y (4) muestrea la coherencia media publicada
por LiCSAR (GeoTIFF uint8, 0-255) en una ventana de ±0.02° alrededor del sitio.

Salida: data/licsar_cobertura_2026-09.json
Uso: python scripts/licsar_cobertura.py   (requiere numpy y rasterio)
"""
import concurrent.futures as cf
import csv
import io
import json
import pathlib
import re
import urllib.parse
import urllib.request

import numpy as np
import rasterio
from rasterio.windows import from_bounds

BASE = "https://gws-access.jasmin.ac.uk/public/nceo_geohazards/LiCSAR_products/"
SITIOS = {
    "Atacama (control)": (-68.30, -23.55),
    "Uyuni (Colcha K)": (-67.70, -20.40),
    "Cerro de Pasco": (-76.25, -10.68),
    "Cerrejon": (-72.65, 11.05),
    "Bajo Cauca (El Bagre)": (-74.80, 7.60),
}
SALIDA = pathlib.Path(__file__).resolve().parent.parent / "data" / "licsar_cobertura_2026-09.json"


def leer(url):
    try:
        return urllib.request.urlopen(url, timeout=40).read().decode("utf-8", "replace")
    except Exception:
        return None


def listar(url):
    t = leer(url)
    return [] if t is None else re.findall(r'href="([^"?/][^"]*)"', t)


def pistas_asf(lon, lat):
    q = {"platform": "S1", "processingLevel": "SLC", "beamMode": "IW", "intersectsWith": f"POINT({lon} {lat})",
         "start": "2025-06-01T00:00:00Z", "end": "2025-09-01T00:00:00Z", "output": "csv"}
    url = "https://api.daac.asf.alaska.edu/services/search/param?" + urllib.parse.urlencode(q)
    filas = csv.DictReader(io.StringIO(urllib.request.urlopen(url, timeout=120).read().decode("utf-8", "replace")))
    return sorted({f["Path Number"].lstrip("0") for f in filas})


def dentro(x, y, poly):
    c = False
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


def poligono(pista, marco):
    t = leer(f"{BASE}{pista}/{marco}/metadata/{marco}-poly.txt")
    if t is None:
        return None
    n = re.findall(r"-?\d+\.\d+", t)
    return [(float(n[i]), float(n[i + 1])) for i in range(0, len(n) - 1, 2)]


def marcos_que_cubren(lon, lat, pistas):
    trabajos = [(p, m.strip("/")) for p in pistas for m in listar(f"{BASE}{p}/") if m.endswith("/")]

    def revisar(j):
        poly = poligono(*j)
        return j if poly and len(poly) >= 3 and dentro(lon, lat, poly) else None

    with cf.ThreadPoolExecutor(16) as ex:
        return [j for j in ex.map(revisar, trabajos) if j]


def coherencia(pista, marco, lon, lat, nombre):
    url = f"/vsicurl/{BASE}{pista}/{marco}/metadata/{marco}.geo.{nombre}.tif"
    try:
        with rasterio.open(url) as ds:
            a = ds.read(1, window=from_bounds(lon - 0.02, lat - 0.02, lon + 0.02, lat + 0.02, ds.transform)).astype("float64")
            a = a[np.isfinite(a)]
            if a.size == 0:
                return None
            return round(float(np.median(a)) / 255.0, 2)
    except Exception:
        return None


def fechas(lista):
    d = sorted(set(re.findall(r"(20\d{6})", " ".join(lista))))
    return (d[0], d[-1]) if d else (None, None)


if __name__ == "__main__":
    salida = {}
    for sitio, (lon, lat) in SITIOS.items():
        pistas = pistas_asf(lon, lat)
        marcos = marcos_que_cubren(lon, lat, pistas)
        detalle = []
        for pista, marco in marcos:
            epocas = listar(f"{BASE}{pista}/{marco}/epochs/")
            ifgs = listar(f"{BASE}{pista}/{marco}/interferograms/")
            detalle.append({
                "marco": marco, "epocas": len(epocas), "periodo_epocas": fechas(epocas),
                "interferogramas": len(ifgs),
                "coherencia_media_12d": coherencia(pista, marco, lon, lat, "meancoh.12"),
                "coherencia_media_36d": coherencia(pista, marco, lon, lat, "meancoh.36"),
            })
        salida[sitio] = {"pistas_sentinel1": pistas, "marcos": detalle}
        print(sitio, len(marcos), "marcos", flush=True)
    SALIDA.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")
