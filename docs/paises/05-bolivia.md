# Bolivia — el mayor depósito de litio del mundo, sin monitoreo geodésico cuantitativo publicado

## Salar de Uyuni

- Contiene el mayor depósito de litio del mundo (~23 millones de toneladas métricas estimadas).
- La extracción de salmuera usa hasta **500 000 litros de agua por tonelada de litio producida**, con impacto directo en agricultura y ecosistemas locales.
- Estudio de análisis químico de aguas residuales (*Environmental Science & Technology Letters*, 2025): en salmuera natural el arsénico se midió entre 1-9 ppm con acidez casi neutra; en la salmuera de las pozas de evaporación finales, la acidez sube y el arsénico alcanza ~50 ppm — **~1 400 veces el nivel ecológicamente aceptable según la EPA de EE.UU.**
- La literatura señala explícitamente que la experiencia de Atacama (Chile) — descenso del nivel freático y subsidencia del terreno — es el precedente de riesgo que Bolivia busca evitar, sin que exista todavía evidencia de que se esté replicando o no en Uyuni.

Fuentes:
- [Bolivia: the environmental impact of lithium extraction in the Uyuni Salt Flat](https://noticiasambientales.com/environment-en/bolivia-the-environmental-impact-of-lithium-extraction-in-the-uyuni-salt-flat/)
- [Examining the potential environmental effects of mining the world's largest lithium deposit — ScienceDaily 2025](https://www.sciencedaily.com/releases/2025/02/250210183627.htm)
- [Wastewater analysis at Bolivian lithium deposit — Envirotec](https://envirotecmagazine.com/2025/02/18/wastewater-analysis-at-bolivian-lithium-deposit-explores-how-to-avoid-past-environmental-mistakes/)

## Hallazgo explícito: vacío geodésico total

A diferencia de Atacama (Chile), donde existe cuantificación satelital de subsidencia en cm/año, **no se encontró ningún estudio publicado de InSAR, gravimetría o GRACE downscaled aplicado específicamente al Salar de Uyuni**. Toda la literatura encontrada es química/ambiental (contaminación por arsénico, balance hídrico agrícola), no geodésica.

Dado que Uyuni es geológica y operativamente comparable a Atacama (mismo mecanismo de extracción de salmuera por bombeo y evaporación), y que Atacama ya demostró subsidencia medible, **la ausencia de estudio geodésico en Uyuni no significa ausencia de fenómeno — significa ausencia de medición**. Es la segunda oportunidad de investigación más clara de este repositorio, después de Cerro de Pasco (Perú).

## Aplicación de la fórmula de excitación EOP (metodología en `00-marco-teorico.md` §6)

Igual que Atacama, la extracción de salmuera en Uyuni sí cumple la condición física de §6.4 del marco teórico (el agua se pierde por evaporación a la atmósfera global) — a diferencia de la minería de sólidos.

### Dato de entrada (verificado en vivo, 2026-09-18)

Sumando la capacidad de diseño de los proyectos ya contratados (no necesariamente el throughput actual de 2026, ver caveat abajo):
- Planta YLB de Colcha K (15 000 t/año carbonato de litio): hasta 20 millones de m³/año de salmuera a máxima capacidad.
- Proyecto YLB + Uranium One (Rusia, 14 000 t/año, tecnología DLE): ~9 millones de m³/año.
- **Total documentado: ~29 millones de m³/año** (excluye el proyecto chino CBC de 35 000 t/año anunciado en nov-2024, sin cifra de volumen de salmuera publicada).
- Latitud del Salar de Uyuni: φ ≈ 20.3°S.

**Caveat**: estas son capacidades de diseño/contratadas, no necesariamente el volumen real bombeado en 2026 si las plantas no operan a plena capacidad — se usa como cota superior razonable, mismo estándar de honestidad que en los demás casos de este repositorio.

### Cálculo

```
ΔM = 29×10⁶ m³/año × 1200 kg/m³ = 3.48×10¹⁰ kg/año
cos²(20.3°) = 0.8791  →  factor (2/3 − cos²φ) = −0.2124
ΔC ≈ −3.00×10²³ kg·m²
ΔLOD ≈ −0.32 nanosegundos/año
```

### Resultado

Entre el Cerrejón/Bogotá (−0.08 a −0.09 ns/año) y Atacama (−0.48 ns/año) — consistente con que Uyuni tiene menor volumen que Atacama pero una latitud ligeramente más favorable. Para deriva polar, sin(2×20.3°) = 0.651, también favorable pero por debajo de Atacama.

**Conclusión**: mismo resultado cualitativo que todos los demás casos — indetectable, 2-3 órdenes de magnitud por debajo de Tres Gargantas. La diferencia con Atacama es de grado, no de tipo: si Uyuni alcanza en el futuro los volúmenes de extracción de Atacama (con los tres proyectos operando a plena capacidad, podría acercarse), seguiría sin ser un efecto medible — la barrera no es de escala de proyecto individual sino de orden de magnitud planetario completo.
