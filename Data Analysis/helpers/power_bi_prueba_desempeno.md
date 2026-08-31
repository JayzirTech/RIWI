# Guía Definitiva de Power BI — Prueba de Desempeño de Análisis de Datos

> Pensada para usarse junto con `pandas_cheatsheet_etl.md`: Pandas/Power Query preparan
> los datos → el modelo dimensional los estructura → DAX los mide → Power BI los comunica.

---

## 1. Flujo mental para resolver la prueba

No empieces haciendo gráficos. Sigue este orden:

```
IMPORTAR
   ↓
ENTENDER LOS DATOS
   ↓
LIMPIAR
   ↓
DEFINIR GRANULARIDAD
   ↓
MODELAR (dimensiones + hechos)
   ↓
CREAR RELACIONES
   ↓
DESACTIVAR AUTO DATE/TIME Y CREAR TABLA CALENDARIO
   ↓
CREAR MEDIDAS DAX
   ↓
VALIDAR RESULTADOS
   ↓
CREAR KPIs
   ↓
CREAR VISUALIZACIONES
   ↓
AGREGAR FILTROS (slicers)
   ↓
FORMATEAR
   ↓
VALIDAR TODO OTRA VEZ
```

---

## 2. Diagnóstico inicial de los datos

Antes de construir nada, respóndete:

- ¿Qué representa cada fila?
- ¿Cuál es la granularidad?
- ¿Cuál es la llave primaria?
- ¿Hay duplicados?
- ¿Hay valores nulos?
- ¿Qué columnas son fechas / numéricas / categóricas?
- ¿Hay valores inconsistentes o imposibles (edades negativas, categorías mal escritas)?
- ¿Hay varias tablas? ¿Cómo se relacionan entre sí?

---

## 3. Granularidad

Granularidad = **qué representa exactamente una fila**.

```text
venta_id | producto_id | cantidad | precio
---------|-------------|----------|-------
1001     | A           | 2        | 100
1001     | B           | 3        | 50
```

Aquí hay **2 filas**, **1 venta**, **2 líneas de producto**. Si no identificas esto bien,
vas a calcular mal: ventas totales, número de transacciones, promedios, cantidades y
utilidades. Es el error de fondo que provoca casi todos los números "raros" en un
dashboard.

---

## 4. Modelo estrella (star schema)

```
                    DimCliente
                        |
DimProducto ---- FactVentas ---- DimFecha
                        |
                    DimRegion
```

**Tabla de hechos** — las transacciones, solo llaves + métricas:

```text
FactVentas
-----------
venta_id
fecha_id
cliente_id
producto_id
region_id
cantidad
ventas
costo
```

**Dimensiones** — información descriptiva, una fila por entidad real:

```text
DimCliente          DimProducto         DimFecha
----------          -----------         --------
cliente_id          producto_id         fecha
nombre               producto            año
segmento             categoria           mes
ciudad               marca               trimestre
                                          día
```

### Regla de oro

```
HECHOS      = números que quieres analizar (ventas, costo, cantidad)
DIMENSIONES = por qué / por quién / cuándo / dónde analizas esos números
```

> Si vienes de pandas: esto es exactamente lo que armamos en la sección de
> `dim_cliente` / `dim_producto` / `fact_ventas` del cheat sheet de ETL, solo que aquí
> ya vive dentro del modelo de Power BI en vez de en Postgres.

---

## 5. Relaciones y cardinalidad

```
DimCliente[cliente_id]   1 ---- * FactVentas[cliente_id]
DimProducto[producto_id] 1 ---- * FactVentas[producto_id]
DimFecha[fecha]          1 ---- * FactVentas[fecha]
```

Cardinalidades que debes reconocer: `1:1`, `1:*`, `*:1`, `*:*`. En un modelo estrella,
lo normal es **Dimensión (1) → Fact (*)**: un cliente tiene muchas ventas, pero cada
venta pertenece a un solo cliente.

**Evita las relaciones muchos-a-muchos** (`* ---- *`) salvo que sea estrictamente
necesario: generan ambigüedad, resultados incorrectos y filtros inesperados.

### Dirección del filtro (lo que suele faltar en estas guías)

Por defecto, cada relación debe filtrar en **una sola dirección**: de la dimensión
hacia la tabla de hechos. Si activas "ambas direcciones" (bidireccional) sin necesitarlo,
es una causa muy común — junto con los duplicados — de que las medidas se dupliquen o
se comporten de forma ambigua. Solo actívala cuando el ejercicio explícitamente lo pida
(por ejemplo, modelos con más de una tabla de hechos que comparten dimensiones).

---

## 6. Power Query — preparación de datos

Operaciones más usadas:

- Remove Rows / Remove Duplicates
- Replace Values
- Split Column / Merge Queries / Append Queries
- Change Type
- Fill Down / Fill Up
- Group By
- Pivot Column / Unpivot Column
- Add Custom Column / Conditional Column

### Equivalencias Power Query ↔ Pandas

| Power Query          | Pandas                          |
|-----------------------|----------------------------------|
| Remove Duplicates     | `drop_duplicates()`             |
| Remove Rows            | `drop()` / filtros               |
| Replace Values         | `replace()`                      |
| Change Type            | `astype()`                       |
| Merge Queries           | `pd.merge()`                     |
| Append Queries          | `pd.concat()`                    |
| Group By                | `groupby()`                      |
| Pivot Column             | `pivot()` / `pivot_table()`     |
| Unpivot Column           | `melt()`                         |
| Conditional Column        | `np.where()` / `np.select()`   |
| Transform Date             | `.dt`                          |
| Fill Down                   | `ffill()`                     |
| Fill Up                      | `bfill()`                    |

---

## 7. Tabla calendario

### ⚠️ Paso que casi siempre se olvida: desactivar Auto date/time

Antes de crear tu propia tabla calendario, ve a **File → Options and settings → Options
→ Data Load** y desactiva **"Auto date/time"** (tanto en el nivel global como en el del
archivo actual). Si no lo haces, Power BI crea jerarquías de fecha ocultas automáticas
por cada columna de fecha, que compiten con tu tabla calendario y pueden hacer que
`SAMEPERIODLASTYEAR` y otras funciones de time intelligence den resultados inconsistentes.

### Crear la tabla

```dax
Calendario =
ADDCOLUMNS(
    CALENDAR(
        MIN(FactVentas[fecha]),
        MAX(FactVentas[fecha])
    ),
    "Año", YEAR([Date]),
    "Mes", MONTH([Date]),
    "NombreMes", FORMAT([Date], "MMMM"),
    "Trimestre", "Q" & FORMAT([Date], "Q"),
    "Dia", DAY([Date])
)
```

### Orden correcto de los meses

Power BI puede ordenar "Abril, Agosto, Diciembre, Enero..." alfabéticamente en vez de
cronológicamente. Solución:

```dax
MesNumero = MONTH(Calendario[Date])
```

Y en la columna `NombreMes`: clic derecho → **Sort by column** → `MesNumero`.

### Marcar como tabla de fechas

Selecciona la tabla `Calendario` → pestaña **Table tools** → **Mark as date table** →
elige la columna `Date`. Esto es obligatorio para que funcionen correctamente las
funciones de time intelligence.

---

## 8. Medidas DAX fundamentales

```dax
Ventas =
SUM(FactVentas[ventas])

Costos =
SUM(FactVentas[costo])

Utilidad =
[Ventas] - [Costos]

Margen % =
DIVIDE([Utilidad], [Ventas], 0)

Cantidad =
SUM(FactVentas[cantidad])

Clientes =
DISTINCTCOUNT(FactVentas[cliente_id])

Transacciones =
DISTINCTCOUNT(FactVentas[venta_id])
```

---

## 9. SUM vs. COUNT vs. DISTINCTCOUNT

```text
venta_id
--------
1001
1001
1001
1002
1002
1003
```

- `COUNT(FactVentas[venta_id])` → **6** (registros no nulos)
- `DISTINCTCOUNT(FactVentas[venta_id])` → **3** (valores únicos)

Confundir estas dos funciones es de los errores más comunes al calcular "número de
transacciones" o "número de clientes".

---

## 10. SUMX — cálculo fila por fila y luego suma

```dax
Ventas =
SUMX(
    FactVentas,
    FactVentas[cantidad] * FactVentas[precio]
)

CostoTotal =
SUMX(
    FactVentas,
    FactVentas[cantidad] * FactVentas[costo_unitario]
)

Utilidad =
[Ventas] - [CostoTotal]
```

Usa `SUMX` cuando el cálculo depende de multiplicar o combinar varias columnas **por
fila** antes de sumar — no puedes hacerlo con un `SUM` simple.

---

## 11. Columna calculada vs. medida

**Columna calculada** — se calcula fila por fila y queda fija en la tabla:

```dax
TotalFila = FactVentas[cantidad] * FactVentas[precio]
```

**Medida** — se calcula dinámicamente según el contexto de filtro del reporte:

```dax
Ventas = SUM(FactVentas[TotalFila])
```

Si filtras por `Ciudad = Bogotá`, la medida cambia automáticamente; la columna
calculada no.

### Regla práctica

- KPIs y métricas del dashboard → **medidas**
- Valores que deben existir fila por fila (para usarlos en otras columnas o exportar
  detalle) → **columna calculada**

---

## 12. CALCULATE — la función más importante de DAX

```dax
Ventas Bogotá =
CALCULATE(
    [Ventas],
    DimCliente[ciudad] = "Bogotá"
)

Ventas Año 2026 =
CALCULATE(
    [Ventas],
    Calendario[Año] = 2026
)
```

`CALCULATE` modifica el contexto de filtro en el que se evalúa una medida. Es la base
de casi todo lo avanzado en DAX.

### ALL() — quitar filtros para calcular un total de referencia

```dax
% del Total =
DIVIDE(
    [Ventas],
    CALCULATE([Ventas], ALL(DimProducto)),
    0
)
```

Esto calcula qué porcentaje representan las ventas del producto filtrado sobre el
total de **todos** los productos, ignorando el filtro de producto activo. Es el patrón
típico para "% del total" en una tabla o tarjeta.

---

## 13. Time intelligence

```dax
Ventas Año Anterior =
CALCULATE(
    [Ventas],
    SAMEPERIODLASTYEAR(Calendario[Date])
)

Crecimiento % =
DIVIDE(
    [Ventas] - [Ventas Año Anterior],
    [Ventas Año Anterior],
    0
)
```

Formatea `Crecimiento %` como **Percentage** en el panel de propiedades de la medida.

Estas funciones **solo funcionan bien** si ya marcaste `Calendario` como tabla de
fechas (paso 7) y desactivaste Auto date/time.

---

## 14. Otras medidas útiles

```dax
Ticket Promedio =
DIVIDE([Ventas], [Transacciones], 0)

Ventas por Cliente =
DIVIDE([Ventas], [Clientes], 0)

Unidades por Transacción =
DIVIDE([Cantidad], [Transacciones], 0)
```

---

## 15. Top N — cuidado con la diferencia entre tabla y medida

```dax
Top Productos =
TOPN(
    10,
    VALUES(DimProducto[producto]),
    [Ventas],
    DESC
)
```

Esta expresión con `TOPN` produce una **tabla**, no una medida directa que puedas poner
en una tarjeta. Se usa dentro de otra medida (envuelta en `SUMX`/`CALCULATE`) o como
tabla calculada. Para un ranking dentro de un visual concreto (barras, tabla), lo más
simple y lo que normalmente se espera en el examen es usar el **filtro visual "Top N"**
del panel de filtros, no escribir DAX.

---

## 16. KPIs recomendados para la página principal

```text
┌────────────┬────────────┬────────────┬────────────┐
│ Ventas     │ Utilidad   │ Margen %   │ Clientes   │
│ $XXX       │ $XXX       │ XX%        │ XXX        │
└────────────┴────────────┴────────────┴────────────┘
```

Con las medidas: `Ventas`, `Utilidad`, `Margen %`, `Clientes` (secciones 8 y 12).

---

## 17. Visualizaciones recomendadas

```text
KPI  → Ventas
KPI  → Utilidad
KPI  → Margen
KPI  → Clientes

Gráfico de líneas   → Ventas por mes
Gráfico de barras   → Ventas por categoría
Gráfico de barras   → Ventas por región
Tabla                → Detalle de productos/clientes
```

**No sobrecargues el dashboard.** Evita 15 gráficos, 8 colores, 10 filtros, varios
mapas y donuts a la vez. El objetivo no es demostrar cuántos visuales sabes crear —
es **contar una historia con los datos**, con pocos elementos bien organizados.

### Estructura recomendada — página 1 (resumen ejecutivo)

```text
┌──────────────────────────────────────────────┐
│              DASHBOARD DE VENTAS              │
├───────────┬───────────┬───────────┬──────────┤
│ Ventas    │ Utilidad  │ Margen    │ Clientes │
├───────────┴───────────┴───────────┴──────────┤
│              Ventas por mes (línea)           │
├──────────────────────┬───────────────────────┤
│ Ventas por categoría  │ Ventas por región    │
├──────────────────────┴───────────────────────┤
│                   Detalle (tabla)             │
└──────────────────────────────────────────────┘
```

### Página 2 (si sobra tiempo) — análisis detallado

Por producto, cliente, categoría, región, segmento o canal, con ranking, ventas,
utilidad, margen, cantidad y ticket promedio.

---

## 18. Slicers / filtros

Recomendados: Año, Mes, Región, Categoría. Según los datos, también: Cliente, Producto,
Segmento, Canal, Marca. No agregues un filtro solo porque puedes — pregúntate siempre
**¿este filtro realmente ayuda al usuario a explorar los datos?**

---

## 19. Interacciones entre visuales

Verifica que al seleccionar, por ejemplo, `Categoría = Electrónica`, cambien
correctamente: Ventas, Utilidad, Clientes, Ventas por región, Ventas por mes. Si algo
no se filtra, revisa en este orden: relaciones → interacciones del visual → filtros de
página/reporte → modelo (dirección de filtro, sección 5).

---

## 20. Drill-down, drill-through y tooltips

**Drill-down** (jerarquía de fecha): `Año → Trimestre → Mes → Día`.

**Drill-through** (página de detalle al hacer clic en un elemento, por ejemplo un
cliente): útil pero es un "plus" — el modelo, las medidas y la validación tienen
prioridad si el tiempo es limitado.

**Tooltips** para mostrar información adicional sin saturar el gráfico principal
(ej. al pasar el mouse sobre un producto: ventas, utilidad, margen, unidades).

---

## 21. Formato

- Números grandes: `$123.5M` en vez de `123456789.32`
- Cantidades: `1,245`
- Porcentajes: `18.4%`
- Pocos colores, con significado consistente: azul = ventas, verde = utilidad positiva,
  rojo = pérdida/caída, gris = información secundaria
- Formato condicional en tablas (verde/rojo según signo) o barras de datos para
  facilitar la lectura rápida

---

## 22. Validación — la parte que más diferencia a quien aprueba

```text
VALIDAR
   ↓
¿Las ventas coinciden con el total original?
   ↓
¿Los clientes coinciden?
   ↓
¿Las transacciones coinciden?
   ↓
¿Los filtros funcionan?
   ↓
¿Los períodos funcionan?
   ↓
¿Las relaciones funcionan?
```

### Comparación directa contra pandas (así se valida en la práctica)

| Verificación   | Pandas                        | Power BI                                    |
|-----------------|--------------------------------|-----------------------------------------------|
| Total de ventas | `df["ventas"].sum()`          | `Ventas = SUM(FactVentas[ventas])`            |
| Clientes únicos | `df["cliente_id"].nunique()`  | `Clientes = DISTINCTCOUNT(FactVentas[cliente_id])` |
| Transacciones    | `df["venta_id"].nunique()`   | `Transacciones = DISTINCTCOUNT(FactVentas[venta_id])` |

### Problema típico: relación mal hecha duplica filas

```text
Original:              Después de una relación incorrecta:
cliente_id | ventas     cliente_id | ventas
1          | 100        1          | 100
2          | 200        1          | 100   ← duplicado
Total: 300              2          | 200
                         Total: 400  ← INCORRECTO
```

Esto ocurre por combinación de: relación mal definida (dirección o cardinalidad
incorrecta) + duplicados en la dimensión + granularidad mal entendida. **Nunca confíes
ciegamente en el número que muestra el dashboard** — siempre compáralo contra un
`.sum()` o `.nunique()` en pandas antes de entregar.

### Checklist de relaciones

- ¿La llave de la dimensión es realmente única? (`dim["llave"].is_unique` en pandas)
- ¿La dimensión está en el lado 1 y la tabla de hechos en el lado *?
- ¿La relación está activa?
- ¿El filtro viaja en la dirección correcta (sección 5)?
- ¿Existe otra ruta de filtrado que genere ambigüedad?

---

## 23. Calidad de datos — revisar antes de entregar

Duplicados, nulos, valores negativos, fechas inválidas, IDs duplicados, categorías
inconsistentes, tipos de datos incorrectos, valores extremos.

**Ejemplos de problemas típicos:**

```text
Edad = -5           → imposible
Ventas = -500000    → puede ser válido (devolución), pero debes poder explicarlo
Bogotá / bogota / BOGOTA / Bogota → misma categoría, mal normalizada
```

**Normalización de texto en Power Query:** `Trim` + `Clean` + `Replace Values` → dejar
una sola forma canónica (`Bogotá`).

---

## 24. Prioridad de estudio

### 🔴 Prioridad 1 — imprescindible
Importar datos, Power Query, tipos de datos, eliminar duplicados, nulos, relaciones,
cardinalidad 1:*, modelo estrella, medidas (`SUM`, `SUMX`, `COUNT`, `DISTINCTCOUNT`,
`DIVIDE`, `CALCULATE`), slicers, KPIs, gráficos básicos, formato.

### 🟠 Prioridad 2 — muy recomendable
Tabla calendario (+ desactivar Auto date/time), `SAMEPERIODLASTYEAR`, crecimiento %,
ranking / filtro Top N, `FILTER`, `ALL`, drill-down, tooltips, formato condicional.

### 🟢 Prioridad 3 — si sobra tiempo
Drill-through, bookmarks, botones, páginas de tooltip, navegación avanzada, DAX
complejo, optimización avanzada.

### Funciones DAX por prioridad

```text
🔴 SUM · SUMX · COUNT · DISTINCTCOUNT · DIVIDE · CALCULATE
🟠 FILTER · ALL · VALUES · SAMEPERIODLASTYEAR · TOPN
🟢 RANKX · DATEADD · DATESYTD · TOTALYTD
```

---

## 25. Checklist final antes de entregar

**Datos**
- [ ] Revisé tipos de datos, nulos, duplicados, valores extremos, categorías
- [ ] Entendí la granularidad

**Modelo**
- [ ] Identifiqué la tabla de hechos y las dimensiones
- [ ] Revisé llaves, relaciones y cardinalidad
- [ ] Evité relaciones ambiguas / bidireccionales innecesarias
- [ ] Tengo tabla calendario marcada como tabla de fechas, con Auto date/time desactivado

**DAX**
- [ ] Ventas, Costos, Utilidad, Margen %, Clientes, Transacciones, Cantidad, Ticket promedio

**Dashboard**
- [ ] KPIs, tendencia temporal, categorías, regiones, tabla de detalle, slicers, formato,
      colores consistentes

**Validación**
- [ ] Los totales coinciden con los datos originales (comparado contra pandas)
- [ ] Los filtros, fechas y relaciones funcionan
- [ ] No hay números duplicados ni visuales vacíos inesperados

---

## 26. Piensa en preguntas de negocio, no en gráficos

```text
¿Cuánto vendimos?                → Ventas
¿Cuánto ganamos?                 → Utilidad
¿Qué tan rentables somos?        → Margen %
¿Dónde vendemos más?             → Región / Ciudad
¿Qué productos venden más?       → Producto / Categoría
¿Cómo evolucionan las ventas?    → Fecha / Mes / Año
¿Estamos creciendo?              → Crecimiento %
¿Quiénes son nuestros mejores clientes? → Ranking / Ventas por cliente
```

### Concepto central

```
DATOS CRUDOS → CALIDAD DE DATOS → MODELO → MÉTRICAS → ANÁLISIS → VISUALIZACIÓN → DECISIÓN
```

Un buen dashboard no es el que tiene más gráficos — es el que permite responder rápido:
¿qué pasó?, ¿por qué pasó?, ¿dónde pasó?, ¿quién lo genera?, ¿cómo evoluciona?, ¿qué
debería investigar?

¡Éxitos mañana!
