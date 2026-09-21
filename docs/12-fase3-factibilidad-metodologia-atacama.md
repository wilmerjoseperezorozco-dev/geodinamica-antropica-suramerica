# 12 — Fase 3: factibilidad de replicar la metodología de Atacama en Uyuni, Cerro de Pasco, Cerrejón y Bajo Cauca

Fecha de las consultas: 2026-09-21. Todas las cifras de este documento provienen de fuentes abiertas sin registro y pueden reproducirse con los scripts de `scripts/` (resultados en `data/`). Esta fase evalúa **si** la metodología es transferible; no produce todavía series de deformación propias.

## 1. Qué se entiende por "metodología de Atacama"

La bibliografía sobre el Salar de Atacama combina dos componentes que conviene evaluar por separado:

| Componente | Descripción verificada | Fuente |
|---|---|---|
| **A. InSAR multisensor** | Series de tiempo de Sentinel-1 (banda C) con SBAS, contrastadas con ALOS-2 y SAOCOM-1 (banda L) y PAZ/TerraSAR-X (banda X); hasta ~1 cm/año sobre ~8 km cerca de los pozos (2019-2021), proceso transitorio con variabilidad espacio-temporal | Delgado et al. 2024 (DOI 10.1109/TGRS.2024.3423792); resumen AGU 2023 NS31A-0616; Fáundez et al. 2026 (*Bull. Eng. Geol. Environ.*) |
| **B. Atribución con GRACE reducido + EOF + aprendizaje automático** | Separación de la causa climática y la causa minera en las aguas subterráneas de la cuenca | Título del resumen AGU 2024 H43O-1076 (solo se pudo consultar el título; el texto del resumen no fue accesible) |

Una precisión respecto de versiones anteriores de este repositorio: la atribución periodística del estudio de InSAR (Universidad de Chile, 1-2 cm/año, 2020-2023) no pudo contrastarse con el texto de las fuentes primarias identificadas, por lo que aquí solo se usan las cifras respaldadas por ellas (ver `paises/03-chile.md`).

## 2. Criterios de evaluación

Para cada sitio se midieron seis condiciones, todas verificables con datos abiertos:

1. **Disponibilidad de escenas Sentinel-1** (API de ASF; `scripts/s1_disponibilidad_asf.py`).
2. **Productos InSAR abiertos ya procesados** por COMET-LiCSAR: marcos cuyo polígono contiene el sitio, épocas e interferogramas (`scripts/licsar_cobertura.py`).
3. **Coherencia media** publicada por LiCSAR en el sitio (mismo script).
4. **Verdad de terreno GNSS** cercana y su umbral de detección (`scripts/umbrales_deteccion.py`).
5. **Detectabilidad en GRACE** de la extracción esperada (mismo script).
6. **Tipo de masa**: si la fórmula EOP de `00-marco-teorico.md` §6 aplica (fluidos) o no (sólidos).

Atacama actúa como **control positivo**: el sitio donde el método está publicado.

## 3. Resultados

| | Atacama (control) | Salar de Uyuni | Cerro de Pasco | Cerrejón | Bajo Cauca |
|---|---|---|---|---|---|
| Sentinel-1 IW SLC 2015-2026: fechas en la pista más densa / intervalo mediano | 495 / 6 d | 495 / 6 d | 341 / 12 d | 477 / 6 d | 355 / 12 d |
| Pistas que cubren el sitio | 2 | 3 | 3 | 3 | 3 |
| Marcos LiCSAR con interferogramas | 2 completos (2 398 y 2 222) | **3 completos (2 584, 2 231 y 1 228)** | **ninguno utilizable** (1-3 épocas, ≤1 interferograma) | 1 parcial (1 030, jul-2020 a oct-2025, una pista) | **ninguno utilizable** (7 épocas, 10 interferogramas) |
| Coherencia media 12 d | 0.89-0.91 | 0.59-0.71 | sin dato (mapa vacío) | no publicada | sin dato (mapa vacío) |
| Coherencia media 36 d | 0.81-0.93 | 0.46-0.83 | sin dato | no publicada | sin dato |
| GNSS más cercano | no evaluado | UYNI (~90 km) | HC03 (~80 km), JU03 (~110 km) | RIOH (~55 km, removida en 2023), VALL (~90 km) | EBPT, CASI, TARZ (ver `paises/01-colombia.md` §6.7) |
| Tipo de masa / fórmula EOP | fluido / sí | fluido / sí | sólido / no | fluido / sí | sólido / no |
| Extracción esperada ÷ umbral GRACE | 1/16 | 1/29 | no aplica | 1/140 | no aplica |

Notas de lectura: (i) las cifras de Sentinel-1 cuentan escenas que intersectan el punto; el indicador comparable entre sitios es el número de fechas por pista. (ii) La coherencia es la mediana del mapa medio de LiCSAR (GeoTIFF uint8, dividido por 255; la escala se infirió de los valores) en una ventana de ±0.02° (~4 km) alrededor del punto. (iii) Distancias aproximadas, calculadas con coordenadas de los pueblos y de los sitios.

### 3.1 Disponibilidad de datos SAR: no es el factor diferenciador

Los cinco sitios tienen entre 977 y 1 399 escenas Sentinel-1 IW SLC entre 2015 y 2026, con dos o tres pistas independientes (ascendentes y descendentes) y hasta 495 fechas en la pista más densa. El intervalo mediano entre adquisiciones es de 6 o 12 días según la pista (no se analizó si responde a la combinación de satélites o al escenario de observación). El control de Atacama no tiene mejor cobertura de adquisición que Uyuni o el Cerrejón: **la brecha de instrumentación no proviene de la falta de imágenes**.

### 3.2 Productos abiertos ya procesados: aquí sí hay diferencias

- **Uyuni está listo para procesar.** Tres marcos LiCSAR sobre el sitio (`156D_11028_131313`, `149A_11032_131313`, `076A_11050_131113`) contienen entre 327 y 455 épocas e interferogramas ya calculados desde octubre de 2014 hasta 2026 — una base equivalente a la del control de Atacama (459 y 438 épocas).
- **El Cerrejón está parcialmente cubierto.** Existe el marco `004A_07905_191818` con 181 épocas y 1 030 interferogramas (jul-2020 a oct-2025), pero en una sola pista ascendente y sin mapas de coherencia publicados; no se encontró ningún marco de las pistas 69 y 77 cuyo polígono contenga el sitio, y no hay productos anteriores a 2020. Esta cifra corrige la afirmación previa de este repositorio de que LiCSAR "no cubre Colombia" (ver `08-tiempo-real.md` §4).
- **Cerro de Pasco y Bajo Cauca no tienen productos utilizables.** Los marcos existen como estructura de archivo, pero con una a siete épocas y como máximo diez interferogramas: no hay serie de tiempo que analizar. Son los únicos casos donde el bloqueo es de procesamiento, no de datos SAR.

### 3.3 Coherencia

La coherencia media en Uyuni (0.59-0.71 a 12 días) es entre 20% y 35% menor que en Atacama (0.89-0.91), pero supera el umbral de 0.4 que suele recomendarse como mínimo; el valor más bajo (0.46 a 36 días en la pista descendente) queda apenas por encima. Un informe de práctica de la Universidad de Potsdam sobre cuatro salares de la Puna argentina (Rincón, Olaroz, Llullaillaco y Aguas Calientes II; Sentinel-1, 2016-2025, LiCSBAS2 sobre productos COMET-LiCS) tuvo que bajar el umbral de coherencia a 0.2 y aun así recuperó velocidades coherentes: −8.16 mm/año en Olaroz (sitio con extracción de salmuera), −0.10 mm/año en Rincón (sin explotación) y elevaciones de +2.2 a +3.1 mm/año en los dos salares de control. **Es literatura gris (informe de práctica), no un artículo revisado por pares**; se cita como evidencia de que la misma cadena de herramientas abiertas funciona en salares vecinos, no como resultado propio ni definitivo.

### 3.4 Verdad de terreno GNSS

| Estación | Tendencia vertical (mm/año) | Error estándar efectivo | Umbral de detección (3σ) | Serie |
|---|---|---|---|---|
| UYNI (Uyuni) | +0.45 (con escalón del sismo de Iquique 2014) o +0.80 (solo 2015-2026) | 0.19 | 0.58 | 2005-2026 |
| HC03 (Amarilis, Huánuco) | −0.34 | 0.40 | 1.20 | 2018-2026 |
| JU03 (Chanchamayo, Junín) | −0.01 | 0.58 | 1.73 | 2018-2026 |
| TPZA (Potosí) | −0.86 | 1.76 | 5.29 | 2023-2026 |

(Error estándar corregido por autocorrelación de lag 1, con AR(1) de 0.7-0.84; se excluyó la ventana feb-jun 2023 por el salto de marco de referencia descrito en `paises/01-colombia.md` §6.7.)

Lectura: ninguna estación muestra subsidencia; los valores de UYNI son levantamientos menores de 1 mm/año, cuya magnitud depende de cómo se trate el escalón de 2014 (un rango que este análisis no resuelve). **Estas series no informan sobre el bombeo de salmuera ni sobre el tajo de Cerro de Pasco**, porque las estaciones están a unos 90, 80 y 110 km de los sitios. Lo que sí establecen es la sensibilidad: con solo tres años de datos (TPZA) el umbral de detección es de ~5 mm/año, de modo que una estación **dentro** del área de bombeo detectaría tasas del orden de 10 mm/año (las publicadas para Atacama y Olaroz) en un plazo de pocos años. Ninguno de los sitios evaluados tiene hoy una estación en esa posición.

### 3.5 GRACE no puede detectar ninguna de estas extracciones

A partir de la serie propia de La Guajira (`paises/01-colombia.md` §6.5; 259 meses, autocorrelación de lag 1 = 0.84, solo ~23 observaciones independientes) el umbral de detección de tendencia (3σ) es de **0.79 cm/año** de altura equivalente de agua. La señal esperada, repartida sobre un mascon de 3° (~102 000-111 000 km²) y tratando toda la extracción como pérdida neta (cota superior), es:

| Extracción | Volumen | Altura equivalente de agua | Umbral ÷ señal |
|---|---|---|---|
| Atacama | 52 Mm³/año | 0.051 cm/año | 16 |
| Uyuni | 29 Mm³/año | 0.028 cm/año | 29 |
| Cerrejón | 6.2 Mm³/año | 0.0057 cm/año | 140 |
| Bogotá (cota alta) | 100 Mm³/año | 0.090 cm/año | 9 |

Aunque el umbral resultara 5 veces menor en el Altiplano que en La Guajira, Atacama y Uyuni seguirían 3 y 6 veces por debajo. Se infiere, con la salvedad de que el texto del resumen AGU 2024 no pudo consultarse, que el componente B de la metodología de Atacama **no puede consistir en detectar la extracción dentro de la señal gravitatoria**: debe apoyarse en la reducción de escala y en variables climáticas e hidrogeológicas locales, que son justamente lo que falta en los sitios de menor densidad de datos. El umbral se estimó en La Guajira; su extrapolación al Altiplano (donde el ciclo hidrológico también está dominado por El Niño/La Niña) es una hipótesis no verificada.

### 3.6 Bandas L: NISAR

El Alaska Satellite Facility informa que la primera liberación pública de datos de banda L de NISAR comenzó el 2026-07-20 e incluye adquisiciones desde el 2026-06-17, con los datos del primer año de operaciones científicas por liberarse "en los próximos meses" y el registro completo previsto hacia finales de 2026. La banda L conserva mejor la coherencia sobre vegetación, lo que la hace la vía más prometedora para Cerrejón y Bajo Cauca (tropicales), pero hoy solo hay ~3 meses de datos, insuficientes para series de tiempo; la cobertura de NISAR sobre estos sitios no se verificó.

## 4. Veredicto por sitio

| Sitio | Componente A (InSAR) | Componente B (GRACE + ML) | Prioridad |
|---|---|---|---|
| **Uyuni** | **Viable ahora**: 3 marcos con series completas 2014-2026; coherencia suficiente pero menor que en el control | No transferible como detección (señal 29 veces bajo el umbral) | 1 |
| **Cerrejón** | **Viable con trabajo previo**: un marco ascendente 2020-2025; falta verificar coherencia sobre y alrededor de los tajos, y añadir pistas | No transferible (140 veces bajo el umbral) | 2 |
| **Cerro de Pasco** | **Bloqueado por procesamiento**: sin series; requiere solicitar procesamiento a COMET-LiCS o procesar con herramientas propias | No aplica (minería de sólidos) | 3 |
| **Bajo Cauca** | **Bloqueado por procesamiento**: sin series; además vegetación tropical densa, favorable a banda L | No aplica (minería de sólidos) | 3 |

Sobre el issue #12 (generalización de la metodología a sitios con menor densidad de datos): **el componente InSAR se generaliza sin barreras técnicas donde ya existen interferogramas procesados (Uyuni, parcialmente Cerrejón); el componente de atribución con GRACE no se generaliza como detección en ningún sitio**, y su equivalente en sitios sin red de pozos ni estaciones GNSS cercanas exige primero instrumentar (una estación GNSS de referencia dentro del área de bombeo bastaría para validar el InSAR).

## 5. Limitaciones de esta evaluación

1. Factibilidad no es resultado: no se procesó ninguna serie InSAR propia; las velocidades citadas de Atacama y la Puna provienen de terceros.
2. La coherencia se muestreó en un punto por marco, con mapas medios de 12 y 36 días; no sustituye una evaluación de coherencia por época ni sobre el área de bombeo exacta.
3. El archivo de LiCSAR está en migración desde octubre de 2025; los conteos pueden cambiar. Los productos de Cerro de Pasco y Bajo Cauca podrían procesarse en el futuro.
4. El peso de un interferograma (unw + cc) es de ~18.8 MB (muestra `20200417_20200505`, marco 156D_11028_131313); los 2 584 interferogramas de ese marco suman unos 49 GB, cifra que un diseño de red reducida disminuiría. No se descargaron.
5. Las distancias GNSS-sitio son aproximadas y las coordenadas de los sitios se fijaron a mano.
6. No se verificó la existencia de redes públicas de pozos ni de datos de operación (volúmenes de salmuera) en Uyuni, Cerrejón, Cerro de Pasco ni Bajo Cauca.

## 6. Próximos pasos

1. **Uyuni**: procesar los marcos `156D_11028_131313` y `149A_11032_131313` con LiCSBAS2 y repetir el procedimiento en Atacama (`156D_11424_131313`) como control positivo, comparando con las tasas publicadas.
2. **Cerrejón**: verificar coherencia sobre y alrededor de los tajos en el marco `004A_07905_191818` y evaluar procesamiento propio de las pistas descendente 69 y ascendente 77.
3. **Cerro de Pasco y Bajo Cauca**: obtener series de tiempo, ya sea por solicitud de prioridad a COMET-LiCS (que prioriza a sus colaboradores y no garantiza atención) o por procesamiento bajo demanda con una cuenta de NASA Earthdata (trámite del titular de la cuenta).
4. **Verdad de terreno**: proponer una estación GNSS dentro del área de bombeo en Uyuni (Colcha K) y una campaña de gravimetría relativa.
5. Repetir la evaluación de NISAR cuando el registro de banda L abarque al menos dos años.
