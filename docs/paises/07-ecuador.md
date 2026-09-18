# Ecuador — glaciares en colapso, mismo vacío de instrumentación geodésica

## 1. Retroceso glaciar — el más documentado en tasa, pero sin vínculo geodésico

- Ecuador ha perdido **32.6%** de su superficie glaciar total, con retroceso documentado desde mediados del siglo XX y una intensificación marcada desde 1976.
- **Cotopaxi**: de 1 472 ha (1985) a 672 ha (2024) — pérdida del **54.4%**.
- **Antisana**: de 2 075 ha (1985) a 1 185 ha (2024) — pérdida del 42.9%.
- **Chimborazo** (el nevado más alto del país): pérdida del **39.5% en un solo año** reciente — la tasa anual más extrema documentada en este repositorio para cualquier glaciar suramericano.
- Efecto regional interesante: los glaciares de la Cordillera Oriental (Cayambe, Antisana) pierden menos (~30%) que los de la Occidental porque la humedad amazónica que condensa sobre ellos actúa como factor moderador — un acoplamiento clima-Amazonía-criósfera documentado por Ecociencia.
- Proyección citada por la comunidad científica ecuatoriana: **desaparición total de los glaciares del país hacia 2050**.

Fuentes:
- [Ecuador pierde sus glaciares: una recuperación aparente oculta una tendencia crítica — ECOCIENCIA](https://ecociencia.org/ecuador-pierde-sus-glaciares-una-recuperacion-aparente-oculta-una-tendencia-critica/)
- [Deshielo de glaciares de Ecuador avanza y llega a "puntos críticos" — Primicias](https://www.primicias.ec/ciencia-tecnologia/deshielo-glaciares-ecuador-antisana-cotopaxi-nieve-informe-ecociencia-118723/)
- [Ecuador ha perdido más de la mitad de su cobertura glaciar — Fundación Glaciares Chilenos](https://www.glaciareschilenos.org/notas/ecuador-ha-perdido-mas-de-la-mitad-de-su-cobertura-glaciar/)

**Brecha idéntica a la de Colombia** (`01-colombia.md` §11): existe excelente caracterización de área glaciar (Ecociencia, IRD) pero **ningún estudio encontrado que conecte esta pérdida con GRACE o con la cadena EOP**.

### Aplicación de la fórmula de excitación EOP (metodología en `00-marco-teorico.md` §6)

Usando el volumen de hielo combinado Ecuador+Colombia (4.17 km³, ver `01-colombia.md` §11.1) menos el volumen colombiano (1.68 km³), el volumen ecuatoriano estimado es **~2.49 km³** — ~1.5 veces el de Colombia, pese a tener ~2.5 veces más área (glaciares ecuatorianos en promedio más delgados). Aplicando la misma tasa de pérdida de masa (0.6-1.2 m eq. agua/año) sobre el área citada (76.8 km², inventario RGI, más antiguo que el dato IDEAM 2024 usado para Colombia — se usa como orden de magnitud, no como cifra actualizada):

```
ΔM = 76.8×10⁶ m² × (0.6 a 1.2 m/año) × 1000 kg/m³ = 4.61×10¹⁰ a 9.22×10¹⁰ kg/año
φ ≈ 0.3-0.7°S (Cotopaxi/Antisana/Cayambe están prácticamente sobre el ecuador)
cos²(0.5°) ≈ 0.99999  →  factor ≈ −0.3333 (el valor máximo teórico posible, el ecuador exacto)
ΔLOD ≈ −0.62 a −1.24 nanosegundos/año
```

**Resultado**: Ecuador resulta ser el caso con **mayor apalancamiento posible por unidad de masa de todo el repositorio para LOD** — sus volcanes-nevados están prácticamente sobre el ecuador geográfico, el punto de eficiencia física máxima de la fórmula (factor −1/3 exacto). Con esto, el efecto calculado (−0.62 a −1.24 ns/año) **supera al de Colombia y se acerca al de la Amazonía en orden de magnitud relativo** (aunque la Amazonía sigue siendo ~200-300 veces mayor en términos absolutos por su volumen muchísimo más grande). Sigue estando 2-3 órdenes de magnitud por debajo de Tres Gargantas — mismo veredicto de indetectabilidad, pero Ecuador es, de todos los casos de hielo/agua de este repositorio, el que más cerca está de la latitud óptima.

Candidato directo para una Fase 3 de este repositorio: repetir la extracción real de GRACE (como se hizo para Colombia en `01-colombia.md` §11.2) sobre los macizos ecuatorianos, y actualizar el área con un inventario más reciente que el RGI usado aquí.

## 2. Minería y volcanismo — riesgo geodésico no explorado en esta fase

Ecuador combina dos fuentes de deformación de la corteza que en otros países de este repositorio aparecen por separado: minería (formal e ilegal) y vulcanismo activo (Cotopaxi, Tungurahua, Reventador, Sangay). Esta investigación no alcanzó a documentar en esta fase, con la misma profundidad que Colombia o Venezuela, la minería aurífera amazónica ecuatoriana ni la instrumentación InSAR de sus volcanes — se deja explícitamente como pendiente en vez de forzar una cifra sin verificar.

## 3. Síntesis de brechas — Ecuador

1. Sin estudio publicado que conecte el retroceso glaciar (32.6% nacional, hasta 54% en Cotopaxi) con GRACE o con la cadena EOP.
2. Sin aplicación en este repositorio de la fórmula de excitación de `00-marco-teorico.md` §6 al caso ecuatoriano — pendiente para la siguiente iteración.
3. Minería aurífera amazónica y monitoreo InSAR volcánico: sin investigar todavía en este repositorio.
