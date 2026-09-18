# Venezuela — el caso de subsidencia más severo de todo el repositorio

## 1. Costa Oriental del Lago de Maracaibo — hasta 7 metros de hundimiento

Este es, de toda la investigación realizada en este repositorio (Colombia, Chile, Bolivia, Brasil, Argentina, Perú, Ecuador), **el caso de subsidencia de mayor magnitud absoluta encontrado** — casi dos órdenes de magnitud mayor que la Sabana de Bogotá.

- La extracción petrolera en la Costa Oriental del Lago de Maracaibo (campos Lagunillas, Tía Juana, Bachaquero) ha causado subsidencia acumulada de **hasta 7 metros** desde que la explotación comenzó en el siglo XX (el campo se descubrió en 1914 y entró en producción en 1922).
- Mecanismo físico: compactación de los yacimientos petrolíferos por la extracción del fluido — el mismo principio que causa subsidencia por extracción de agua subterránea (Bogotá, Ciudad de México), pero con petróleo y sobre más de un siglo de explotación continua.
- **Bolívar Coastal Fields**: el complejo petrolero más grande de Suramérica y uno de los más grandes del mundo fuera de Medio Oriente (6 000-7 000 pozos a lo largo de 56 km de costa), con más de 5 500 millones de barriles de reservas probadas. La cuenca de Maracaibo en conjunto acumula **más de 35 000 millones de barriles** producidos históricamente.
- Consecuencias documentadas: inundación y filtración de agua en zonas urbanas construidas sobre el área subsidida, contaminación ambiental extensa, y un histórico "derrame constante de crudo" en la orilla del lago por infraestructura dañada.

Fuentes:
- [Bolivar Coastal Fields — Wikipedia](https://en.wikipedia.org/wiki/Bolivar_Coastal_Fields)
- [Maracaibo Basin — Wikipedia](https://en.wikipedia.org/wiki/Maracaibo_Basin)
- [Costa Oriental del Lago de Maracaibo — Wikipedia](https://en.wikipedia.org/wiki/Costa_Oriental_del_Lago_de_Maracaibo)
- [El Lago de Maracaibo, un "constante derrame de crudo" — Semanario Universidad](https://semanariouniversidad.com/mundo/el-lago-de-maracaibo-en-venezuela-un-constante-derrame-de-crudo/)

## 2. Instrumentación geodésica — el tercer caso mejor documentado de la región

A diferencia de Cerrejón, Cerro de Pasco o Uyuni, Venezuela **sí tiene** cuantificación geodésica satelital reciente y publicada:

- Estudio con imágenes Sentinel-1 (banda C, 2018-2019, 20 imágenes en modo ascendente, técnica **DInSAR-PSI**): tasas de deformación entre **+45 mm/año (levantamiento) y −40 mm/año (subsidencia)** en las ciudades costeras orientales del lago, con **−3 cm/año específicamente en Lagunillas**.
- Es la primera vez que se determina subsidencia en Venezuela con tecnología DInSAR de acceso libre (antes solo se monitoreaba con nivelación geodésica clásica y GPS).
- El levantamiento (+45 mm/año) en algunas zonas sugiere procesos de reinyección de agua/fluidos en ciertos yacimientos para mantener presión — un patrón espacial mixto (subsidencia + levantamiento localizado) más complejo que el caso simple de Bogotá o Atacama.

Fuentes:
- [Estudio de las deformaciones de la corteza derivadas de la geodinámica a partir de InSAR: aplicación a la Costa Oriental del Lago de Maracaibo — SciELO México 2025](https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S2663-39812025000100121)
- [Detección de subsidencia por efecto de extracción petrolera aplicando DInSAR en Venezuela](https://ojs.revistamapping.com/MAPPING/article/download/204/67/340)
- [DInSAR para Análisis Geomecánico de Yacimientos — Lagunillas Inferior 07 — ResearchGate](https://www.researchgate.net/publication/390007907_DInSAR_para_Analisis_Geomecanico_de_Yacimientos_-_Aplicacion_al_Yacimiento_Lagunillas_Inferior_07_Lago_de_Maracaibo_Venezuela)

**Esto añade un tercer caso al patrón de `07-mineria-comparativo.md`**: de los ahora 8 sitios revisados en la región, **3 (Chile, Brasil, Venezuela)** tienen cuantificación geodésica satelital publicada — no 2 como se documentó en la Fase 0. Ver actualización de la hipótesis en §4.

## 3. Aplicación de la fórmula de excitación EOP (metodología en `00-marco-teorico.md` §6) — con caveat de calidad de dato

A diferencia de la subsidencia local (que depende de la compactación puntual del yacimiento), el efecto en la cadena EOP depende de cuánto petróleo se extrae y se combustiona globalmente por año — no de cuántos metros se hunde el terreno.

**Caveat honesto, específico de Venezuela**: las estadísticas de producción petrolera venezolana son notoriamente poco transparentes desde hace más de una década (colapso de PDVSA, sanciones, ausencia de reportes auditados) — a diferencia de todos los demás países de este repositorio, aquí no hay una cifra oficial confiable de producción actual específica de la Costa Oriental del Lago. Se usa una cifra ilustrativa de orden de magnitud, marcada explícitamente como tal.

```
Estimación ilustrativa: ~1 millón de barriles/día atribuible históricamente a la cuenca de Maracaibo
ΔM ≈ 58×10⁶ m³/año × 930 kg/m³ (crudo pesado, API<22) ≈ 5.4×10¹⁰ kg/año
φ_Maracaibo ≈ 9.8°N  →  cos²(9.8°) = 0.971  →  factor = −0.304
ΔLOD ≈ −0.72 nanosegundos/año
```

**Resultado**: sería, con esta cifra ilustrativa, el caso de mayor magnitud de LOD entre todas las operaciones industriales individuales de este repositorio (por encima de Atacama) — pero dado el caveat de calidad de dato, este número debe tratarse como el menos confiable de todo el repositorio en cuanto a su insumo (el mecanismo físico y el orden de magnitud sí son sólidos). Sigue estando 2 órdenes de magnitud por debajo de Tres Gargantas — el veredicto cualitativo (indetectable) no cambia aunque la cifra de entrada tenga incertidumbre.

## 4. Actualización de la hipótesis de `09-proyeccion-2100.md` §4

La Fase 0 de este repositorio planteó que la variable determinante para tener instrumentación geodésica publicada era "un grupo universitario local con acceso a InSAR/GRACE y motivación de publicación", no la severidad del fenómeno. El caso venezolano **matiza esa hipótesis**: aquí el fenómeno es tan severo y tan antiguo (7 metros en un siglo) que motivó estudio incluso en el contexto de crisis institucional profunda que atraviesa el país — sugiriendo que la severidad extrema del fenómeno **sí puede ser suficiente por sí sola** para generar investigación, incluso sin la capacidad institucional robusta que tienen Chile o Brasil. La ausencia de estudio geodésico en Cerrejón, Cerro de Pasco o Uyuni parece entonces depender más de que esos fenómenos, aunque reales, no han cruzado un umbral de visibilidad pública comparable (ningún colapso masivo como Brumadinho, ninguna cifra tan extrema como 7 metros).

## 5. Síntesis de brechas — Venezuela

1. La tasa reciente de subsidencia (2018-2019) no se ha actualizado públicamente con datos post-2019 — dado el ritmo de declive de la industria petrolera venezolana en ese período, sería valioso saber si la subsidencia se ha desacelerado en proporción a la caída de producción.
2. Sin cifra de producción petrolera confiable y auditada específica de la cuenca de Maracaibo para años recientes — limita la precisión de cualquier cálculo de excitación EOP para este país, a diferencia de todos los demás casos del repositorio.
3. Sin estudio que conecte la subsidencia de Maracaibo con la red GNSS venezolana — varias estaciones SIRGAS-CON venezolanas (CN39, CN41, MARA, BANS, CRCS, CUM3) figuran con estado **"removed"** en el listado oficial de SIRGAS (verificado en `01-colombia.md` §6.4 durante la Fase 1), sugiriendo pérdida de capacidad de monitoreo geodésico continuo en el país — un hallazgo indirecto preocupante que merece su propio issue de investigación.
