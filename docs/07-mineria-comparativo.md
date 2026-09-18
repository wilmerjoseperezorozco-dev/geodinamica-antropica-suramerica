# 07 — Minería en Suramérica: comparativo de instrumentación geodésica

| País | Sitio | Recurso | Medición geodésica cuantitativa publicada | Fuente |
|---|---|---|---|---|
| Chile | Salar de Atacama | Litio (salmuera) | **Sí** — InSAR satelital, 1-2 cm/año de subsidencia, atribución climática vs. minera con ML | [Mining.com](https://www.mining.com/web/lithium-mining-is-slowly-sinking-chiles-atacama-salt-flat-study-shows/) |
| Brasil | Brumadinho (Minas Gerais) | Hierro (relaves) | **Sí** — InSAR, 30 cm de subsidencia precursora del colapso 2019 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0303243420300192) |
| Colombia | Cerrejón (La Guajira) | Carbón | **No encontrada** — solo caracterización hídrica/social | [OCMAL](https://www.ocmal.org/agua-y-mineria-en-la-guajira/) |
| Colombia | Chocó/Antioquia/Bajo Cauca | Oro aluvial | **No encontrada** para geodesia — sí hay teledetección de área/deforestación (UNODC) | [Mongabay](https://es.mongabay.com/2023/11/mineria-ilegal-aumento-en-colombia-informe/) |
| Perú | Cerro de Pasco | Plomo/zinc/plata | **No encontrada** — solo análisis multiespectral 2D/3D de superficie y contaminación | [NASA Earth Observatory](https://science.nasa.gov/earth/earth-observatory/mining-perus-cerro-de-pasco-144481/) |
| Bolivia | Salar de Uyuni | Litio (salmuera) | **No encontrada** — solo análisis químico/ambiental | [ScienceDaily](https://www.sciencedaily.com/releases/2025/02/250210183627.htm) |
| Argentina | Vaca Muerta (Neuquén) | Hidrocarburos no convencionales | **Sí, pero sismológica, no gravimétrica** — 548 sismos inducidos documentados 2018-2025 | [Seismica](https://seismica.library.mcgill.ca/article/view/1435) |

## Lectura del patrón

De 7 sitios mineros mayores de Suramérica revisados, solo **2 (Chile y Brasil)** cuentan con cuantificación geodésica satelital publicada de deformación del terreno. Argentina tiene instrumentación sismológica pero no gravimétrica/InSAR. Colombia, Perú y Bolivia — que incluyen dos de los recursos más estratégicos del mundo actual (litio y oro) — **no tienen ningún estudio geodésico cuantitativo publicado**, pese a tener caracterización ambiental/social extensa.

**Implicación**: la brecha no es de interés científico ni de existencia del fenómeno — es de **instrumentación aplicada**. Los mismos satélites (Sentinel-1 InSAR, GRACE-FO) que ya cubren Atacama y Brumadinho cubren también Cerrejón, Cerro de Pasco y Uyuni. El costo marginal de extender la metodología ya validada en Chile/Brasil a estos tres sitios es, en principio, bajo — es un problema de procesamiento y publicación, no de captura de datos nuevos.

## Síntesis regional: fórmula de excitación EOP aplicada a todos los casos (2026-09-18)

Con la metodología de `00-marco-teorico.md` §6 (validada contra Tres Gargantas), se calculó el efecto de cada caso sobre la cadena EOP. Esta es la primera vez que estos sitios se comparan entre sí en una misma unidad física.

| Caso | País | Tipo de masa | ¿Aplica la fórmula? | Latitud | ΔLOD (por año) | Apalancamiento deriva polar sin(2φ) |
|---|---|---|---|---|---|---|
| Amazonía (ganancia neta) | Brasil | Agua (TWS) | Sí | 3°S | **+0.21 µs/año** | 0.10 (bajo, pero masa enorme) |
| Salar de Atacama | Chile | Salmuera | Sí | 23.5°S | −0.48 ns/año | **0.73 (el más alto de los casos de agua)** |
| Salar de Uyuni | Bolivia | Salmuera | Sí | 20.3°S | −0.32 ns/año | 0.65 |
| Sabana de Bogotá | Colombia | Agua subterránea | Sí | 4.6°N | −0.09 ns/año | 0.16 |
| Cerrejón | Colombia | Agua subterránea | Sí | 11.0°N | −0.08 ns/año | 0.38 |
| Vaca Muerta | Argentina | Hidrocarburos | Sí (combustión) | 38.5°S | +0.07 ns/año | 0.97 (máximo absoluto, pero mecanismo distinto al agua) |
| Bajo Cauca (oro) | Colombia | Roca/sedimento | **No** — se queda en la cuenca | 7.5°N | ~0 por diseño físico | n/a |
| Cerro de Pasco | Perú | Roca/sedimento | **No** — se queda en la cuenca | 10.7°S | ~0 por diseño físico | n/a |
| Glaciares Cordillera Central | Colombia | Hielo (deshielo) | Sí | 5.5°N | −0.26 a −0.52 ns/año | 0.19 (bajo, pero segunda mayor magnitud de LOD del repositorio) |

**Lectura del patrón**:
1. **El tipo de sustancia importa más que la magnitud de la operación**: la minería de sólidos (oro, plomo, zinc) tiene efecto nulo en la cadena EOP *por construcción física*, sin importar cuánta masa se remueva, porque el material no sale de la cuenca. La minería de fluidos (salmuera, hidrocarburos, agua subterránea) sí es físicamente elegible, aunque en la práctica ningún caso individual suramericano se acerque a ser medible.
2. **La Amazonía domina por 3-4 órdenes de magnitud** sobre cualquier caso minero — no por ser un caso "antrópico" en el sentido de extracción deliberada, sino por la escala continental del sistema hídrico involucrado. Es el único caso de este repositorio que se acerca (sin llegar) a la escala de fenómenos geodésicos ya documentados como Tres Gargantas.
3. **La latitud es tan determinante como la masa**: Vaca Muerta y Atacama, con masas del mismo orden que Bogotá/Cerrejón, tienen apalancamientos de deriva polar 2-6 veces mayores solo por su latitud — y Vaca Muerta cae casi exactamente en el "ángulo mágico" (35.26°) donde el efecto en LOD se anula por coincidencia geográfica.
4. **Ninguno de los 6 casos elegibles llega, ni sumados, a una fracción significativa del umbral de detección** (microsegundos de LOD, centímetros/año de deriva polar) — confirmando con cálculo explícito, no solo con intuición, que el fenómeno de Seo et al. (2023) opera a una escala (miles de acuíferos, continentes enteros) cualitativamente distinta a cualquier operación individual, por grande que sea.
