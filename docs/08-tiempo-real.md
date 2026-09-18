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

1. Estaciones GNSS de referencia densificadas sobre sitios críticos (Sabana de Bogotá, Cerrejón, Bajo Cauca) — la red IGS actual en Colombia es dispersa fuera de las estaciones geodésicas nacionales del IGAC.
2. Un pipeline de descarga y procesamiento automático de Sentinel-1 sobre esos mismos sitios (técnicamente factible hoy, sin desarrollo de hardware nuevo).
3. Acuerdo de acceso a datos del SGC (gravimetría histórica de la Sabana de Bogotá) para calibrar el modelo de atribución.
4. Ninguna de estas tres cosas requiere lanzar un satélite nuevo — es integración de fuentes existentes, lo que hace este objetivo realista a 2-3 años si se prioriza como proyecto de investigación aplicada, no como ciencia básica de largo plazo.

## 5. Límite honesto

El componente gravimétrico satelital (GRACE-FO) seguirá teniendo latencia mensual hasta que NGGM/MAGIC (2032) u otra misión lo reemplace. "Tiempo real" en este dominio significa, de forma realista, **latencia de días a semanas para InSAR/GNSS, y latencia mensual irreducible para el componente de masa gravitatoria** — no hay forma honesta de prometer monitoreo instantáneo de redistribución de masa con la tecnología satelital actual.
