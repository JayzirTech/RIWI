# Immportaciones
import os
import pandas as pd
from sql import procesar_entidades_envios

os.system('cls')

df = pd.read_csv('logistica_desnormalizado.csv')

# Recorre todos los datos columna por columna
for col in df.columns:
    unicos_crudos = df[col].nunique()   # Conteo de valores únicos crudos (sin limpiar)
    unicos_limpios = df[col].astype(str).str.strip().str.lower().nunique()  # Conteo de valores únicos limpios
    
    # Si al limpiar hay MENOS valores únicos, ¡hay inconsistencias!
    if unicos_limpios < unicos_crudos:
        print(f'⚠️  ¡Alerta! Hay valores repetidos escritos de forma diferente.')
        print(f'Columna: {col}')
        print(f'Variaciones: {df[col].unique().tolist()}\n')

        # Limpio los datos en la columna donde se encuentran las inconsistencias
        df[col] = df[col].str.strip().str.capitalize()
        print(f'Valores limpiados:\n{df[col].unique().tolist()}\n')   # Verifico que se hayan limpiado los datos

print(f'------------------------------------------------------------\n')

# Convierto los datos de texto a numéricos
cols_numericas = ['calificacion_transportista', 'dias_estimados_entrega', 'costo_envio_mxn', 'peso_kg']

# Aplico to_numeric con errors='coerce' a todas las columnas seleccionadas
df[cols_numericas] = df[cols_numericas].apply(pd.to_numeric, errors='coerce')

# Aplico to_datetime a la columna 'fecha_entrega' con errors='coerce'
df['fecha_envio'] = pd.to_datetime(df['fecha_envio'], dayfirst=True, errors='coerce')

# Verifico si hay datos nulos
if df.isnull().sum().sum() > 0:
    print(f'⚠️  ¡Alerta! Hay datos nulos.')

    # Muestro las filas con valores nulos    
    print(f'{df[df.isnull().any(axis=1)]}\n')

    # Reemplazo los valores nulos por '0'
    df = df.fillna(0)

    print(f'Valores nulos reemplazados por "No Especificado":\n')

else:
    print(f'No hay datos nulos.\n')

print(f'------------------------------------------------------------\n')

# Verifico si hay filas duplicadas
if df.duplicated().sum() > 0:
    print(f'⚠️  ¡Alerta! Hay filas duplicadas.')

    # Muestro las filas duplicadas
    print(f'{df[df.duplicated()]}\n')

    # Elimino las filas duplicadas
    df = df.drop_duplicates()

    print(f'Filas duplicadas eliminadas.\n')

else:
    print(f'No hay filas duplicadas.\n')

print(f'------------------------------------------------------------\n')

procesar_entidades_envios(df)