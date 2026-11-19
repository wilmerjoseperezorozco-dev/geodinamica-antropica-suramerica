"""Fase 4 — inversión SBAS/NSBAS propia sobre la pila recortada de interferogramas LiCSAR.

Equivalente reducido de LiCSBAS (Morishita et al. 2020) para una ventana pequeña, sin dependencias externas:
1. multilook 3x3 (~300 m) de la fase desenrollada (media de valores válidos);
2. referencia: se resta a cada interferograma la mediana de una caja de referencia estable;
3. NSBAS por píxel (Doin et al. 2011): incrementos entre épocas + restricción débil (gamma) a un modelo
   lineal, para unir componentes desconectadas de la red (p. ej. el hueco de Sentinel-1B, 2022-2023);
4. velocidad LOS (mm/año, positivo hacia el satélite) por mínimos cuadrados sobre la serie acumulada,
   con error estándar corregido por autocorrelación (AR(1)) de los residuos;
5. conversión a vertical suponiendo movimiento solo vertical: v_up = v_los / U, U = cos(incidencia).

Uso: python scripts/fase4_sbas.py uyuni|atacama
Salida: .cache/sbas_<sitio>.npz (mapas) y data/fase4_sbas_<sitio>.json (resumen)
"""
import datetime as dt
import json
import pathlib
import sys

import numpy as np

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CACHE = RAIZ / ".cache"
LAMBDA = 0.055465763                      # m, Sentinel-1 banda C
M2MM = -LAMBDA / (4 * np.pi) * 1000       # rad -> mm LOS (positivo hacia el satélite, convención LiCSBAS)
ML = 3
GAMMA = 1e-4

CONF = {
    # incidencia media de metadata.txt de cada marco; caja de referencia (lon_min, lat_min, lon_max, lat_max)
    "uyuni": {"marco": "156D_11028_131313", "inc": 33.76, "ref": (-67.70, -20.30, -67.60, -20.20)},
    "atacama": {"marco": "156D_11424_131313", "inc": 33.55, "ref": None},
}


def fecha(s):
    return dt.datetime.strptime(s, "%Y%m%d").date()


def multilook(a, n=ML):
    f, c = a.shape[-2] // n * n, a.shape[-1] // n * n
    b = a[..., :f, :c].reshape(*a.shape[:-2], f // n, n, c // n, n)
    with np.errstate(invalid="ignore"):
        return np.nanmean(b, axis=(-3, -1))


def coordenadas(transform, forma, n=ML):
    a, _, c, _, e, f = transform
    lon = c + a * n * (np.arange(forma[1]) + 0.5)
    lat = f + e * n * (np.arange(forma[0]) + 0.5)
    return lon, lat


def nsbas(pila, ifgs):
    """pila: (n_ifg, npix) en mm. Devuelve (epocas, serie acumulada (n_ep, npix), velocidad, error)."""
    pares = [tuple(i.split("_")) for i in ifgs]
    epocas = sorted({e for p in pares for e in p})
    idx = {e: k for k, e in enumerate(epocas)}
    t = np.array([(fecha(e) - fecha(epocas[0])).days / 365.25 for e in epocas])
    ne, ni = len(epocas), len(ifgs)
    # incógnitas: incrementos d_k (k=1..ne-1) + v + c
    G = np.zeros((ni, ne - 1))
    for r, (a, b) in enumerate(pares):
        G[r, idx[a]:idx[b]] = 1.0
    acum = np.tril(np.ones((ne - 1, ne - 1)))      # serie acumulada en épocas 1..ne-1
    Greg = np.hstack([GAMMA * acum, -GAMMA * t[1:, None], -GAMMA * np.ones((ne - 1, 1))])
    Gfull = np.vstack([np.hstack([G, np.zeros((ni, 2))]), Greg])
    npix = pila.shape[1]
    serie = np.full((ne, npix), np.nan)
    validos = np.isfinite(pila)
    # agrupar píxeles por patrón de datos faltantes (casi todos completos sobre el salar)
    patrones, inv = np.unique(validos.T, axis=0, return_inverse=True)
    for k, patron in enumerate(patrones):
        cols = np.where(inv.ravel() == k)[0]
        if patron.sum() < 0.9 * ni:
            continue
        filas = np.concatenate([np.where(patron)[0], ni + np.arange(ne - 1)])
        d = np.vstack([pila[patron][:, cols], np.zeros((ne - 1, cols.size))])
        sol = np.linalg.lstsq(Gfull[filas], d, rcond=None)[0]
        serie[0, cols] = 0.0
        serie[1:, cols] = acum @ sol[:ne - 1]
    # velocidad por mínimos cuadrados sobre la serie
    X = np.vstack([t, np.ones_like(t)]).T
    ok = np.isfinite(serie[0])
    vel = np.full(npix, np.nan)
    err = np.full(npix, np.nan)
    beta, *_ = np.linalg.lstsq(X, serie[:, ok], rcond=None)
    res = serie[:, ok] - X @ beta
    r1 = np.sum(res[1:] * res[:-1], axis=0) / np.sum(res**2, axis=0)
    r1 = np.clip(r1, 0, 0.99)
    neff = ne * (1 - r1) / (1 + r1)
    s2 = np.sum(res**2, axis=0) / np.maximum(neff - 2, 1)
    vel[ok] = beta[0]
    err[ok] = np.sqrt(s2 / np.sum((t - t.mean()) ** 2) * ne / np.maximum(neff, 3))
    return epocas, t, serie, vel, err


def main(sitio):
    cf = CONF[sitio]
    z = np.load(CACHE / f"pila_{sitio}_{cf['marco']}.npz")
    unw, ifgs, tr = z["unw"], list(z["ifgs"]), z["transform"]
    unw = np.where(unw == 0, np.nan, unw)
    ml = multilook(unw) * M2MM
    lon, lat = coordenadas(tr, ml.shape[1:])
    # referencia: caja dada o, por defecto, mediana espacial de cada interferograma
    if cf["ref"]:
        x0, y0, x1, y1 = cf["ref"]
        m = (lon[None, :] >= x0) & (lon[None, :] <= x1) & (lat[:, None] >= y0) & (lat[:, None] <= y1)
        ref = np.nanmedian(ml[:, m], axis=1)
    else:
        ref = np.nanmedian(ml.reshape(len(ifgs), -1), axis=1)
    ml = ml - ref[:, None, None]
    # descartar interferogramas con < 90 % de píxeles válidos (máscaras de LiCSAR por baja coherencia,
    # p. ej. inundación estacional del salar); NSBAS une los huecos que esto deje en la red
    frac = np.isfinite(ml.reshape(len(ifgs), -1)).mean(axis=1)
    keep = frac >= 0.9
    print(f"interferogramas usados: {keep.sum()} de {len(ifgs)}")
    ml, ifgs = ml[keep], [i for i, k in zip(ifgs, keep) if k]
    forma = ml.shape[1:]
    epocas, t, serie, vel, err = nsbas(ml.reshape(len(ifgs), -1), ifgs)
    U = np.cos(np.radians(cf["inc"]))
    np.savez_compressed(CACHE / f"sbas_{sitio}.npz", lon=lon, lat=lat, epocas=np.array(epocas), t=t,
                        serie=serie.reshape(len(epocas), *forma).astype("float32"),
                        vel=vel.reshape(forma), err=err.reshape(forma), U=U)
    print(sitio, "épocas", len(epocas), "ifgs", len(ifgs), "píxeles válidos", int(np.isfinite(vel).sum()), "de", vel.size)
    print("velocidad LOS (mm/año): p1 %.2f  p50 %.2f  p99 %.2f" % tuple(np.nanpercentile(vel, [1, 50, 99])))


if __name__ == "__main__":
    main(sys.argv[1])
