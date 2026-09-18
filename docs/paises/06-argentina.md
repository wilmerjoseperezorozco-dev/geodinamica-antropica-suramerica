# Argentina — sismicidad inducida documentada, cruce con glaciares sin resolver

## Vaca Muerta (Cuenca Neuquina) — sismicidad inducida por fracking

- El Observatorio de Sismicidad Inducida (OSI) registró **548 sismos entre 2018 y junio de 2025** en la formación Vaca Muerta.
- Estudio de atribución estadística: ~0.5% de las operaciones de fractura hidráulica se asocian con sismos, con correlación temporal >99.99% de confianza entre sismicidad y tasas de inyección de fluido.
- El aumento en el número de etapas de fractura por pozo (de ~10 en los primeros pozos a >50 en pozos recientes) se ha vinculado con el aumento de sismos en la región.
- Estudio complementario (*Scientific Reports*, 2022): evaluación de deformación del terreno y sismicidad en dos áreas de producción intensiva de hidrocarburos en la Patagonia argentina.

Fuentes:
- [Chasing the ghost of fracking in the Vaca Muerta Formation — Seismica](https://seismica.library.mcgill.ca/article/view/1435)
- [Fracking-Induced Earthquakes Are Menacing Argentina — Inside Climate News](https://insideclimatenews.org/news/14042024/argentina-fracking-earthquakes/)
- [Assessment of ground deformation and seismicity in two areas of intense hydrocarbon production in Argentinian Patagonia — Scientific Reports](https://www.nature.com/articles/s41598-022-23160-6)

**Relevancia para este repositorio**: es el único caso suramericano encontrado donde la redistribución/alteración de esfuerzo en la corteza por actividad extractiva se mide directamente en términos sismológicos operativos (un observatorio dedicado, OSI), no solo en estudios académicos puntuales. Es un modelo institucional a considerar para Colombia si se documentara sismicidad inducida por minería o inyección de fluidos.

## Glaciares andinos y GRACE — brecha de integración

La búsqueda específica de un estudio que **cruce la sismicidad/deformación de Vaca Muerta con la señal GRACE de pérdida de masa glaciar andina** no arrojó resultados. Ambos fenómenos se estudian en la literatura de forma completamente separada (geofísica de hidrocarburos vs. glaciología), pese a ocurrir en el mismo país y, en parte, en cuencas hidrográficas relacionadas.

**Brecha identificada**: no existe un estudio integrado de balance de masa a escala de Argentina que combine (a) pérdida de hielo andino, (b) extracción de hidrocarburos no convencionales y su sismicidad inducida, y (c) su efecto conjunto en la señal gravitatoria regional. Esta es exactamente el tipo de síntesis multi-fuente que este repositorio identifica como ausente en toda la región (ver `10-preguntas-no-resueltas.md`).

## Aplicación de la fórmula de excitación EOP a Vaca Muerta (metodología en `00-marco-teorico.md` §6)

A diferencia de la minería de sólidos (oro en Bajo Cauca), el petróleo extraído de Vaca Muerta **sí** cumple la condición de §6.4: se transporta, se refina y se combustiona, liberando CO₂/H₂O que se mezcla en la atmósfera global en 1-2 años — una redistribución genuinamente global, incluso más rápida y completa que la del agua subterránea hacia el océano.

### Dato de entrada (verificado en vivo, 2026-09-18)

- Producción de petróleo de Vaca Muerta: **628 924 barriles/día** (abril 2026, récord histórico). 1 barril ≈ 159 L; densidad del crudo ≈ 850 kg/m³.
- ΔM ≈ 628 924 bbl/día × 159 L/bbl × 365 días × 0.85 kg/L ≈ **3.1×10¹⁰ kg/año**.
- Latitud de la Cuenca Neuquina: φ ≈ 38.5°S.

### Cálculo

```
cos²(38.5°) = 0.6125  →  factor (2/3 − cos²φ) = +0.0542   (positivo: 38.5° está más allá del "ángulo mágico" de 35.26°)
ΔC ≈ +6.82×10²² kg·m²
ΔLOD ≈ +0.073 nanosegundos/año
```

### Resultado

Vaca Muerta está a solo 3.2° del "ángulo mágico" (35.26°S) donde el factor cos²φ se anula exactamente — es, por pura coincidencia geográfica, una de las peores latitudes posibles para que una fuente de esta masa tenga efecto en LOD, pese a mover una masa comparable a Bogotá o el Cerrejón. Para deriva polar, en cambio, sin(2×38.5°)=0.974, casi el máximo teórico — **Vaca Muerta tendría el mayor apalancamiento de todo el repositorio sobre deriva polar por unidad de masa si la sustancia extraída fuera agua**; con hidrocarburos combustionados el mecanismo de excitación de bamboleo es menos directo (no hay un análogo limpio al "agua vuelve al océano") y se deja fuera de este cálculo para no sobre-extender la fórmula más allá de su validación.

**Conclusión**: mismo resultado que todos los casos anteriores — indetectable, esta vez además favorecido por una coincidencia geográfica real (proximidad al ángulo mágico) que sí vale la pena documentar como curiosidad geofísica genuina, no solo como resultado nulo.
