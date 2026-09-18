# 10 — Preguntas de investigación no resueltas

Organizadas por alcance: Colombia → Suramérica → global. Cada una nace de una brecha documentada con referencias en los archivos de país correspondientes, no de especulación.

## Colombia

1. ~~¿Cuánto contribuye la subsidencia de la Sabana de Bogotá (hasta 7.5 cm/año medida) a la señal agregada de deriva polar o LOD a escala nacional?~~ — **RESUELTO 2026-09-18**: no de forma medible. Cálculo físico de primer orden (validado contra Tres Gargantas) da −0.09 a −1.4 nanosegundos/año de LOD, 4-5 órdenes de magnitud por debajo del piso de detección operativo (microsegundos). Ver `paises/01-colombia.md` §8.
2. ¿Existe subsidencia medible por InSAR en el Cerrejón, comparable a la de Atacama (1-2 cm/año)? — nunca medido públicamente.
3. ¿Cuánta masa se ha movido por minería aurífera ilegal en Chocó/Antioquia (69 123 ha en 2022) en términos gravimétricos, no solo de área deforestada? — el monitoreo actual (UNODC/SIMCI) es de área, no de masa.
4. ~~¿Cuánto del retroceso glaciar tropical colombiano se refleja de forma aislable en la señal GRACE regional andina, separado de Perú/Ecuador/Bolivia?~~ — **RESUELTO 2026-09-18**: es espacialmente separable (mascons distintos) pero irrelevante en la práctica — Colombia es solo ~1.6% del hielo andino total (30.83 km² de 2024, IDEAM) y su contribución a LOD (−0.26 a −0.52 ns/año) es indetectable, confirmado con extracción real de GRACE sobre la Cordillera Central (sin tendencia visible, dominada por ENSO). Ver `paises/01-colombia.md` §11.

## Suramérica

5. ¿Por qué solo Chile y Brasil tienen cuantificación geodésica satelital publicada de deformación minera, de 7 sitios mayores revisados? (ver `09-proyeccion-2100.md` §4 — hipótesis: capacidad institucional local, no severidad del fenómeno).
6. ¿Existe subsidencia en el Salar de Uyuni comparable a Atacama? — nunca medido públicamente, pese a compartir el mismo mecanismo de extracción.
7. ¿Existe subsidencia en Cerro de Pasco (Perú), el sitio minero más antiguo del continente? — nunca medido con InSAR/gravimetría pese a décadas de caracterización ambiental.
8. ¿Hay un vínculo cuantificable entre la sismicidad inducida de Vaca Muerta (548 sismos 2018-2025) y la señal de pérdida de masa glaciar andina en la misma cuenca hidrográfica? — nunca estudiado de forma conjunta.
9. ¿Por qué la Amazonía gana agua subterránea (+22.24 km³/año) mientras la tendencia global es de pérdida? ¿Es reversible con deforestación acelerada, y en qué horizonte temporal?

## Global (más allá de Suramérica, identificadas en la sesión previa de esta investigación)

10. La resolución espacial de GRACE (~300 km) solo cubre el 10% de cuencas fluviales significativas del mundo — ¿qué sesgo introduce esto en toda la literatura de atribución hasta que NGGM/MAGIC (2032) mejore la cobertura al 80%?
11. El problema de atribución de fuente (manto vs. hielo vs. agua subterránea vs. embalses) sigue siendo matemáticamente mal condicionado — ¿qué tan generalizable es la solución de Atacama (EOF+ML) a regiones sin la misma densidad de datos de calibración?
12. La cobertura de pozos de monitoreo in situ es fuerte en EE.UU./India/China y casi inexistente en África y gran parte de Suramérica — ¿cuánto sesga esto las cifras globales agregadas de depleción de acuíferos?
13. No existe un sistema operativo de alerta temprana en tiempo real que hubiera podido anticipar Brumadinho (la señal de 30 cm de subsidencia existía 12 meses antes) — ¿cuántos otros diques de relaves activos en el mundo muestran hoy una señal similar sin que nadie la esté monitoreando operativamente?
14. Ninguna proyección publicada de deriva polar o LOD va más allá de 2050 — toda proyección a 2100 (incluida la de este repositorio, `09-proyeccion-2100.md` §2-3) es necesariamente extrapolación razonada, no dato validado.

## Cómo usar esta lista

Cada pregunta es candidata a convertirse en un issue de investigación individual en este repositorio (ver milestones de GitHub). Las preguntas 2, 6 y 7 (Colombia/Bolivia/Perú) son las de mayor prioridad porque replican una metodología ya validada (Atacama) a sitios sin ningún estudio geodésico previo — el menor costo de entrada para un resultado publicable.
