# Perú — caso de vacío de datos geodésicos documentado

## Cerro de Pasco

- Una de las minas metálicas más antiguas y más documentadas ambientalmente de Suramérica (plomo, zinc, plata; explotación desde inicios del s. XX, hoy con un tajo abierto que literalmente atraviesa el centro de la ciudad).
- NASA Earth Observatory ha publicado imágenes satelitales del sitio como caso de estudio visual de transformación del paisaje por minería.
- Existen análisis multiespectrales y 3D del sitio (ScienceDirect/OSTI) y documentación extensa de contaminación por metales pesados en la población.
- Hay planes recientes de análisis hidrogeológico y estudios geofísicos de subsuelo asociados al "Acuerdo Quiulacocha" (2026) para reprocesamiento de relaves.

Fuentes:
- [Mining Peru's Cerro de Pasco — NASA Earth Observatory](https://science.nasa.gov/earth/earth-observatory/mining-perus-cerro-de-pasco-144481/)
- [Temporal multispectral and 3D analysis of Cerro de Pasco, Peru — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0048969719356359)
- [Poisoned for decades by a Peruvian mine — Mongabay](https://news.mongabay.com/2023/11/poisoned-for-decades-by-a-peruvian-mine-communities-say-they-feel-forgotten/)
- [Cerro de Pasco Quiulacocha Agreement — Discovery Alert 2026](https://discoveryalert.com/financial-innovation-critical-mineral-processing-2026/)

## Hallazgo explícito de esta investigación: ausencia de literatura InSAR/gravimétrica

A diferencia de Chile (Atacama, cuantificado en cm/año con satélite) y Brasil (Brumadinho, cuantificado en cm con InSAR), **la búsqueda documental para este repositorio no encontró ningún estudio publicado que aplique InSAR o gravimetría de precisión a Cerro de Pasco** pese a ser uno de los sitios mineros más antiguos y con mayor huella superficial del continente.

Esto es, en sí mismo, un resultado de investigación relevante para `10-preguntas-no-resueltas.md`: existe abundante caracterización de contaminación química y de salud pública, pero **un vacío total en la caracterización geodésica de la deformación del terreno**, que sí se hizo en casos comparables (Atacama, Brumadinho). Es una de las oportunidades de investigación más claras y accionables de todo este repositorio — candidato natural para colaboración con universidades peruanas (PUCP, UNI) o el IGN peruano.

## Nota sobre la fórmula de excitación EOP (metodología en `00-marco-teorico.md` §6)

A diferencia de Chile/Bolivia (salmuera) o Argentina (hidrocarburos combustionados), Cerro de Pasco es minería de metales sólidos (plomo, zinc, plata) — cae en la misma categoría física que la minería aurífera de Bajo Cauca (`01-colombia.md` §10): el material excavado y los relaves se quedan dentro de la misma cuenca alto-andina, sin redistribuirse a escala de armónico esférico de grado 2. Por la regla general de `00-marco-teorico.md` §6.4, **no se aplica la fórmula** — el efecto sobre la cadena EOP es nulo por construcción, independientemente de que Cerro de Pasco sea uno de los tajos más antiguos y profundos del continente. El impacto real de este sitio sigue siendo el ya documentado arriba (contaminación, salud pública) más la brecha geodésica de deformación local (InSAR), no un efecto planetario.
