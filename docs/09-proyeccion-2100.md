# 09 — Proyección a 2100

**Nota metodológica obligatoria**: todo lo que sigue combina cifras oficiales de IPCC AR6 (medidas, con incertidumbre reportada) con una extrapolación regional propia hacia Suramérica (marcada explícitamente como estimación, no como dato medido). No se debe citar la sección 3 de este documento como si fuera una cifra del IPCC.

## 1. Cifras oficiales IPCC AR6 (verificadas, no estimadas por este repositorio)

| Variable | 2000-2010 | 2099 (proyección) |
|---|---|---|
| Extracción global de agua subterránea no renovable | 304 km³/año (2010) | 597 km³/año (2099) |
| Agotamiento de agua subterránea (depletion) | ~204 ± 30 km³/año (2000) | ~427 ± 56 km³/año (2099) |
| Contribución de agua subterránea al nivel del mar | 0.57 mm/año (2000) | 0.82 mm/año (2050, proyección intermedia) |
| Subida global del nivel del mar a 2100 (relativo a 1995-2014) | — | 0.28-0.55 m (SSP1-1.9, muy bajas emisiones) a 0.63-1.01 m (SSP5-8.5, muy altas emisiones) |

Fuente: [IPCC AR6 Sea Level Projection Tool — NASA](https://sealevel.nasa.gov/ipcc-ar6-sea-level-projection-tool?type=global&info=true.1), [RealClimate — Sea level in AR6](https://www.realclimate.org/index.php/archives/2021/08/sea-level-in-the-ipcc-6th-assessment-report-ar6/)

**Hallazgo clave ya documentado en la conversación previa de esta investigación**: se proyecta que en ~50 años el agotamiento de acuíferos podría igualar en magnitud la contribución actual de glaciares y casquetes de hielo al nivel del mar — un cambio estructural en el balance atribuido de la subida del nivel del mar que hoy el discurso público no refleja (sigue centrado casi exclusivamente en deshielo).

## 2. Lectura por escenario para el componente rotacional/geodésico (extrapolación razonada, no cifra oficial)

Si la extracción de agua subterránea casi se duplica hacia 2099 (304→597 km³/año) y esa extracción sigue geográficamente concentrada (como en el patrón 1993-2010 de Seo et al. 2023: oeste de Norteamérica, noroeste de India), entonces, **por el mismo mecanismo físico ya medido**, es razonable esperar que la tasa de deriva polar de ~4.36 cm/año observada en 1993-2010 **no se mantenga constante sino que crezca** en proporción similar al crecimiento de la extracción — es decir, del orden de una duplicación, sujeta a dónde se concentre geográficamente la nueva extracción (India, China, EE.UU., y crecientemente el sur global, incluida Suramérica).

Esto es una hipótesis razonada a partir de proporcionalidad física simple (más masa movida → más torque sobre el eje), **no una proyección publicada en la literatura revisada** — no se encontró ningún estudio que proyecte la deriva polar más allá de 2050. Se marca explícitamente como brecha en `10-preguntas-no-resueltas.md`.

## 3. Escenario Suramérica a 2100 (estimación propia de este repositorio, declarada como tal)

Supuestos explícitos:
- La demanda de litio (Chile, Bolivia, Argentina — el "triángulo del litio") crecerá con la transición energética global, lo que sugiere más extracción de salmuera, no menos, salvo cambio tecnológico hacia extracción directa de litio (DLE) que requiere menos agua.
- La demanda de cobre y minerales críticos (ver investigación paralela del autor sobre minería de cobre en Colombia) sugiere expansión, no contracción, de minería a cielo abierto en la región hacia 2030-2050.
- La Amazonía es hoy una excepción (ganancia neta de agua subterránea, no pérdida) — si esa tendencia se revierte por deforestación y cambio climático, Brasil podría pasar de "caso atípico positivo" a sumarse al patrón global de agotamiento, lo cual cambiaría materialmente el balance regional.

**Proyección cualitativa (no cuantitativa) para 2100**: es razonable esperar que Suramérica pase de ser una región subrepresentada en la literatura de atribución geodésica (como documenta este repositorio) a una región con score de riesgo creciente, concentrado en el triángulo del litio (Chile-Bolivia-Argentina) y en las cuencas mineras de Colombia y Perú — **si** la tendencia de expansión minera se mantiene y **si** no se despliega la instrumentación de monitoreo que hoy falta (ver `07-mineria-comparativo.md`).

## 4. Patrón óptimo identificado para investigación futura

El patrón que mejor explica qué sitios SÍ tienen medición geodésica cuantitativa (Chile, Brasil) frente a los que no (Colombia, Perú, Bolivia) no es el tamaño del yacimiento ni la severidad del impacto ambiental — es **la existencia de un grupo de investigación universitario local con acceso a InSAR/GRACE y motivación de publicación** (Universidad de Chile en el caso de Atacama). Esto sugiere que la intervención de mayor retorno no es tecnológica sino de **alianza institucional**: vincular este repositorio con un grupo geodésico universitario colombiano (ver issue de milestone correspondiente) es más determinante para cerrar la brecha que cualquier mejora de sensor.
