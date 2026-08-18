# Ejercicio 5 — Logística (Negocio: TiendaMax, Retail/Electrónica)

**Archivo:** `logistica_desnormalizado.csv` (requiere también `ventas_desnormalizado.csv` del Ejercicio 1 para la pregunta 3)

**Contexto:** Exportación del sistema de logística de TiendaMax. Cada fila es un envío, con datos
del transportista y del almacén de origen repetidos. La columna `estado_envio` tiene mayúsculas y
minúsculas mezcladas, hay nulos en costo de envío, una fila duplicada, y una llave foránea
(`id_venta_relacionada`) que conecta con el dataset de ventas del Ejercicio 1.

## Flujo de trabajo
1. Leer el CSV con pandas.
2. Explorar y limpiar: nulos, duplicados, normalización de texto en `estado_envio`, formatos de fecha, tipos de datos.
3. **Normalizar** en tablas relacionadas (3FN): `transportistas`, `almacenes`, `envios` (FK a transportista, almacén y a `ventas` del ejercicio 1).
4. Conectarse a PostgreSQL y cargar las tablas normalizadas:
```python
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://usuario:password@localhost:5432/tiendamax")
transportistas.to_sql("transportistas", engine, if_exists="replace", index=False)
```
5. Responder las preguntas con pandas o `pd.read_sql()`.
6. Generar el gráfico final.

## Preguntas
1. Normaliza `estado_envio` (mayúsculas/minúsculas mezcladas) y calcula el porcentaje de envíos "Entregado", "Retrasado" y "Cancelado" por transportista.
2. ¿Qué transportista tiene el mejor balance entre costo promedio de envío y calificación?
3. Une (`merge`) este dataset con `ventas_desnormalizado.csv` usando `id_venta_relacionada` / `id_venta`. ¿Qué sucursal de origen de venta genera más envíos retrasados?
4. ¿Existe relación entre `peso_kg` y `costo_envio_mxn`? Calcula la correlación después de eliminar nulos y el duplicado.
5. ¿Cuál es el tiempo estimado de entrega promedio por almacén de origen, y cuál almacén debería priorizarse para mejorar tiempos?

## Gráfico final
**Usar matplotlib** (`matplotlib.pyplot`) con `plt.subplots(2, 2, figsize=(14, 10))` para armar un
dashboard de 4 paneles: % de estados de envío por transportista, dispersión peso vs costo de envío,
envíos retrasados por sucursal de origen (tras el merge), y tiempo estimado de entrega por almacén.

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes[0,0].bar(...)     # % estados de envío por transportista
axes[0,1].scatter(...) # peso vs costo de envío
axes[1,0].bar(...)     # envíos retrasados por sucursal de origen
axes[1,1].bar(...)     # tiempo estimado de entrega por almacén
plt.tight_layout()
plt.savefig("ej5_dashboard.png", dpi=150)
plt.show()
```

## Checklist de dificultad
- [ ] Normalización de texto en `estado_envio`.
- [ ] Manejo de fechas (`fecha_envio` en formato `%d-%m-%Y`).
- [ ] `merge` entre dos datasets distintos (llave foránea cruzada).
- [ ] Manejo de nulos en `costo_envio_mxn`.
- [ ] Eliminación de duplicados exactos.
- [ ] Diseño de esquema normalizado (3FN) antes de cargar a PostgreSQL.
- [ ] Carga con `to_sql()` y validación con `pd.read_sql()`.
- [ ] Gráfico compuesto que sintetice el análisis.
