# 08 — Factibilidad de integración en tiempo real

## 1. Qué existe hoy (estado del arte verificado)

| Componente | Latencia real actual | Fuente |
|---|---|---|
| GRACE-FO mascon (JPL RL06.3) | Mensual, con retraso de procesamiento de semanas | [NASA Earthdata](https://www.earthdata.nasa.gov/data/catalog/pocloud-tellus-grac-grfo-mascon-cri-grid-rl06.3-v4-rl06.3mv04) |
| IERS Bulletin A/B (EOP) | Semanal (predicciones diarias a corto plazo) | IERS |
| IGS GNSS Real-Time Service | Segundos a minutos (posicionamiento), pero no integrado con gravimetría | [IGS — GNSS Monitoring](https://igs.org/wg/gnss-monitoring/) |
| InSAR (Sentinel-1) | Revisita de 6-12 días, procesamiento posterior de días a semanas | ESA Copernicus |

**Conclusión directa**: hoy **no existe** un sistema que combine estas cuatro fuentes en tiempo real. El componente más lento (GRACE-FO, mensual con retraso) es el cuello de botella estructural — ninguna arquitectura de software puede acelerar la física de la misión satelital.

## 2. Lo más cercano a integración multi-fuente encontrado en la literatura

El estudio brasileño de "inversión conjunta de diferencia de geopotencial basada en GRACE + desplazamiento vertical GNSS" (ver `paises/02-brasil.md`) es el ejemplo más avanzado hallado en Suramérica: combina dos fuentes (gravimetría satelital + GNSS terrestre) para mejorar la resolución de la señal de almacenamiento de agua. No opera en tiempo real, pero es la base metodológica correcta.

## 3. Arquitectura propuesta (nivel de diseño, no implementada)

```
Capa 1 — Ingesta
  GRACE-FO mascon (mensual) + IERS EOP (semanal) + GNSS IGS-RT (continuo) + InSAR Sentinel-1 (6-12 días)
       │
Capa 2 — Homogenización temporal
  Modelo de gap-filling/downscaling (Transformer o LSTM, ver docs/00-marco-teorico.md §5)
  que interpola la señal de baja frecuencia (GRACE) usando la señal de alta frecuencia (GNSS) como
  variable auxiliar — exactamente el enfoque validado en Brasil, extendido a Colombia.
       │
Capa 3 — Atribución de fuente
  Modelo supervisado (EOF + ML, metodología validada en Atacama/Chile) para separar componente
  climático vs. antrópico (minería, agua subterránea, embalses) por región/cuenca.
       │
Capa 4 — Alerta temprana
  Umbral de subsidencia/deformación anómala (referencia: Brumadinho mostró 30 cm en 12 meses antes
  del colapso — un sistema con esta arquitectura corriendo en 2018 pudo haber emitido alerta).
```

## 4. Qué se necesitaría para que esto sea realmente "tiempo real" en Colombia

**Actualizado 2026-09-18 tras verificación directa (ver `paises/01-colombia.md` §6)**: el punto 1 de esta lista estaba subestimado. IGAC opera desde 2023 un Centro de Control Geodésico Nacional con servicios en tiempo real NTRIP/VRS gratuitos, PPP en línea, y descarga diaria de RINEX de toda la Red Activa GNSS — incluida al menos una estación CORS MAGNA-ECO en La Guajira. La infraestructura de posicionamiento en tiempo real **ya existe a escala nacional**.

1. ~~Estaciones GNSS de referencia densificadas~~ → **Ya existen** (Red Activa GNSS + NTRIP/VRS del IGAC). Lo pendiente es verificar densidad suficiente específicamente sobre Cerrejón y Bajo Cauca (la estación conocida de La Guajira está cerca de Riohacha, no necesariamente sobre la mina).
2. Un pipeline de descarga y procesamiento automático de Sentinel-1 sobre esos mismos sitios. **Corrección (2026-09-21, ver `12-fase3-factibilidad-metodologia-atacama.md`)**: la versión anterior de este punto afirmaba que COMET-LiCS "no cubre Colombia por defecto", tomando como base el texto del portal (foco inicial en el cinturón Alpino-Himalayo) y no el archivo de productos. Al consultar el archivo se encontró un marco procesado sobre el Cerrejón (`004A_07905_191818`, 181 épocas y 1 030 interferogramas, jul-2020 a oct-2025). La cobertura existe pero es parcial (una sola pista, desde 2020); para sitios sin marco procesado el portal admite solicitudes de prioridad a `comet.lics@leeds.ac.uk`.
3. Acceso a datos del SGC: **parcialmente resuelto** — el portal `datos.sgc.gov.co` ya expone en abierto la Red de Gravedad Absoluta (RGAC, 25 estaciones, 4 en Bogotá) y 220 puntos gravimétricos históricos, con contactos técnicos (`magnaeco@igac.gov.co`, `geotermia@sgc.gov.co`) embebidos en los metadatos. Lo que falta es gravimetría de detalle específicamente sobre Cerrejón/Bajo Cauca, que no aparece en el catálogo público — requiere solicitud directa.
4. Con la Red Activa GNSS y la RGAC ya operativas, el cuello de botella real para Colombia se reduce a dos cosas: (a) completar la cobertura InSAR de Cerrejón (parcial, ver punto 2) y de Bajo Cauca con productos abiertos o con procesamiento propio de Sentinel-1, y (b) obtener series gravimétricas de detalle del SGC sobre esos mismos sitios. Ninguna de las dos requiere lanzar un satélite nuevo ni construir infraestructura terrestre — es gestión de acceso y solicitud de procesamiento, lo que hace este objetivo más cercano de lo estimado originalmente (meses, no años, para un primer resultado preliminar).

## 5. Límite honesto

El componente gravimétrico satelital (GRACE-FO) seguirá teniendo latencia mensual hasta que NGGM/MAGIC (2032) u otra misión lo reemplace. "Tiempo real" en este dominio significa, de forma realista, **latencia de días a semanas para InSAR/GNSS, y latencia mensual irreducible para el componente de masa gravitatoria** — no hay forma honesta de prometer monitoreo instantáneo de redistribución de masa con la tecnología satelital actual.
