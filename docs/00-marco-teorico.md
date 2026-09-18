# 00 — Marco teórico: rotación, traslación y redistribución de masa

## 1. Rotación terrestre

- Velocidad angular: ω ≈ 7.2921159 × 10⁻⁵ rad/s
- Día sidéreo: 23h 56m 4.09s (86 164.09 s)
- Velocidad tangencial ecuatorial: ~1 670 km/h
- **LOD (Length of Day)**: la duración real del día difiere de 86 400 s por milisegundos; medida operativamente por el IERS (International Earth Rotation and Reference Systems Service) vía VLBI y relojes atómicos.

### Registro reciente de LOD (verificado, 2024-2026)
| Fecha | LOD respecto a 86 400 s |
|---|---|
| 5 jul 2024 | −1.66 ms (mínimo histórico de la era de relojes atómicos) |
| 10 jul 2025 | −1.37 ms |
| 26 jul 2026 (proyección IERS) | −0.65 ms |

Fuentes: [timeanddate.com — Earth rotation 2026](https://www.timeanddate.com/news/astronomy/earth-rotation-2026), [timeanddate.com — Earth fast rotation 2025](https://www.timeanddate.com/news/astronomy/earth-fast-rotation-2025), [Forbes, jul-2026](https://www.forbes.com/sites/jamiecartereurope/2026/07/24/why-sunday-may-now-be-the-shortest-day-of-the-year-as-earth-slows-down/)

La aceleración rotacional 2020-2024 parece haber alcanzado su pico; el planeta vuelve a desacelerar hacia la tendencia de largo plazo (fricción de marea lunar, +1.7 a 2.3 ms/siglo). Esto es relevante operativamente: por primera vez se discute un "segundo intercalar negativo" en el UTC.

### Causas conocidas de variación de LOD, de mayor a menor escala
1. Intercambio de momento angular atmósfera–Tierra sólida (moduado por El Niño/La Niña)
2. Acoplamiento núcleo–manto
3. Terremotos grandes (Tohoku 2011, M9.1, acortó el día ~1.8 µs)
4. Ajuste isostático glacial y deshielo polar
5. **Redistribución antrópica de agua** (agua subterránea, embalses) — objeto de este repositorio

## 2. Traslación terrestre

- Velocidad orbital media: 29.78 km/s; perihelio ~30.29 km/s, afelio ~29.29 km/s
- 1 UA ≈ 149.6 millones de km; año sidéreo 365.256 días
- Jerarquía de marcos para "trayectoria galáctica": Tierra→Sol (29.78 km/s) → Sol→centro galáctico (~220-230 km/s, año galáctico 225-250 Ma) → Vía Láctea→CMB (~370 km/s peculiar)
- A esta escala la Tierra se trata como masa puntual (GM⊕ conocido con precisión de partes por billón vía seguimiento de naves); **la redistribución interna de masa NO afecta la trayectoria orbital/galáctica**, solo el eje de rotación y el LOD.

## 3. Instrumentos de medición de altimetría y masa

| Sistema | Mide | Resolución |
|---|---|---|
| SRTM, Copernicus DEM, ASTER GDEM | Topografía de superficie | 30 m |
| ICESat-2 (láser) | Altimetría de hielo/agua | cm |
| Jason-3, Sentinel-6 | Altimetría oceánica | mm/año de tendencia |
| EGM2008/EGM2020 | Geoide (superficie equipotencial) | ~5 km |
| **GRACE / GRACE-FO** | Redistribución temporal de masa por firma gravitatoria | ~300-400 km, mensual |
| IERS Bulletin A/B | Parámetros de orientación terrestre (EOP): polar motion, UT1-UTC, LOD | operativo semanal |

**Limitación central**: con la resolución actual de GRACE (~300 km), solo el 10% de las cuencas fluviales significativas del mundo son observables con detalle útil. La misión sucesora **NGGM/MAGIC** (ESA+NASA, lanzamiento previsto 2032) promete 100-150 km de resolución, elevando esa cobertura al 80%. Fuente: [MAGIC — eoPortal](https://www.eoportal.org/satellite-missions/magic), [Next Generation Gravity Mission — Wikipedia](https://en.wikipedia.org/wiki/Next_Generation_Gravity_Mission).

## 4. Caso de referencia global: agua subterránea y deriva polar

Seo et al. (Seoul National University, *Geophysical Research Letters*, 2023): entre 1993 y 2010 se extrajeron >2 150 Gt de agua subterránea (sobre todo en el oeste de Norteamérica y noroeste de India), desplazando el polo de rotación hacia el este (64.16°E) a ~4.36 cm/año, y contribuyendo ~6.24 mm a la subida global del nivel del mar en ese período. Es, tras el flujo del manto, el segundo factor más importante de deriva del polo entre las causas climático-antrópicas.

Fuente primaria: [Seo et al. 2023, GRL](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL103509)

## 5. IA aplicada a esta medición (estado del arte, no específico de Suramérica)

- **Gap-filling GRACE↔GRACE-FO** (vacío de 11 meses, 2017-2018): Transformers con atención, CNN, DCAE, BCNN, redes de retropropagación, SSA.
- **Downscaling espacial**: deep learning + variables auxiliares (topografía, precipitación, uso de suelo) para bajar de ~300 km a escala de cuenca.
- **Predicción de polar motion/LOD**: LSTM, CNN-LSTM-atención, EEMD-LSTM; mejoras de 48-53% en MAE a 6 días frente al método operativo IERS Bulletin A.

Ver `docs/10-preguntas-no-resueltas.md` para las brechas que esta línea de IA todavía no resuelve (atribución de fuente, cobertura in situ desigual).
