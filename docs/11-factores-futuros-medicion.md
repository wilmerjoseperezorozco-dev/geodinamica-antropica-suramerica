# 11 — Qué tendrá que medir la humanidad para un análisis inteligente integrado

Este documento responde directamente a la pregunta de investigación: si hoy la medición está fragmentada (gravimetría satelital, InSAR, GNSS, pozos, sismología, cada uno en su literatura separada), ¿qué haría falta para un análisis verdaderamente integrado?

## 1. Resolución espacio-temporal suficiente (parcialmente en camino)

- NGGM/MAGIC (2032) resuelve parte del problema de resolución de masa (300→100-150 km), pero **no** resuelve el problema de latencia — sigue siendo una misión de gravimetría orbital, no un sensor continuo.
- Falta: una red terrestre de gravímetros absolutos densificada en sitios de riesgo (minero, acuífero crítico) que sirva de "verdad de terreno" continua entre pasadas satelitales — hoy prácticamente inexistente en Suramérica fuera de estaciones geodésicas nacionales aisladas.

## 2. Separación causal, no solo correlación (el problema no resuelto más importante)

- La IA actual (LSTM, Transformers, EOF+ML) interpola y predice bien la señal combinada, pero **atribuir causa** (¿fue el clima, la minería, o el manto?) sigue dependiendo de tener un caso de calibración con datos in situ densos (como Atacama).
- Lo que faltará medir: series largas y densas de **verdad de terreno etiquetada por causa** (ej. volumen de salmuera bombeada día a día, volumen de agua subterránea extraída por pozo con telemetría) en sitios sin instrumentación hoy (Cerrejón, Cerro de Pasco, Uyuni) — sin esto, ningún modelo de IA, por sofisticado que sea, puede aprender a separar causas de forma confiable ahí.

## 3. Integración multi-escala real (de milímetros locales a centímetros globales)

- Hoy la subsidencia de un dique de relaves (cm, escala de metros) y la deriva polar global (cm/año, escala planetaria) se estudian con instrumentos y comunidades científicas completamente separadas (ingeniería geotécnica vs. geodesia espacial).
- Falta un marco de modelado que suba la señal desde la escala de sitio (InSAR de una mina) hasta la escala de cuenca (GRACE) hasta la escala global (IERS EOP) de forma trazable — hoy cada nivel se publica en revistas y con métodos distintos, sin un "puente" formal.

## 4. Series temporales suficientemente largas para separar tendencia de ruido natural

- El bamboleo de Chandler (período ~433 días) y otras oscilaciones naturales del eje de rotación se superponen a la señal antrópica. Separar ambas de forma confiable en una región específica (ej. Suramérica) requiere décadas de datos consistentes — apenas se tienen ~30 años de GRACE-equivalente (1993-presente) a escala global, y mucho menos a escala regional con la resolución necesaria.

## 5. Gobernanza de datos abiertos entre países y sectores

- El caso de Atacama funcionó porque hubo acceso académico a datos satelitales + publicación abierta. En minería, buena parte de los datos operativos reales (volumen bombeado, profundidad de tajo día a día) son privados y no se publican — la brecha de Cerrejón/Cerro de Pasco/Uyuni documentada en este repositorio puede deberse tanto a falta de estudio académico como a falta de acceso a datos operativos de las empresas.
- Lo que la humanidad tendrá que resolver no es solo técnico: es un acuerdo de **transparencia obligatoria de datos operativos mineros/hídricos** para investigación ambiental, similar a lo que ya existe en algunos países para emisiones de CO₂.

## 6. Síntesis: la lista mínima de "lo que faltará medir"

1. Verdad de terreno etiquetada por causa en sitios sin instrumentación (Colombia, Perú, Bolivia).
2. Redes de gravímetros terrestres densificadas en sitios de riesgo.
3. Framework formal de trazabilidad multi-escala (sitio → cuenca → global).
4. Series temporales regionales de 30+ años con resolución suficiente para separar señal antrópica de variabilidad natural.
5. Marco de gobernanza de datos operativos mineros/hídricos abiertos para investigación.

Ninguno de estos cinco puntos requiere una tecnología que no exista hoy — son, en su mayoría, problemas de despliegue, acceso a datos y coordinación institucional, no de investigación básica pendiente. Esa es la conclusión más importante de este documento.
