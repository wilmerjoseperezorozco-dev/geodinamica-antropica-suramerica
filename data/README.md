# Datos extraídos por este proyecto

Esta carpeta contiene datos **derivados**, extraídos directamente de fuentes primarias abiertas para este repositorio (no son datos originales del repositorio — cada archivo documenta su fuente exacta). Se guardan aquí para que el análisis sea reproducible sin depender de que la herramienta original siga disponible de la misma forma.

## `grace_la_guajira_2002-2026.csv`

- **Fuente**: [GRACE(-FO) Data Analysis Tool](https://grace.jpl.nasa.gov/data-analysis-tool/) de NASA/JPL, dataset `Water Equivalent Thickness – Land (GRACE, GRACE-FO JPL)` (JPL RL06.3M mascon, v04).
- **Método de extracción**: recuadro dibujado manualmente sobre el departamento de La Guajira (12.5156°N a 10.3359°N, -74.0391° a -71.5078°O), operación "Time Series", rango completo disponible (abril 2002 - julio 2026). Extraído en vivo el 2026-09-18 vía la interfaz pública de la herramienta (sin necesidad de registro).
- **Unidades**: anomalía de espesor de agua equivalente en cm, relativa al promedio 2004.0-2009.999 (línea base estándar de GRACE).
- **Nota de calidad**: contiene el vacío de datos conocido entre GRACE y GRACE-FO (última observación 2017-06-11, siguiente 2018-06-16) — esto es una característica real de la misión, no un error de extracción (ver `docs/00-marco-teorico.md` §5 sobre gap-filling).
- **Análisis derivado**: ver `docs/paises/01-colombia.md` §6.5.

## `sirgas_neu_colombia_2004-2026.csv`

- **Fuente**: [SIRGAS Analysis Centre at DGFI-TUM — Station list](https://www.sirgas.org/en/stations/station-list/), archivos NEU públicos en `https://www.sirgas.org/fileadmin/docs/SIRGAS_TS/<CODIGO>.NEU` (sin necesidad de registro ni login).
- **Estaciones incluidas**: EBPT (El Bagre, Bajo Cauca, Antioquia — activa), CASI (Caucasia, Bajo Cauca, Antioquia — activa), TARZ (Tarazá, Bajo Cauca, Antioquia — inactiva desde ~2026), RIOH (Riohacha, La Guajira — **removida**, última observación 2023-01-18). No incluye VALL (Valledupar) por espacio; su serie completa está en la misma URL patrón con código `VALL`.
- **Contenido**: componente vertical (altura/Up) semanal en mm, relativa a la primera época de cada estación. El archivo original de cada estación también incluye componentes Norte/Este y errores formales — no replicados aquí por enfocarnos en la señal de subsidencia/levantamiento.
- **Nota de calidad importante**: se detectó un salto sistemático de +60 a +155 mm en TRES estaciones distintas (EBPT, TARZ, VALL) de forma simultánea entre marzo y mayo de 2023, coincidiendo con múltiples cambios de marco de referencia geodésico en los archivos (IGb14→IGS20→IGb20→IGc20). Esto es casi con certeza un artefacto de reprocesamiento/realización de marco de referencia, **no una deformación real del terreno** — un evento geofísico real no produce el mismo salto simultáneo en estaciones a cientos de km de distancia. Ver análisis en `docs/paises/01-colombia.md` §6.7.
