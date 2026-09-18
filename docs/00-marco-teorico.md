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

## 6. Fórmula de excitación de la cadena EOP por redistribución de masa local (metodología reusable)

Este repositorio necesitaba una forma de responder, con física y no solo con analogía, si una redistribución de masa local (ej. un acuífero, una mina) es capaz de producir un cambio medible en la cadena EOP (deriva polar, LOD). No existía en la literatura revisada una fórmula lista para aplicar caso por caso — se deriva aquí a partir de la teoría estándar del tensor de inercia terrestre (Munk & MacDonald 1960; Lambeck 1980), en su versión de primer orden (sin números de Love elásticos ni autoatracción oceánica, que sí usan los cálculos operativos de IERS/JPL).

**Modelo físico**: una masa ΔM se extrae de un punto en la superficie a latitud φ y se redistribuye, en promedio, sobre el océano global (aproximación estándar en estudios de agotamiento de acuíferos, incluido Seo et al. 2023 §4).

### 6.1 Efecto en LOD (momento de inercia axial C)

```
ΔC = ΔM · R² · (2/3 − cos²φ)        [2/3 = promedio de cos²φ sobre una esfera = efecto del océano]
Δω/ω = −ΔC/C                          [conservación del momento angular, C·ω = const]
ΔLOD = −LOD₀ · (Δω/ω)
```

Con C = 8.0365×10³⁷ kg·m² (momento de inercia axial terrestre), R = 6.371×10⁶ m, LOD₀ = 86400 s.

**Consecuencia no trivial**: el factor (2/3 − cos²φ) es **negativo en el ecuador** (cos²0°=1 > 2/3) y se vuelve positivo en latitudes altas (cos²φ→0). Esto significa que extraer masa de una fuente **ecuatorial** y moverla al océano **acelera** la rotación (acorta el LOD) — el mismo efecto de "patinador que encoge los brazos" — mientras que extraer masa de una fuente en **latitud alta** (glaciares, acuíferos templados) la **frena** (alarga el LOD). El factor es máximo en magnitud exactamente en el ecuador (φ=0° → factor = −1/3) y nulo cuando cos²φ=2/3 (φ≈35.26°, el "ángulo mágico").

### 6.2 Efecto en deriva polar (bamboleo)

La excitación del movimiento del polo depende de los productos de inercia (I₁₃, I₂₃), que escalan con **sin(2φ)** en vez de cos²φ — es decir, se anulan en el ecuador y son máximos cerca de ±45°. Esto es la razón física por la que Seo et al. (2023) encuentran la mayor contribución a la deriva polar en fuentes de latitud media (oeste de EE.UU. ~35-40°N, noroeste de India ~28-30°N): están cerca del máximo de sin(2φ), no es casualidad geográfica.

### 6.3 Validación de la fórmula contra un caso ya publicado (control de calidad)

Antes de aplicar esta fórmula a un caso nuevo de este repositorio, se validó contra el efecto ya publicado de la represa de las Tres Gargantas (Chao et al., ~40 km³ de agua embalsada, φ≈30.8°N, efecto reportado: **+0.06 microsegundos** de LOD, un alargamiento):

- ΔM = 4×10¹³ kg (agua añadida al embalse, tomada del promedio oceánico)
- cos²(30.8°) = 0.739 → factor (cos²φ − 2/3) = +0.072 (signo invertido porque aquí la masa se **añade** en tierra, no se extrae)
- ΔC = +1.17×10²⁶ kg·m² → ΔLOD ≈ **+0.126 microsegundos**

El resultado del modelo simplificado (+0.126 µs) coincide en orden de magnitud y signo con el valor publicado (+0.06 µs) — dentro de un factor ~2, la diferencia esperada por omitir números de Love elásticos y la dinámica real de redistribución oceánica. **Esto da confianza suficiente para usar la fórmula en la comparación de órdenes de magnitud que es el propósito de este repositorio** (no para sustituir un cálculo geodésico operativo de precisión).

Aplicación de esta metodología al caso de Bogotá: ver `docs/paises/01-colombia.md` §8.

### 6.4 Cuándo esta fórmula NO aplica: masa hídrica vs. masa sólida (regla general para todo el repositorio)

Un error fácil de cometer al extender este cálculo a un caso de minería (en vez de un acuífero) es asumir que "más masa removida = más efecto en EOP". Eso es falso si esa masa **no llega a redistribuirse a escala global**.

- **Agua subterránea (acuíferos, salmueras de litio)**: cuando se bombea, una fracción relevante entra al ciclo hidrológico y eventualmente llega al océano global (evapotranspiración → lluvia → escorrentía, o descarga directa a un río que desemboca al mar) en escalas de años a décadas. Por eso el modelo "se extrae de un punto, se redistribuye en promedio sobre el océano" (§6.1) es una aproximación razonable — es exactamente el mecanismo que usan Seo et al. (2023) y los estudios de nivel del mar.
- **Roca, suelo y relaves de minería (excavación, sobrecarga, colas)**: ese material casi nunca sale de la misma cuenca hidrográfica — se deposita en escombreras, se redepositan como sedimento río abajo a decenas o cientos de km, o queda como relave en la misma región. **No hay redistribución a escala de armónico esférico de grado 2** (la escala que domina la señal de EOP), sin importar cuánta masa total se haya movido. El efecto de este tipo de minería sobre la cadena EOP es, por diseño físico del fenómeno, cercano a cero — **no por ser poca masa, sino por no salir de la región**.

**Regla práctica para este repositorio**: la fórmula de §6.1-6.2 se aplica directamente a extracción de agua subterránea o salmuera (Bogotá, Cerrejón, Atacama, Uyuni). Para minería de sólidos (oro en Bajo Cauca, cobre, carbón a cielo abierto) se debe evaluar primero si el material realmente sale de la cuenca — si no, el efecto en EOP es nulo por construcción, y el impacto real de esa minería se mide en otras variables (deformación local vía InSAR, sedimentación fluvial, contaminación), no en la cadena EOP. Ver aplicación de esta distinción en `docs/paises/01-colombia.md` §9-10.
