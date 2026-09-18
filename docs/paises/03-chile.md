# Chile — el caso cuantitativo más sólido de la región

## Salar de Atacama — subsidencia medida por satélite, atribución por machine learning

Este es, de toda la búsqueda realizada para este repositorio, **el estudio suramericano más completo y metodológicamente comparable a los estándares internacionales** (Three Gorges, groundwater pumping global de Seo et al. 2023).

- Estudio de la Universidad de Chile (*IEEE Transactions on Geoscience and Remote Sensing*): el salar se está hundiendo a **1-2 cm/año** por extracción de salmuera de litio, usando datos satelitales 2020-2023.
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

No se encontró evidencia de que esta subsidencia local (1-2 cm/año en un área de ~40 km²) se haya vinculado cuantitativamente a la señal agregada de deriva polar o LOD a escala nacional/regional — el mismo vacío de "conexión con la cadena geodésica global" que en Colombia, aunque el dato local esté mucho mejor instrumentado.
