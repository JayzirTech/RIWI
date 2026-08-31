# Cheat Sheet Definitiva de Pandas para ETL y Análisis de Datos

> Basada en tu versión original, corregida y ampliada con los bloques que suelen faltar
> en pruebas de desempeño de análisis de datos: series de tiempo, pivotes, rendimiento
> y errores comunes.

---

## ⚠️ Corrección importante sobre tu versión original

```python
df.shape()   # ❌ INCORRECTO — .shape es un ATRIBUTO, no un método
df.shape     # ✅ CORRECTO — no lleva paréntesis
```

Tú mismo lo anotaste en el comentario, pero el código de la línea seguía teniendo los
paréntesis. Es un error clásico que en un examen te puede sacar de la prueba porque
lanza `TypeError: 'tuple' object is not callable`.

---

## 1. Creación y carga de datos

```python
import numpy as np
import pandas as pd

# --- Lectura ---
df = pd.read_csv("datos.csv")                          # CSV
df = pd.read_csv("datos.csv", sep=";", encoding="utf-8")# CSV con separador/encoding distinto
df = pd.read_csv("datos.csv", usecols=["col1", "col2"]) # Cargar solo ciertas columnas (ahorra memoria)
df = pd.read_csv("datos.csv", dtype={"id": "str"})      # Forzar tipos al leer
df_excel = pd.read_excel("datos.xlsx", sheet_name="Hoja1")
df_json = pd.read_json("datos.json")
df_dict = pd.DataFrame({"col1": [1, 2], "col2": ["A", "B"]})

# --- Lectura por lotes (archivos muy grandes que no caben en memoria) ---
for chunk in pd.read_csv("datos_grandes.csv", chunksize=100_000):
    procesar(chunk)   # procesas cada trozo y luego concatenas o agregas resultados

# --- Desde/hacia bases de datos ---
import sqlite3
conn = sqlite3.connect("mi_base.db")
df_sql = pd.read_sql("SELECT * FROM ventas", conn)
df.to_sql("ventas", conn, if_exists="replace", index=False)

# --- JSON anidado (muy común en ETL de APIs) ---
df_flat = pd.json_normalize(datos_json, sep="_")  # Aplana diccionarios anidados en columnas

# --- Exportar ---
df.to_csv("salida.csv", index=False)
df.to_parquet("salida.parquet")   # formato columnar, comprimido y rápido de leer
df.to_excel("salida.xlsx", index=False, sheet_name="Resultado")
```

**Tip de examen:** si te dan un archivo grande y te preguntan cómo optimizar la lectura,
la respuesta esperada casi siempre es `usecols`, `dtype` y/o `chunksize`.

---

## 2. Exploración básica de datos

```python
df.head(10)                 # Primeras 10 filas
df.tail(5)                  # Últimas 5 filas
df.sample(5)                # 5 filas aleatorias (útil para verificar sin sesgo de orden)
df.info()                   # Tipos de datos, nulos y uso de memoria
df.describe()               # Estadísticas de columnas numéricas
df.describe(include="all")  # Incluye también columnas categóricas/objeto
df.shape                    # (filas, columnas) — SIN paréntesis
df.columns                  # Nombres de columnas
df.dtypes                   # Tipo de dato por columna
df.memory_usage(deep=True)  # Memoria real usada por columna (clave con strings)
df.nunique()                # Cantidad de valores únicos por columna
df["columna"].unique()      # Valores únicos de una serie
df["columna"].value_counts()                # Conteo de frecuencia
df["columna"].value_counts(normalize=True)  # Como proporción (%) en vez de conteo
df.corr(numeric_only=True)  # Matriz de correlación entre columnas numéricas
```

---

## 3. Selección y filtrado (loc, iloc, query)

```python
df["columna"]                          # Una columna como Serie
df[["col1", "col2"]]                   # Varias columnas como DataFrame
df.loc[0]                              # Fila por etiqueta de índice
df.loc[0:5, ["col1", "col2"]]          # Filas 0-5 y columnas por nombre
df.iloc[0:5, 0:2]                      # Filas y columnas por posición numérica
df[df["edad"] > 18]                    # Filtro simple
df[(df["edad"] > 18) & (df["ciudad"] == "Bogotá")]   # AND lógico (usar &, no "and")
df[(df["edad"] < 18) | (df["vip"] == True)]          # OR lógico (usar |, no "or")
df[df["ciudad"].isin(["Bogotá", "Medellín"])]        # Filtrar por lista de valores
df[~df["ciudad"].isin(["Bogotá"])]                   # Negación (excluir valores)
df[df["edad"].between(18, 30)]                       # Filtrar por rango
df[df.duplicated(subset=["id_cliente"], keep=False)] # Ver todos los duplicados
df.query("edad > 18 and ciudad == 'Bogotá'")         # Alternativa más legible al filtro booleano
```

**Tip de examen:** en pandas los operadores lógicos correctos para filtrar son
`&`, `|`, `~` (no `and`, `or`, `not`), y cada condición va entre paréntesis.

---

## 4. Limpieza de datos (nulos, duplicados, outliers)

```python
df.isnull()                              # Máscara booleana de nulos
df.notnull()                             # Máscara de no-nulos
df.isnull().sum()                        # Total de nulos por columna
df.isnull().mean() * 100                 # % de nulos por columna (muy usado en ETL)
df.dropna()                              # Eliminar filas con cualquier nulo
df.dropna(subset=["col1"])               # Eliminar filas donde col1 sea nulo
df.dropna(axis=1, thresh=len(df) * 0.5)  # Eliminar columnas con más de 50% de nulos
df.fillna(0)                             # Rellenar nulos con 0
df["col1"].fillna(df["col1"].mean())     # Rellenar con la media
df["col1"].fillna(method="ffill")        # Rellenar con el valor anterior (forward fill)
df["col1"].interpolate()                 # Rellenar por interpolación lineal (series numéricas/tiempo)
df.drop_duplicates()                     # Eliminar filas totalmente duplicadas
df.drop_duplicates(subset=["id_cliente"], keep="last")  # Duplicados por columna clave
df["col"].clip(lower=0, upper=100)       # Limitar valores a un rango (tratar outliers)
```

---

## 5. Transformación y modificación de columnas

```python
df["nueva_col"] = df["col1"] + df["col2"]
df.rename(columns={"viejo": "nuevo"})
df.drop(columns=["col_basura"], inplace=True)

# --- Texto (accessor .str) ---
df["texto"] = df["texto"].str.lower()
df["texto"] = df["texto"].str.strip()
df["texto"] = df["texto"].str.replace("a", "e")
df["contiene"] = df["texto"].str.contains("bogota", case=False, na=False)
df["dominio"] = df["email"].str.split("@").str[1]      # Extraer parte de un string
df["codigo"]  = df["texto"].str.extract(r"(\d{4})")    # Extraer con regex

# --- Binning / categorización numérica ---
df["rango_edad"] = pd.cut(df["edad"], bins=[0, 18, 30, 60, 100],
                           labels=["menor", "joven", "adulto", "mayor"])
df["cuartil_monto"] = pd.qcut(df["monto"], q=4, labels=False)  # divide en cuartiles

# --- apply vs. operaciones vectorizadas ---
df["col"].apply(lambda x: x * 2)                    # OK para casos puntuales
df["precio"] * df["cantidad"]                       # ✅ preferido: vectorizado, mucho más rápido
df.apply(lambda row: row["precio"] * row["cantidad"], axis=1)  # más lento, evitar si hay alternativa vectorizada
```

**Tip de examen:** si te piden "optimizar" un `apply(axis=1)`, la respuesta esperada es
reemplazarlo por una operación vectorizada directa sobre las columnas.

---

## 6. Cambio de tipos de datos

```python
df["col"] = df["col"].astype("int64")
df["col"] = df["col"].astype("float")
df["col"] = df["col"].astype("category")     # Reduce memoria en columnas con pocos valores únicos
df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d", errors="coerce")
df["col"] = pd.to_numeric(df["col"], errors="coerce")  # Fuerza numérico, errores -> NaN

# --- Accessor .dt para fechas ---
df["anio"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["dia_semana"] = df["fecha"].dt.day_name()
df["es_fin_de_semana"] = df["fecha"].dt.weekday >= 5
```

---

## 7. Mapeos y reemplazos (clave para dimensiones)

```python
mapeo = {"Activo": 1, "Inactivo": 0}
df["estado_id"] = df["estado"].map(mapeo)         # Mapear diccionario -> columna
df["estado"] = df["estado"].replace({"Activo": "A"})
df["estado"] = df["estado"].where(df["estado"] != "N/A", "Desconocido")  # Reemplazo condicional
df["categoria"] = np.where(df["monto"] > 1000, "Alto", "Bajo")           # if/else vectorizado
```

---

## 8. Agrupaciones y agregaciones (groupby, pivot, crosstab)

```python
df.groupby("categoria")["monto"].sum()
df.groupby("categoria")["monto"].mean()
df.groupby("categoria")["id"].count()
df.groupby("region").agg({"monto": ["sum", "mean"], "id": "count"})
df.groupby("region").agg(
    total_ventas=("monto", "sum"),
    promedio_ventas=("monto", "mean")
).reset_index()

# --- transform: agrega pero devuelve el mismo tamaño del df original (muy usado en ETL) ---
df["promedio_categoria"] = df.groupby("categoria")["monto"].transform("mean")

# --- filter: se queda con grupos completos que cumplen una condición ---
df_filtrado = df.groupby("cliente_id").filter(lambda g: g["monto"].sum() > 1000)

# --- pivot_table: tabla resumen tipo Excel ---
tabla = df.pivot_table(index="region", columns="categoria",
                        values="monto", aggfunc="sum", fill_value=0)

# --- crosstab: conteo cruzado entre dos categorías ---
pd.crosstab(df["region"], df["categoria"])
```

---

## 9. Cruces y uniones de datos (merge, concat, join)

```python
df_merged = pd.merge(df_ventas, df_clientes, on="cliente_id", how="left")
df_merged_multi = pd.merge(df_ventas, df_detalles, on=["order_id", "prod_id"], how="inner")
df_merged_ind = pd.merge(df_a, df_b, on="id", how="outer", indicator=True)  # columna "_merge" indica origen de cada fila

df_concat = pd.concat([df_2025, df_2026], axis=0, ignore_index=True)  # Apilar verticalmente
df_concat_cols = pd.concat([df_parte1, df_parte2], axis=1)            # Unir horizontalmente

df.combine_first(df_respaldo)  # Rellena nulos de df con valores de otro df usando el mismo índice
```

**Tip de examen:** `how` puede ser `"left"`, `"right"`, `"inner"`, `"outer"` — igual que
en SQL. Si preguntan por filas sin coincidencia, se identifican filtrando por nulos
después del merge o usando `indicator=True`.

---

## 10. Ordenamiento, índices y reestructuración (reshape)

```python
df.sort_values(by="fecha", ascending=False)
df.sort_values(by=["pais", "monto"], ascending=[True, False])
df.reset_index(drop=True)
df.set_index("id_cliente")

# --- Reestructuración: ancho <-> largo (muy típico en ETL) ---
df_largo = df.melt(id_vars=["id_cliente"], value_vars=["ene", "feb", "mar"],
                    var_name="mes", value_name="ventas")   # de ancho a largo
df_ancho = df_largo.pivot(index="id_cliente", columns="mes", values="ventas")  # de largo a ancho

df.stack()      # Convierte columnas en niveles de índice (formato largo)
df.unstack()    # Operación inversa

df.explode("lista_col")  # Convierte una columna de listas en varias filas
```

---

## 11. Series de tiempo (frecuente en pruebas de análisis)

```python
df = df.set_index("fecha")
df.resample("M").sum()          # Agregación mensual
df.resample("W").mean()         # Agregación semanal
df["media_movil_7d"] = df["ventas"].rolling(window=7).mean()   # Media móvil
df["acumulado"] = df["ventas"].expanding().sum()                # Acumulado progresivo
df["ventas"].shift(1)           # Valor del período anterior (útil para variación %)
df["variacion_pct"] = df["ventas"].pct_change()                 # % de cambio período a período
```

---

## 12. Funciones personalizadas y encadenamiento (apply, pipe)

```python
df["col"].apply(lambda x: x * 2)
df.apply(lambda row: row["precio"] * row["cantidad"], axis=1)

# pipe: permite encadenar funciones propias manteniendo el código legible
def quitar_nulos(d):
    return d.dropna(subset=["monto"])

def normalizar_texto(d):
    d["ciudad"] = d["ciudad"].str.lower().str.strip()
    return d

df_limpio = (
    df
    .pipe(quitar_nulos)
    .pipe(normalizar_texto)
    .sort_values("fecha")
)
```

---

## 13. Buenas prácticas y errores comunes a evitar

| Error común | Por qué falla / es mal visto | Alternativa correcta |
|---|---|---|
| `df.shape()` | `.shape` es atributo, no método | `df.shape` |
| `df[df["edad"]>18 and df["vip"]==True]` | `and`/`or` no funcionan elemento a elemento en pandas | usar `&`, `\|` con paréntesis en cada condición |
| Modificar un slice sin `.loc` | Dispara `SettingWithCopyWarning` | `df.loc[condición, "columna"] = valor` |
| Usar `apply(axis=1)` para operaciones aritméticas simples | Es mucho más lento que vectorizar | Operar directamente sobre columnas: `df["a"] + df["b"]` |
| Comparar fechas en texto | No ordena ni filtra correctamente | Convertir siempre con `pd.to_datetime` primero |
| No usar `inplace=True` ni reasignar | El cambio no se guarda | `df = df.dropna()` o `df.dropna(inplace=True)` |
| Ignorar `errors="coerce"` en conversiones | El script se rompe ante un dato sucio | Usar `errors="coerce"` y luego revisar los NaN generados |
| Leer un CSV enorme sin `chunksize`/`usecols` | Puede agotar la memoria | Filtrar columnas o leer por lotes |

---

## 14. Normalizar un DataFrame gigante en dimensiones + tabla de hechos (star schema)

Este es el patrón típico cuando tienes **un solo DataFrame "ancho"** (por ejemplo, ventas
con todos los datos del cliente, producto y ciudad repetidos en cada fila) y necesitas
separarlo en **tablas de dimensión** + **una tabla transaccional (fact table)** que solo
tenga las llaves (IDs) para cargarlo a Postgres y consumirlo después desde Power BI.

### Paso 1 — Identificar qué columnas forman cada dimensión

```python
# Ejemplo de df ancho (transaccional sin normalizar)
# columnas: fecha, cliente_id, nombre_cliente, ciudad, producto_id, nombre_producto,
#           categoria, cantidad, precio_unitario

# Agrupa mentalmente las columnas que "viajan juntas":
# - Dimensión cliente:  cliente_id, nombre_cliente, ciudad
# - Dimensión producto:  producto_id, nombre_producto, categoria
# - Tabla de hechos:     fecha, cliente_id, producto_id, cantidad, precio_unitario
```

### Paso 2 — Construir cada dimensión con su llave surrogate (PK)

```python
# --- Dimensión cliente ---
dim_cliente = (
    df[["cliente_id", "nombre_cliente", "ciudad"]]
    .drop_duplicates(subset=["cliente_id"])   # una fila por cliente real
    .reset_index(drop=True)
)
dim_cliente["cliente_key"] = dim_cliente.index + 1   # llave surrogate autoincremental

# --- Dimensión producto ---
dim_producto = (
    df[["producto_id", "nombre_producto", "categoria"]]
    .drop_duplicates(subset=["producto_id"])
    .reset_index(drop=True)
)
dim_producto["producto_key"] = dim_producto.index + 1

# --- Dimensión fecha (muy típica en modelos para Power BI) ---
dim_fecha = pd.DataFrame({"fecha": df["fecha"].drop_duplicates().sort_values().reset_index(drop=True)})
dim_fecha["fecha_key"] = dim_fecha.index + 1
dim_fecha["anio"] = dim_fecha["fecha"].dt.year
dim_fecha["mes"] = dim_fecha["fecha"].dt.month
dim_fecha["dia_semana"] = dim_fecha["fecha"].dt.day_name()
```

> **Atajo con `pd.factorize`:** genera la llave surrogate y el mapeo en un solo paso,
> útil cuando no necesitas conservar otros atributos de la dimensión:
> ```python
> df["cliente_key"], claves_unicas = pd.factorize(df["cliente_id"])
> df["cliente_key"] += 1  # para que empiece en 1 en vez de 0
> ```

### Paso 3 — Construir la tabla de hechos (transaccional) solo con llaves + métricas

```python
fact_ventas = (
    df
    .merge(dim_cliente[["cliente_id", "cliente_key"]], on="cliente_id", how="left")
    .merge(dim_producto[["producto_id", "producto_key"]], on="producto_id", how="left")
    .merge(dim_fecha[["fecha", "fecha_key"]], on="fecha", how="left")
)

fact_ventas = fact_ventas[["fecha_key", "cliente_key", "producto_key", "cantidad", "precio_unitario"]]
fact_ventas["monto_total"] = fact_ventas["cantidad"] * fact_ventas["precio_unitario"]
fact_ventas.insert(0, "venta_id", fact_ventas.index + 1)  # PK propia de la tabla de hechos
```

### Paso 4 — Verificar integridad antes de cargar a Postgres

```python
# No debe haber nulos en las llaves foráneas después del merge (indicaría un ID sin dimensión)
assert fact_ventas[["cliente_key", "producto_key", "fecha_key"]].isnull().sum().sum() == 0

# Confirmar que cada dimensión tiene llaves únicas
assert dim_cliente["cliente_key"].is_unique
assert dim_producto["producto_key"].is_unique
```

### Paso 5 — Cargar a Postgres

```python
from sqlalchemy import create_engine

engine = create_engine("postgresql://usuario:password@localhost:5432/mi_basedatos")

dim_cliente.to_sql("dim_cliente", engine, if_exists="replace", index=False)
dim_producto.to_sql("dim_producto", engine, if_exists="replace", index=False)
dim_fecha.to_sql("dim_fecha", engine, if_exists="replace", index=False)
fact_ventas.to_sql("fact_ventas", engine, if_exists="replace", index=False)
```

En Postgres, después de cargar, defines las llaves primarias/foráneas con SQL
(`ALTER TABLE ... ADD PRIMARY KEY`, `ADD FOREIGN KEY`) si `to_sql` no las crea, y ese
esquema en estrella (una tabla de hechos + varias dimensiones conectadas por llave) es
exactamente lo que Power BI espera para armar el modelo de datos y las relaciones.

**Tip de examen:** si te piden "normalizar", el criterio que evalúan casi siempre es:
① cada dimensión debe tener una fila única por entidad (`drop_duplicates`), ② la tabla
de hechos no debe repetir texto/descripciones, solo llaves y métricas, y ③ después del
`merge` no debe quedar ninguna llave foránea en `NaN`.

---

## 15. Mini-checklist para el día del examen

1. Cargar datos → revisar `.info()`, `.head()`, `.shape`
2. Detectar nulos y duplicados → `.isnull().sum()`, `.duplicated()`
3. Limpiar tipos → `astype`, `to_datetime`, `to_numeric(errors="coerce")`
4. Transformar → `str.*`, `map`, `np.where`, `cut/qcut`
5. Agregar → `groupby`, `pivot_table`, `transform`
6. Cruzar fuentes → `merge` con el `how` correcto
7. Verificar el resultado final → `.shape`, `.info()`, `.sample()`
8. Exportar → `to_csv(index=False)` o `to_parquet`

¡Mucho éxito en tu prueba de mañana!


```sql
-- 1. Llave primaria en cada dimensión
ALTER TABLE dim_cliente
    ADD CONSTRAINT pk_dim_cliente PRIMARY KEY (cliente_key);

ALTER TABLE dim_producto
    ADD CONSTRAINT pk_dim_producto PRIMARY KEY (producto_key);

ALTER TABLE dim_fecha
    ADD CONSTRAINT pk_dim_fecha PRIMARY KEY (fecha_key);

-- 2. Llave primaria en la tabla de hechos
ALTER TABLE fact_ventas
    ADD CONSTRAINT pk_fact_ventas PRIMARY KEY (venta_id);

-- 3. Llaves foráneas: conectan fact_ventas con cada dimensión
ALTER TABLE fact_ventas
    ADD CONSTRAINT fk_fact_cliente
    FOREIGN KEY (cliente_key) REFERENCES dim_cliente (cliente_key);

ALTER TABLE fact_ventas
    ADD CONSTRAINT fk_fact_producto
    FOREIGN KEY (producto_key) REFERENCES dim_producto (producto_key);

ALTER TABLE fact_ventas
    ADD CONSTRAINT fk_fact_fecha
    FOREIGN KEY (fecha_key) REFERENCES dim_fecha (fecha_key);
```