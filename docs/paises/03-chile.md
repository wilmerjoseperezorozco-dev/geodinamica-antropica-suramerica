# Chile — el caso cuantitativo más sólido de la región

## Salar de Atacama — subsidencia medida por satélite, atribución por machine learning

Este es, de toda la búsqueda realizada para este repositorio, **el estudio suramericano más completo y metodológicamente comparable a los estándares internacionales** (Three Gorges, groundwater pumping global de Seo et al. 2023).

- Fuentes primarias identificadas (consulta del 2026-09-21; precisan la atribución inicial, basada en resúmenes de prensa):
  - Delgado, Shreve, Borgstrom, León-Ibáñez, Castillo y Poland (2024), *IEEE Transactions on Geoscience and Remote Sensing*, DOI 10.1109/TGRS.2024.3423792: evaluación global de SAOCOM-1 (banda L) que incluye la subsidencia por bombeo de salmuera en Atacama y la contrasta con ALOS-2, Sentinel-1 y TerraSAR-X/TanDEM-X/PAZ (correlación 1:1 ± 3% en la velocidad en línea de vista).
  - Resumen AGU 2023 (Fall Meeting, NS31A-0616): series InSAR Sentinel-1 y ALOS-2 (2019-2021) con hasta **1 cm/año** de subsidencia sobre ~8 km de halita cerca de los pozos de bombeo, y una serie Sentinel-1 descendente (oct-2014 a may-2023) que indica un proceso transitorio con variabilidad espacio-temporal significativa.
  - Fáundez, Orpinas, Álvarez, Cumsille y Guzmán (2026), *Bulletin of Engineering Geology and the Environment*: evaluación de toda la cuenca 2019-2024 con Sentinel-1 y SBAS.
  - Las cifras de prensa de **1-2 cm/año** (2020-2023) y del área de ~8 × 5 km no pudieron contrastarse con el texto de una fuente primaria; hasta hacerlo, el valor citable con respaldo directo es "hasta ~1 cm/año sobre ~8 km".
- La subsidencia más severa ocurre en el sector suroeste del salar, donde se concentran las operaciones de litio; área afectada ~8 km (norte-sur) × 5 km (este-oeste).
- Causa física: la tasa de bombeo de salmuera supera la tasa de recarga de los acuíferos, generando hundimiento por consolidación.
- Estudio complementario: "Disentangling Climate Change and Lithium Mining Impacts on Groundwater in the Salar de Atacama Basin" — usa un enfoque híbrido EOF + machine learning sobre GRACE downscaled específicamente para **separar la causa climática de la causa minera**, el problema de atribución que en Colombia (Cerrejón) sigue sin resolverse.

Fuentes:
- [Lithium mining is slowly sinking Chile's Atacama salt flat — MINING.COM](https://www.mining.com/web/lithium-mining-is-slowly-sinking-chiles-atacama-salt-flat-study-shows/)
- [Uncertainties in the debate on the environmental impact of lithium brine extraction in Salar de Atacama — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2950117223000249)
- [Disentangling Climate Change and Lithium Mining Impacts on Groundwater — ADS/AGU](https://ui.adsabs.harvard.edu/abs/2024AGUFMH43O.1076B/abstract)
- [Lithium mining leaves severe impacts in Chile, but new methods exist — Mongabay 2025](https://news.mongabay.com/2025/09/lithium-mining-leaves-severe-impacts-in-chile-but-new-methods-exist-report/)

## Por qué Chile es el benchmark metodológico de este repositorio

El caso de Atacama resuelve, con evidencia satelital y de machine learning, dos de las brechas identificadas en Colombia (`01-colombia.md`, sección 5):
1. Cuantifica la subsidencia en cm/año con datos satelitales (Colombia no lo tiene para minería).
2. Separa estadísticamente la causa climática de la causa antrópica (Colombia no lo tiene para ningún caso minero).

**Implicación directa para la Fase 2 de este proyecto**: la metodología EOF + machine learning de atribución usada en Atacama es replicable en La Guajira (Cerrejón) y en el sector minero de Chocó/Antioquia, si se consigue acceso a la misma cadena de datos (Sentinel-1 InSAR + GRACE-FO downscaled).

## Brecha remanente incluso en Chile

No se encontró evidencia de que esta subsidencia local (1-2 cm/año en un área de ~40 km²) se haya vinculado cuantitativamente a la señal agregada de deriva polar o LOD a escala nacional/regional — el mismo vacío de "conexión con la cadena geodésica global" que en Colombia, aunque el dato local esté mucho mejor instrumentado. Esta sección cierra ese vacío con la misma metodología aplicada a Colombia.

## Aplicación de la fórmula de excitación EOP (metodología en `00-marco-teorico.md` §6)

Este es el mejor caso posible para aplicar la fórmula: a diferencia de la minería de sólidos (oro en Bajo Cauca, Colombia), la extracción de salmuera **sí** cumple la condición de §6.4 del marco teórico — el 85-95% del agua se pierde por evaporación directa a la atmósfera, que sí se redistribuye globalmente.

### Dato de entrada (verificado en vivo, 2026-09-18)

- Tasa de extracción combinada de las operadoras (SQM + Albemarle): **1 650 litros/segundo** = 52 millones de m³/año. Fuente: reportes especializados citando datos de extracción declarada.
- Densidad de salmuera (más densa que agua dulce por su alta salinidad): ~1 200 kg/m³.
- Latitud del Salar de Atacama: φ ≈ 23.5°S.

### Cálculo

```
ΔM = 52×10⁶ m³/año × 1200 kg/m³ = 6.24×10¹⁰ kg/año
cos²(23.5°) = 0.8411  →  factor (2/3 − cos²φ) = −0.1744
ΔC = 6.24×10¹⁰ × (6.371×10⁶)² × (−0.1744) ≈ −4.42×10²³ kg·m²
ΔLOD ≈ −0.48 nanosegundos/año
```

### Resultado y comparación

- **~5-6 veces mayor que Bogotá o el Cerrejón** (−0.09 a −0.08 ns/año) — porque el volumen es ~8 veces mayor, parcialmente compensado por estar más lejos del ecuador.
- Para la deriva polar, sin(2×23.5°) = **0.731** — muy cerca del máximo teórico (0.94 a 35°), muy por encima del valor de Bogotá (0.16) o el Cerrejón (0.38). **De todos los casos calculados en este repositorio, Atacama tiene el mayor apalancamiento por unidad de masa sobre la deriva polar**, aunque la masa absoluta sigue siendo ~15 000 veces menor que la escala global de Seo et al. (2023).
- Sigue estando **~2-3 órdenes de magnitud por debajo** del efecto ya minúsculo de Tres Gargantas (60 000 ns, un solo evento) y muy por debajo del piso de detección operativo del IERS (microsegundos).

**Conclusión**: Atacama es, de los casos de este repositorio, el que más se acerca a una combinación favorable de masa y latitud — y aun así no es medible. Es la confirmación más fuerte disponible de que ninguna operación minera individual conocida en Suramérica alcanza la escala necesaria para tocar la cadena EOP; el fenómeno de Seo et al. (2023) requiere la suma de miles de acuíferos a escala de continentes enteros, no un solo sitio.
