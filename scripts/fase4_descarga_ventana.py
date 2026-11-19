"""Fase 4 — descarga de una red reducida de interferogramas COMET-LiCSAR, recortada a una ventana.

Desde la migración del archivo de LiCSAR (ago-2025 en adelante) cada interferograma de
`LiCSAR_products/<pista>/<marco>/interferograms/` es un pequeño archivo HTML con enlaces al
archivo CEDA (`data.ceda.ac.uk/neodc/comet/data/licsar_products/...`). Los GeoTIFF de CEDA están
organizados en franjas de una fila (no son COG) y el servidor entrega ~20 KB/s por conexión, así que
descargar marcos completos (~15 MB por interferograma) no es viable. Este script:

1. Lista los interferogramas disponibles del marco.
2. Elige una red reducida: una cadena de épocas separadas ~24 días (12-60 d) más todas las
   conexiones entre épocas elegidas con línea base temporal <= 72 días (redundancia para SBAS).
3. Lee con GDAL /vsicurl solo las filas de la ventana (lectura parcial por rangos HTTP), en paralelo.
4. Guarda una pila .npz (fase desenrollada en radianes, float32) en .cache/ (no se versiona).

Uso:  python scripts/fase4_descarga_ventana.py uyuni|atacama [--hilos 16]
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import pathlib
import re
import time
import urllib.request

import numpy as np
import rasterio
from rasterio.windows import from_bounds

JASMIN = "https://gws-access.jasmin.ac.uk/public/nceo_geohazards/LiCSAR_products/"
CEDA = "https://dap.ceda.ac.uk/neodc/comet/data/licsar_products/"
RAIZ = pathlib.Path(__file__).resolve().parent.parent
CACHE = RAIZ / ".cache"

# (pista, marco, (lon_min, lat_min, lon_max, lat_max))
SITIOS = {
    "uyuni": ("156", "156D_11028_131313", (-67.95, -20.65, -67.15, -20.10)),
    "atacama": ("156", "156D_11424_131313", (-68.55, -23.80, -68.05, -23.35)),
}
GDAL_OPC = dict(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", GDAL_HTTP_MERGE_CONSECUTIVE_RANGES="YES",
                CPL_VSIL_CURL_CHUNK_SIZE=524288, GDAL_HTTP_MAX_RETRY=4, GDAL_HTTP_RETRY_DELAY=5,
                GDAL_HTTP_TIMEOUT=300)


def fecha(s):
    return dt.datetime.strptime(s, "%Y%m%d").date()


def listar_ifgs(pista, marco):
    t = urllib.request.urlopen(f"{JASMIN}{pista}/{marco}/interferograms/", timeout=180).read().decode()
    return sorted(set(re.findall(r'href="(20\d{6}_20\d{6})', t)))


def red_reducida(ifgs, paso_obj=24, dmin=12, dmax=60, redund=72):
    pares = {(a, b) for a, b in (i.split("_") for i in ifgs)}
    salida = {}
    for a, b in pares:
        salida.setdefault(a, []).append(b)
    epocas = sorted({e for p in pares for e in p})
    elegidas, actual = [epocas[0]], epocas[0]
    while True:
        cand = [b for b in salida.get(actual, []) if dmin <= (fecha(b) - fecha(actual)).days <= dmax]
        if not cand:  # hueco en la red: saltar a la siguiente época con salidas válidas
            sig = [e for e in epocas if e > actual and any(dmin <= (fecha(b) - fecha(e)).days <= dmax
                                                            for b in salida.get(e, []))]
            if not sig:
                break
            actual = sig[0]
            elegidas.append(actual)
            continue
        actual = min(cand, key=lambda b: abs((fecha(b) - fecha(actual)).days - paso_obj))
        elegidas.append(actual)
    s = set(elegidas)
    return sorted(f"{a}_{b}" for a, b in pares
                  if a in s and b in s and (fecha(b) - fecha(a)).days <= redund)


def leer_ventana(pista, marco, ifg, caja):
    url = f"/vsicurl/{CEDA}{pista}/{marco}/{ifg}/{ifg}.geo.unw.tif"
    try:  # el archivo-enlace indica la ubicación real (CEDA o LiCSAR_products.public en JASMIN)
        t = urllib.request.urlopen(f"{JASMIN}{pista}/{marco}/interferograms/{ifg}", timeout=120).read().decode()
        m = re.search(r"href='([^']+\.geo\.unw\.tif)'", t)
        if m:
            url = "/vsicurl/" + m.group(1)
    except Exception:  # noqa: BLE001
        pass
    for intento in range(3):
        try:
            with rasterio.Env(**GDAL_OPC), rasterio.open(url) as ds:
                w = from_bounds(*caja, ds.transform).round_offsets().round_lengths()
                return ifg, ds.read(1, window=w).astype("float32"), ds.window_transform(w)
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(10 * (intento + 1))
    return ifg, None, str(err)[:120]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("sitio", choices=SITIOS)
    ap.add_argument("--hilos", type=int, default=16)
    a = ap.parse_args()
    pista, marco, caja = SITIOS[a.sitio]
    CACHE.mkdir(exist_ok=True)
    destino = CACHE / f"pila_{a.sitio}_{marco}.npz"
    parcial = CACHE / f"pila_{a.sitio}_{marco}.parcial"
    parcial.mkdir(exist_ok=True)

    red = red_reducida(listar_ifgs(pista, marco))
    print(f"{marco}: {len(red)} interferogramas en la red reducida", flush=True)
    pend = [i for i in red if not (parcial / f"{i}.npy").exists()]
    transf = None
    t0 = time.time()
    with cf.ThreadPoolExecutor(a.hilos) as ex:
        for n, (ifg, arr, tr) in enumerate(ex.map(lambda i: leer_ventana(pista, marco, i, caja), pend), 1):
            if arr is None:
                print(f"FALLO {ifg}: {tr}", flush=True)
                continue
            np.save(parcial / f"{ifg}.npy", arr)
            transf = tr
            if n % 20 == 0:
                print(f"{n}/{len(pend)} ({time.time() - t0:.0f} s)", flush=True)

    ok = [i for i in red if (parcial / f"{i}.npy").exists()]
    if transf is None:
        with rasterio.Env(**GDAL_OPC), rasterio.open(f"/vsicurl/{CEDA}{pista}/{marco}/{ok[0]}/{ok[0]}.geo.unw.tif") as ds:
            transf = ds.window_transform(from_bounds(*caja, ds.transform).round_offsets().round_lengths())
    pila = np.stack([np.load(parcial / f"{i}.npy") for i in ok])
    np.savez_compressed(destino, unw=pila, ifgs=np.array(ok), transform=np.array(transf)[:6], caja=np.array(caja))
    print(f"LISTO {destino.name}: {pila.shape}, faltaron {len(red) - len(ok)}", flush=True)
