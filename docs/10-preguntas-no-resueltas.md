# 10 — Preguntas de investigación no resueltas

Organizadas por alcance: Colombia → Suramérica → global. Cada una nace de una brecha documentada con referencias en los archivos de país correspondientes, no de especulación.

## Colombia

1. ~~¿Cuánto contribuye la subsidencia de la Sabana de Bogotá (hasta 7.5 cm/año medida) a la señal agregada de deriva polar o LOD a escala nacional?~~ — **RESUELTO 2026-09-18**: no de forma medible. Cálculo físico de primer orden (validado contra Tres Gargantas) da −0.09 a −1.4 nanosegundos/año de LOD, 4-5 órdenes de magnitud por debajo del piso de detección operativo (microsegundos). Ver `paises/01-colombia.md` §8.
2. ¿Existe subsidencia medible por InSAR en el Cerrejón, comparable a la de Atacama (1-2 cm/año)? — nunca medido públicamente.
3. ¿Cuánta masa se ha movido por minería aurífera ilegal en Chocó/Antioquia (69 123 ha en 2022) en términos gravimétricos, no solo de área deforestada? — el monitoreo actual (UNODC/SIMCI) es de área, no de masa.
4. ~~¿Cuánto del retroceso glaciar tropical colombiano se refleja de forma aislable en la señal GRACE regional andina, separado de Perú/Ecuador/Bolivia?~~ — **RESUELTO 2026-09-18**: es espacialmente separable (mascons distintos) pero irrelevante en la práctica — Colombia es solo ~1.6% del hielo andino total (30.83 km² de 2024, IDEAM) y su contribución a LOD (−0.26 a −0.52 ns/año) es indetectable, confirmado con extracción real de GRACE sobre la Cordillera Central (sin tendencia visible, dominada por ENSO). Ver `paises/01-colombia.md` §11.

## Suramérica

5. ~~¿Por qué solo Chile y Brasil tienen cuantificación geodésica satelital publicada de deformación minera?~~ — **ACTUALIZADO 2026-09-18 (parcialmente resuelto)**: son 3, no 2 — Venezuela también la tiene (DInSAR-PSI, Costa Oriental del Lago de Maracaibo, hasta 7 m de subsidencia). Esto matiza la hipótesis original: la severidad extrema del fenómeno (7 m es el mayor de todo el repositorio) parece ser suficiente por sí sola para generar instrumentación, incluso sin la capacidad institucional robusta de Chile/Brasil — Venezuela lo logró pese a su crisis institucional. Ver `paises/08-venezuela.md` §4 y `07-mineria-comparativo.md`. Queda abierto confirmar si esta hipótesis revisada (severidad extrema O capacidad institucional) explica también la ausencia de estudio en Cerrejón/Cerro de Pasco/Uyuni.
6. ¿Existe subsidencia en el Salar de Uyuni comparable a Atacama? — nunca medido públicamente, pese a compartir el mismo mecanismo de extracción.
7. ¿Existe subsidencia en Cerro de Pasco (Perú), el sitio minero más antiguo del continente? — nunca medido con InSAR/gravimetría pese a décadas de caracterización ambiental.
8. ¿Hay un vínculo cuantificable entre la sismicidad inducida de Vaca Muerta (548 sismos 2018-2025) y la señal de pérdida de masa glaciar andina en la misma cuenca hidrográfica? — nunca estudiado de forma conjunta.
9. ¿Por qué la Amazonía gana agua subterránea (+22.24 km³/año) mientras la tendencia global es de pérdida? ¿Es reversible con deforestación acelerada, y en qué horizonte temporal?
10. ¿Se ha desacelerado la subsidencia de la Costa Oriental del Lago de Maracaibo (Venezuela) en proporción a la caída de la producción petrolera nacional desde 2019? — la última medición DInSAR pública es de 2018-2019, sin actualización posterior encontrada.
11. ¿Qué llevó a que múltiples estaciones GNSS venezolanas de la red SIRGAS-CON (CN39, CN41, MARA, BANS, CRCS, CUM3) pasaran a estado "removed"? ¿Pérdida de mantenimiento institucional, o decisión deliberada? — hallazgo indirecto sin explorar, ver `paises/08-venezuela.md` §5.
12. ¿Cuánto contribuye el retroceso glaciar ecuatoriano (32.6% de pérdida nacional, hasta 54% en Cotopaxi) a la señal GRACE regional? — nunca calculado ni extraído en este repositorio (a diferencia de Colombia, donde sí se hizo), pendiente para la siguiente fase.

## Global (más allá de Suramérica, identificadas en la revisión de estado del arte de la Fase 0)

10. La resolución espacial de GRACE (~300 km) solo cubre el 10% de cuencas fluviales significativas del mundo — ¿qué sesgo introduce esto en toda la literatura de atribución hasta que NGGM/MAGIC (2032) mejore la cobertura al 80%?
11. El problema de atribución de fuente (manto vs. hielo vs. agua subterránea vs. embalses) sigue siendo matemáticamente mal condicionado — ¿qué tan generalizable es la solución de Atacama (EOF+ML) a regiones sin la misma densidad de datos de calibración? — **RESPONDIDO EN PARTE (Fase 3, 2026-09-21)**: el componente InSAR se generaliza donde ya hay interferogramas procesados (Uyuni sí; Cerrejón parcialmente; Cerro de Pasco y Bajo Cauca no); el componente de atribución con GRACE no puede basarse en detectar la extracción (señal 16 a 140 veces bajo el umbral empírico), por lo que depende de datos locales que estos sitios no tienen. Ver `12-fase3-factibilidad-metodologia-atacama.md`.
12. La cobertura de pozos de monitoreo in situ es fuerte en EE.UU./India/China y casi inexistente en África y gran parte de Suramérica — ¿cuánto sesga esto las cifras globales agregadas de depleción de acuíferos?
13. No existe un sistema operativo de alerta temprana en tiempo real que hubiera podido anticipar Brumadinho (la señal de 30 cm de subsidencia existía 12 meses antes) — ¿cuántos otros diques de relaves activos en el mundo muestran hoy una señal similar sin que nadie la esté monitoreando operativamente?
14. Ninguna proyección publicada de deriva polar o LOD va más allá de 2050 — toda proyección a 2100 (incluida la de este repositorio, `09-proyeccion-2100.md` §2-3) es necesariamente extrapolación razonada, no dato validado.

## Cómo usar esta lista

Cada pregunta es candidata a convertirse en un issue de investigación individual en este repositorio (ver milestones de GitHub). Las preguntas 2, 6 y 7 (Colombia/Bolivia/Perú) son las de mayor prioridad porque replican una metodología ya validada (Atacama) a sitios sin ningún estudio geodésico previo — el menor costo de entrada para un resultado publicable.
