# Geodinámica Antrópica de Suramérica

**Redistribución de masa terrestre inducida por el ser humano (minería, extracción de agua subterránea, embalses) y su efecto medible en la rotación, la deriva polar y el nivel del mar — con foco inicial en Colombia y expansión documentada a Suramérica.**

> Estado: Fase 0 — Marco teórico y línea base completados. Fase 1 (Colombia) en curso.

---

## 1. Qué investiga este repositorio

Existe evidencia geodésica sólida (satelital y observacional) de que la actividad humana — extracción de agua subterránea, minería a cielo abierto, embalses y explotación de salares — mueve masa a una escala que ya es detectable en:

- El **eje de rotación terrestre** (deriva polar, ~cm/año en episodios documentados)
- La **duración del día** (LOD, variaciones de microsegundos a milisegundos)
- El **nivel del mar** (mm/año acumulativos)
- La **corteza local** (subsidencia de cm/año a decenas de cm/año en sitios puntuales)

Lo que **no existe** es un inventario documentado, con referencias verificables, de qué se ha medido específicamente en Colombia y Suramérica, dónde están los vacíos de datos, y qué arquitectura permitiría pasar de estudios retrospectivos aislados a un monitoreo sistemático. Ese es el objetivo de este repositorio: no reprocesar los datos crudos de las misiones satelitales (eso ya lo hace JPL/NASA/ESA/IERS), sino **mapear el estado del arte, identificar explícitamente lo que no se ha medido, y proponer una hoja de ruta de investigación replicable**.

## 2. Objetivo general

Producir un inventario documentado y con referencias verificables del estado del conocimiento sobre redistribución antrópica de masa terrestre (minería, agua subterránea, embalses) en Colombia y Suramérica, identificando explícitamente las brechas de medición, y proponer una arquitectura de monitoreo en tiempo real y proyecciones a 2100 basadas en literatura revisada por pares.

## 3. Objetivos específicos

1. Documentar, país por país (Colombia primero), los estudios existentes de gravimetría, InSAR/subsidencia, GRACE/GRACE-FO y monitoreo de acuíferos vinculados a minería y extracción de agua.
2. Formular explícitamente las preguntas de investigación que **no** han sido abordadas en Colombia, en Suramérica, ni en el resto del mundo respecto a este fenómeno.
3. Evaluar la factibilidad técnica de integrar estas fuentes (GRACE-FO, GNSS, InSAR, pozos de monitoreo) en un sistema de seguimiento cercano al tiempo real.
4. Proyectar, con la mejor evidencia disponible (IPCC AR6 y literatura de atribución), el posible escenario a 2100 para la región.
5. Consolidar un comparativo de minería por país (Colombia, Perú, Chile, Bolivia, Brasil, Argentina) con estudios geodésicos/ambientales asociados.
6. Publicar el trabajo con control de versiones, citación formal (CITATION.cff) y DOI vía Zenodo.

## 4. Alcance y lo que este proyecto NO es

- No es una misión de observación satelital nueva ni reemplaza a GRACE-FO/IERS/SGC.
- No genera datos primarios propios en esta fase; **sintetiza y referencia** literatura científica y técnica existente, señalando explícitamente cuando algo es una proyección/estimación propia vs. un dato medido y publicado.
- No hace afirmaciones catastrofistas: cada cifra de "gravedad" está acotada a la magnitud reportada en la fuente citada.

## 5. Estructura del repositorio

```
docs/
  00-marco-teorico.md          Rotación, traslación, LOD, deriva polar, altimetría/gravimetría — base física
  paises/
    01-colombia.md             Sabana de Bogotá, La Guajira/Cerrejón, glaciares tropicales, minería aurífera
    02-brasil.md                Amazonía (GRACE), Brumadinho (InSAR)
    03-chile.md                  Salar de Atacama (litio, subsidencia, GRACE+ML)
    04-peru.md                    Cerro de Pasco — caso de vacío de datos geodésicos
    05-bolivia.md                 Salar de Uyuni — caso de vacío de datos geodésicos
    06-argentina.md               Vaca Muerta (sismicidad inducida), Andes (glaciares)
    07-ecuador.md                  Glaciares (Cotopaxi/Antisana/Chimborazo), latitud ecuatorial óptima para LOD
    08-venezuela.md                Costa Oriental del Lago de Maracaibo — hasta 7 m de subsidencia petrolera
  07-mineria-comparativo.md    Tabla comparativa por país
  08-tiempo-real.md            Arquitectura propuesta de monitoreo casi en tiempo real
  09-proyeccion-2100.md        Escenarios a 2100 basados en IPCC AR6 + extrapolación regional
  10-preguntas-no-resueltas.md Brechas de investigación explícitas (Colombia, Suramérica, mundo)
  11-factores-futuros-medicion.md  Qué tendrá que medir la humanidad para un análisis inteligente integrado
CITATION.cff
LICENSE
```

## 6. Metodología

1. Búsqueda dirigida en literatura revisada por pares (AGU, ScienceDirect, Nature, Springer), reportes institucionales (SGC, IPCC, NASA/JPL, ESA) y prensa especializada verificable.
2. Cada afirmación cuantitativa cita la fuente primaria con enlace directo.
3. Toda brecha de datos se documenta explícitamente como tal — "no se encontró estudio publicado sobre X" es un resultado válido de esta investigación, no un vacío que se rellena con especulación.
4. Las proyecciones a 2100 parten de escenarios oficiales (IPCC AR6 SSP1-1.9 a SSP5-8.5) y se extrapolan regionalmente con supuestos declarados explícitamente.

## 7. Seguimiento del proyecto

- [Milestones](https://github.com/wilmerjoseperezorozco-dev/geodinamica-antropica-suramerica/milestones) — 7 fases, de la línea base (completada) a la publicación con DOI.
- [Issues](https://github.com/wilmerjoseperezorozco-dev/geodinamica-antropica-suramerica/issues) — cada pregunta de investigación de `docs/10-preguntas-no-resueltas.md` es un issue rastreable.

## 8. Cómo citar

Ver [CITATION.cff](CITATION.cff) y [.zenodo.json](.zenodo.json). DOI de Zenodo pendiente de activación — ver [issue de Fase 6](https://github.com/wilmerjoseperezorozco-dev/geodinamica-antropica-suramerica/milestone/7).

## 9. Licencia

Contenido documental bajo [CC BY 4.0](LICENSE).

## 10. Autor

Wilmer José Pérez Orozco — investigación independiente, Barranquilla/Tubará, Atlántico, Colombia.
