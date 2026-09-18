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

## 3. Síntesis de brechas específicas de Brasil

1. La cuenca amazónica está bien instrumentada, pero el resto del territorio minero brasileño (Minas Gerais, Pará) carece de la misma cobertura de downscaling GRACE+GNSS.
2. Brumadinho demuestra la tecnología (InSAR) pero no existe evidencia de que se haya institucionalizado un monitoreo satelital operativo post-2019 a escala nacional de todos los diques de relaves activos.
