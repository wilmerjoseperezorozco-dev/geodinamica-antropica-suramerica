"""Fase 4 — excitación de la rotación terrestre (LOD y movimiento del polo) por las fuentes suramericanas.

A diferencia de `00-marco-teorico.md` §6 (primer orden, sin números de Love), aquí se usan las funciones
de excitación de masa estándar (Barnes et al. 1983; Eubanks 1993; Gross 2015, Treatise on Geophysics 3.11),
que ya incluyen la deformación elástica de carga (k'2 = -0.301) y el desacople núcleo-manto para LOD:

    chi1 = -1.098 R^2/(C-A) * dM * sin(phi) cos(phi) cos(lam)
    chi2 = -1.098 R^2/(C-A) * dM * sin(phi) cos(phi) sin(lam)
    dLOD/LOD0 = +0.753 R^2/C_m * dM * (cos^2(phi) - 2/3)        (dM > 0: masa añadida en tierra)

La masa sale (o entra) de un punto y se compensa con una capa uniforme sobre la esfera (mismo supuesto de
§6.1). Para el polo, una capa uniforme no excita grado 2, así que solo cuenta la fuente puntual. Para una tasa
constante, la deriva secular del polo es d(chi)/dt (la componente de Chandler se promedia en décadas).

Se suman vectorialmente todos los casos suramericanos y se comparan con:
  * precisión diaria IERS: LOD ~ 10 µs; polo ~ 30 µas (orden de magnitud de las series EOP 20 C04)
  * la señal global de agua subterránea de Seo et al. 2023 (GRL, 4.36 cm/año de deriva del polo, 1993-2010)

Salida: data/fase4_excitacion_eop_suramerica.json   Uso: python scripts/fase4_excitacion_eop.py
"""
import json
import math
import pathlib

R = 6.371e6
C, A = 8.0365e37, 8.0101e37          # momentos principales (kg m^2)
C_M = 7.1236e37                     # manto + corteza
LOD0 = 86400.0
MAS = 180 / math.pi * 3600e3         # rad -> mas

# nombre: (dM en kg/año, negativo = masa que sale del continente; lat, lon; categoría; fuente en el repo)
CASOS = {
    "Salar de Atacama (salmuera)": (-6.24e10, -23.5, -68.3, "antropica_fluidos", "paises/03-chile.md"),
    "Salar de Uyuni (salmuera, capacidad de diseño)": (-3.48e10, -20.3, -67.7, "antropica_fluidos", "paises/05-bolivia.md"),
    "Sabana de Bogotá (cota alta)": (-1.0e11, 4.6, -74.1, "antropica_fluidos", "paises/01-colombia.md §8"),
    "Cerrejón (agua)": (-6.2e9, 11.0, -72.65, "antropica_fluidos", "paises/01-colombia.md §9"),
    "Vaca Muerta (hidrocarburos)": (-3.1e10, -38.5, -69.0, "antropica_fluidos", "paises/06-argentina.md"),
    "Costa Oriental Lago de Maracaibo (petróleo, ilustrativo)": (-5.4e10, 9.8, -71.2, "antropica_fluidos", "paises/08-venezuela.md"),
    "Glaciares de Colombia (cota alta)": (-3.70e10, 5.5, -75.4, "climatica_inducida", "paises/01-colombia.md §11"),
    "Glaciares de Ecuador (cota alta)": (-9.22e10, -0.5, -78.4, "climatica_inducida", "paises/07-ecuador.md"),
    "Amazonía (ganancia neta de agua, GRACE)": (+1.426e13, -3.0, -60.0, "natural", "paises/02-brasil.md"),
}
UMBRAL_LOD_S = 10e-6
UMBRAL_POLO_MAS = 0.030
SEO_POLO_MAS_ANIO = 0.0436 / R * MAS   # 4.36 cm/año -> mas/año


def excitacion(dm, lat, lon):
    p, l = math.radians(lat), math.radians(lon)
    k = -1.098 * R**2 / (C - A) * dm * math.sin(p) * math.cos(p)
    chi1, chi2 = k * math.cos(l), k * math.sin(l)
    dlod = LOD0 * 0.753 * R**2 / C_M * dm * (math.cos(p) ** 2 - 2 / 3)
    return chi1 * MAS, chi2 * MAS, dlod


def suma(filas):
    x = sum(f["chi1_mas_anio"] for f in filas)
    y = sum(f["chi2_mas_anio"] for f in filas)
    lod = sum(f["dLOD_s_anio"] for f in filas)
    return {"chi1_mas_anio": x, "chi2_mas_anio": y, "polo_mas_anio": math.hypot(x, y),
            "polo_mm_anio": math.hypot(x, y) / MAS * R * 1e3,
            "direccion_lon_grados": math.degrees(math.atan2(y, x)), "dLOD_s_anio": lod}


if __name__ == "__main__":
    filas = []
    for nombre, (dm, lat, lon, cat, fuente) in CASOS.items():
        c1, c2, lod = excitacion(dm, lat, lon)
        filas.append({"caso": nombre, "categoria": cat, "fuente": fuente, "dM_kg_anio": dm, "lat": lat, "lon": lon,
                      "chi1_mas_anio": c1, "chi2_mas_anio": c2, "polo_mas_anio": math.hypot(c1, c2),
                      "dLOD_s_anio": lod})
    grupos = {
        "antropica_directa": [f for f in filas if f["categoria"] == "antropica_fluidos"],
        "antropica_mas_glaciares": [f for f in filas if f["categoria"] != "natural"],
        "todo_incluida_amazonia": filas,
    }
    resumen = {}
    for g, fs in grupos.items():
        s = suma(fs)
        s["polo_fraccion_seo2023"] = s["polo_mas_anio"] / SEO_POLO_MAS_ANIO
        s["anios_para_umbral_polo"] = UMBRAL_POLO_MAS / s["polo_mas_anio"]
        s["anios_para_umbral_lod"] = UMBRAL_LOD_S / abs(s["dLOD_s_anio"])
        s["IDR_polo_10_anios"] = 10 * s["polo_mas_anio"] / UMBRAL_POLO_MAS
        s["IDR_lod_10_anios"] = 10 * abs(s["dLOD_s_anio"]) / UMBRAL_LOD_S
        resumen[g] = s
    salida = {"supuestos": {"umbral_lod_s": UMBRAL_LOD_S, "umbral_polo_mas": UMBRAL_POLO_MAS,
                            "seo2023_polo_mas_anio": SEO_POLO_MAS_ANIO,
                            "IDR": "Índice de detectabilidad rotacional = señal acumulada en 10 años / precisión diaria IERS"},
              "casos": filas, "sumas": resumen}
    ruta = pathlib.Path(__file__).resolve().parent.parent / "data" / "fase4_excitacion_eop_suramerica.json"
    ruta.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")
    for f in filas:
        print(f"{f['caso'][:48]:48s} polo {f['polo_mas_anio']*1e3:9.4f} µas/año  LOD {f['dLOD_s_anio']*1e9:+9.3f} ns/año")
    for g, s in resumen.items():
        print(f"\n[{g}] polo {s['polo_mas_anio']*1e3:.3f} µas/año ({s['polo_mm_anio']:.4f} mm/año, hacia {s['direccion_lon_grados']:.0f}°)"
              f"  LOD {s['dLOD_s_anio']*1e9:+.3f} ns/año\n   fracción de Seo 2023: {s['polo_fraccion_seo2023']:.2e}"
              f"  años para umbral polo: {s['anios_para_umbral_polo']:.0f}  LOD: {s['anios_para_umbral_lod']:.0f}"
              f"  IDR10 polo {s['IDR_polo_10_anios']:.2e}  LOD {s['IDR_lod_10_anios']:.2e}")
