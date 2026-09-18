# Brasil — el caso mejor instrumentado de la región

## 1. Amazonía — GRACE y almacenamiento de agua subterránea

- La cuenca amazónica es uno de los pocos casos suramericanos con **downscaling de GRACE/GRACE-FO validado con machine learning**: de resolución nativa 1° (~110 km) a 0.25° (~27.5 km), periodo 2002-2021.
- Resultado: el almacenamiento terrestre total aumenta a 14.26 ± 1.18 km³/año, y el almacenamiento de agua subterránea a 22.24 ± 1.18 km³/año — es decir, en la Amazonía la señal dominante **no es agotamiento sino ganancia**, contraria a la tendencia global de otras regiones (India, oeste de EE.UU.).
- El agua subterránea es el componente dominante del ciclo hidrológico amazónico porque el nivel freático es someramente profundo en la mayor parte de la cuenca.
- Estudio complementario 2025-2026: "Two decades of human- and climate-induced groundwater storage shifts in Brazil" (*Science Advances*) — separa explícitamente componente climático vs. antrópico a escala de todo el país, no solo la Amazonía.

Fuentes:
- [Characterization of groundwater storage changes in the Amazon River Basin — PubMed](https://pubmed.ncbi.nlm.nih.gov/38029979/)
- [Two decades of human- and climate-induced groundwater storage shifts in Brazil — Science Advances](https://www.science.org/doi/10.1126/sciadv.aee0266)
- [Groundwater dominates terrestrial hydrological processes in the Amazon — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022169423012544)
- [Estimation of TWS changes in Brazil from joint inversion GRACE + GNSS — ResearchGate](https://www.researchgate.net/publication/385565618_Estimation_of_Terrestrial_Water_Storage_Changes_in_Brazil_From_the_Joint_Inversion_of_GRACE-Based_Geopotential_Difference_and_GNSS_Vertical_Displacement_Data)

**Relevancia metodológica**: el estudio de inversión conjunta GRACE + desplazamiento vertical GNSS es, de toda la literatura suramericana revisada en este repositorio, **el que más se acerca a una arquitectura de monitoreo integrado multisensor** (ver `08-tiempo-real.md`). Es el modelo a replicar para Colombia.

## 2. Brumadinho — subsidencia InSAR como señal de alerta temprana (caso de referencia, no hipotético)

- El dique de relaves de la mina de hierro de Brumadinho (Vale S/A) colapsó el 25 de enero de 2019, con 259 muertos confirmados y 11 desaparecidos.
- Mediciones InSAR retrospectivas mostraron **subsidencia de hasta 30 cm en la parte trasera del dique durante los 12 meses previos al colapso**.
- Este es el caso documentado más fuerte de esta investigación de que la teledetección geodésica **pudo haber servido como sistema de alerta temprana** si se hubiera monitoreado operativamente en tiempo real, no solo de forma retrospectiva/forense.

Fuente: [The 2019 Brumadinho tailings dam collapse: possible cause and impacts — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0303243420300192)

**Brecha identificada**: la señal existía 12 meses antes del desastre pero no había un sistema operativo de alerta basado en InSAR corriendo en tiempo real sobre la infraestructura minera brasileña en 2019. Punto de partida directo para `08-tiempo-real.md` y para el argumento de por qué esta investigación importa más allá de lo académico.

## 3. Aplicación de la fórmula de excitación EOP — el caso más grande e interesante del repositorio (metodología en `00-marco-teorico.md` §6)

Este es el único caso de todo el repositorio donde hay **ganancia** neta de masa en vez de extracción, y también el de mayor magnitud absoluta con diferencia — vale la pena calcularlo aunque no sea un caso de "minería".

### Dato de entrada

- Ganancia neta de almacenamiento terrestre de agua en la Amazonía: **+14.26 km³/año** (dato ya documentado en §1, Characterization of groundwater storage changes in the Amazon River Basin).
- Esta masa, físicamente, tiene que provenir de una reducción de humedad/precipitación en otra parte del ciclo global (en última instancia, del promedio océano-atmósfera) — es el proceso inverso al de un acuífero que se agota.
- Latitud del centro de masa de la cuenca amazónica: φ ≈ 3°S.

### Cálculo

Como aquí la masa se **añade** a tierra (no se extrae), el signo del factor se invierte respecto a los casos anteriores:

```
ΔM = 14.26×10⁹ m³/año × 1000 kg/m³ = 1.426×10¹³ kg/año   (≈2 300 veces la masa de Atacama)
cos²(3°) = 0.9973  →  factor (cos²φ − 2/3) = +0.3306
ΔC = 1.426×10¹³ × (6.371×10⁶)² × 0.3306 ≈ +1.91×10²⁶ kg·m²
ΔLOD ≈ +0.21 microsegundos/año
```

### Resultado — el único caso que se acerca a la escala de fenómenos ya documentados

- **+0.21 microsegundos/año** es ~2 000 a 4 000 veces mayor que cualquier caso minero calculado en este repositorio (Bogotá, Cerrejón, Atacama, Uyuni, todos en el rango de 0.08-0.5 **nano**segundos/año).
- Es del mismo **orden de magnitud** que el efecto de un solo llenado de Tres Gargantas (0.06-0.13 µs) — pero la Amazonía lo produce **cada año**, de forma sostenida desde al menos 2002.
- Sigue siendo **~5 000 a 10 000 veces menor** que la variabilidad natural de LOD por El Niño/La Niña y momento angular atmosférico (±1-2 milisegundos, ver `00-marco-teorico.md` §1) — por lo que no es "la explicación" de ningún evento observado, pero es el primer caso de este repositorio donde el efecto calculado deja de ser trivialmente despreciable frente a fenómenos geodésicos reales conocidos.
- Consistencia externa: la literatura de geodesia ya reconoce que el ciclo estacional de almacenamiento de agua en la Amazonía es uno de los mayores contribuyentes a la señal **estacional** de LOD a nivel mundial (junto al momento angular atmosférico) — mi cálculo es de la **tendencia de largo plazo**, una cantidad distinta pero del mismo mecanismo físico, lo que da una validación cualitativa adicional de que el orden de magnitud es razonable.

**Implicación para el discurso de "riesgo" de este repositorio**: si la Amazonía revirtiera su tendencia actual (ganancia) hacia pérdida neta por deforestación acelerada — la pregunta 9 de `10-preguntas-no-resueltas.md`, todavía sin resolver — el signo de esta contribución se invertiría, y por ser la de mayor magnitud de todo el repositorio, sería la primera candidata realista (aunque siga siendo pequeña frente al ruido natural) a producir un efecto medible en el balance de LOD a escala de Suramérica.

## 4. Síntesis de brechas específicas de Brasil

1. La cuenca amazónica está bien instrumentada, pero el resto del territorio minero brasileño (Minas Gerais, Pará) carece de la misma cobertura de downscaling GRACE+GNSS.
2. Brumadinho demuestra la tecnología (InSAR) pero no existe evidencia de que se haya institucionalizado un monitoreo satelital operativo post-2019 a escala nacional de todos los diques de relaves activos.
