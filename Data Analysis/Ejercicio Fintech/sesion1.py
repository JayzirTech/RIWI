import os
import pandas as pd

# Función para quitar espacios y tildes y hacer todos los textos en minúscula
def minuscula_sin_tildes (dirty_dataframe):

    # Tabla de traducción de caracteres -----------------------------------
    tabla_tildes = str.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU')

    for col in dirty_dataframe.select_dtypes(include='string').columns:
        dirty_dataframe[col] = dirty_dataframe[col].astype(str).str.strip().str.lower()   # Todo minúscula
        dirty_dataframe[col] = dirty_dataframe[col].astype(str).apply(lambda x: x.translate(tabla_tildes))    #Todo sin tilde

    clean_dataframe = dirty_dataframe

    return clean_dataframe

def limpieza_números(any_dataframe):
    # Limpias símbolos ($ , -) y espacios
    any_dataframe['monto'] = any_dataframe['monto'].str.replace(r'[$,\s-]', '', regex=True)
    # \s quiere decir espacio

    # Usas Regex con $ para eliminar el .0 o .00 SOLO si está AL FINAL
    any_dataframe['monto'] = any_dataframe['monto'].str.replace(r'\.0+$', '', regex=True)
    # \. Le dice a Python: "Busca un punto literal" (el \ quita el efecto de comodín)
    # .0+ Busca uno o más ceros seguidos.
    # $ Exige que esto esté únicamente al FINAL de la celda.

    # Lo conviertes a número entero o flotante
    #monto_col = pd.to_numeric(monto_col)

    return any_dataframe

def dato_fecha (date_string_dataframe):

    # Toma el dato de la columna y lo convierte a fecha
    date_string_dataframe['fecha'] = pd.to_datetime(date_string_dataframe['fecha'], 
                                                    format='mixed', 
                                                    dayfirst=True)

    return date_string_dataframe

# Limpia consola -----------------------------------
os.system('cls')

# Lee archivo CSV -----------------------------------
df = pd.read_csv('MOCK_DATA.csv')

# Muestra cabecera del archivo (Primeras filas) -----------------------------------
print('---Primeras filas---')
print(df.head())
print()


'''
# Me entrega todo el archivo con True o False. Donde está vacío me muestra True y, donde tiene información me muestra False -----------------------------------
print('---Archivo con booleanos---')
print(df.isnull())
print()

# El .sum() suma cuántos espacios hay vacíos en cada columna -----------------------------------
print('---Cantida de casillas vacías por columnas---')
print(df.isnull().sum())
print()

# Me muestra las filas que están duplicadas -----------------------------------
print('---Filas duplicada---')
print(df[df.duplicated()])
print()

# Me muestra la cantidad de filas duplicadas -----------------------------------
print('---Cantidad de filas duplicadas---')
print(len(df[df.duplicated()]))
print()
'''


# ===============================================================================
# Limpiando todo el archivo -----------------------------------

df_filas_borradas = df.dropna() # Elimina las filas cuyas celdas estén vacías

df_no_especificado = df.fillna('No Especificado')   # Mantengo todas las filas, pero aquellas filas cuyas celdas estén vacías, le doy el valor de 'No Especificado'


df_filas_borradas = minuscula_sin_tildes(df_filas_borradas) # Datos sin espacios, minúsculas y sin tildes

df_no_especificado = minuscula_sin_tildes(df_no_especificado) # Datos sin espacios, minúsculas y sin tildes


df_filas_borradas = limpieza_números(df_filas_borradas) # Limpia los números de carácteres que no sean numéricos

df_no_especificado = limpieza_números(df_no_especificado) # Limpia los números de carácteres que no sean numéricos

# Ingreso y gastos totales de la empresa -----------------------------------
# Se utiliza el dataframe con filas borradas porque el otro dataframe contiene valores no especificados que no se pueden convertir en numéricos
df_filas_borradas['monto'] = pd.to_numeric(df_filas_borradas['monto'])  # Convierte a numérico

# Suma el 'monto' agrupado por cada tipo de 'cuenta'
resumen_ingresos_gastos = df_filas_borradas.groupby('tipo')['monto'].sum()

print(f'El ingreso total de la empresa es: ${resumen_ingresos_gastos["ingreso"]} y los gastos son: ${resumen_ingresos_gastos['gasto']}')
print()

# Balance neto de la empresa -----------------------------------
balance_neto = resumen_ingresos_gastos['ingreso'] - resumen_ingresos_gastos['gasto']

print(f'El balance neto de la empresa es: ${balance_neto}')
print()

# Calculando el gasto total por categoría -----------------------------------
resumen_cateorias = df_filas_borradas.groupby('categoria')['monto'].sum().sort_values(ascending=False)

print(f'La categoría con mayor gasto es: {resumen_cateorias.idxmax().upper()} con un gasto de: ${resumen_cateorias.max()}')
print()

# Calculando el porcentaje de transacciones por método de pago -----------------------------------
porcentaje_metodos_pagos = (df_no_especificado['metodo_pago'].value_counts(normalize=True)*100).round(2)

print('---Porcentaje de transacciones por método de pago---')
print(f'{porcentaje_metodos_pagos}')
print()

# Calculando balance neto por fechas -----------------------------------

# Convierte el dato de la columna 'fecha' a fecha
df_filas_borradas = dato_fecha(df_filas_borradas)

# Creamos una nueva columna con el mes
df_filas_borradas['mes'] = df_filas_borradas['fecha'].dt.to_period('M')

# Creamos tabla pivote
pivote_mes_tipo_monto = df_filas_borradas.pivot_table(
                                                    index='mes',
                                                    columns='tipo',
                                                    values='monto',
                                                    aggfunc='sum',
                                                    fill_value=0).reset_index()

pivote_mes_tipo_monto ['balance_neto'] = pivote_mes_tipo_monto['ingreso'] - pivote_mes_tipo_monto['gasto']

print('---Balance neto por mes---')
print(pivote_mes_tipo_monto)
print()

# Calculando las 5 transacciones más altas -----------------------------------
top_5_transacciones = df_filas_borradas.nlargest(5, 'monto')
print('---Las 5 transacciones más altas---')
print(top_5_transacciones)
print()

'''
# Resultado -----------------------------------
print('---Resultado---')
print()
print('---Dataframe con filas borradas---')
print(df_filas_borradas)
print()
print('---Dataframe con filas con valores no escificados---')
print(df_no_especificado)
print()
'''


'''
# Limpia el dataframe de valores nulos y los guarda en una variable -----------------------------------
print('---Dataframe sin valores nulos---')
df_limpio = df.dropna()
print(df_limpio)
print()

# Me muestra las filas que están duplicadas -----------------------------------
print('---Cantidad de filas duplicadas---')
print(df_limpio[df_limpio.duplicated()])
print()

# Muestra solo la columna que quiero ver -----------------------------------
print('---Columna de monto---')
print(df_limpio['monto'])
print()

# Limpieza de datos en MONTO -----------------------------------
print('---Se quitan caracteres que no son numéricos, se conviente los números a dato númerico---')
# Limpias símbolos ($ , -) y espacios
df_limpio['monto'] = df_limpio['monto'].str.replace(r'[$,\s-]', '', regex=True)
# \s quiere decir espacio

# Usas Regex con $ para eliminar el .0 o .00 SOLO si está AL FINAL
df_limpio['monto'] = df_limpio['monto'].str.replace(r'\.0+$', '', regex=True)
# \. Le dice a Python: "Busca un punto literal" (el \ quita el efecto de comodín)
# .0+ Busca uno o más ceros seguidos.
# $ Exige que esto esté únicamente al FINAL de la celda.

# Lo conviertes a número entero o flotante
df_limpio['monto'] = pd.to_numeric(df_limpio['monto'])

print(df_limpio)
print()

# Limpiando columna de cuenta para responder las preguntas del gerente -----------------------------------
print('---Se quitan espacios y tildes para evitar errores de CUENTA---')
# Quitamos especios y colocamos todo en minuscula
df_limpio['cuenta'] = df_limpio['cuenta'].str.strip().str.lower()

#Remplazamos tildes por vocales sin tildes

# Función lambda para remplazar
df_limpio['cuenta'] = df_limpio['cuenta'].astype(str).apply(lambda x: x.translate(tabla_tildes))

print(df_limpio)
print()

# Limpiando columna de tipo
print('---Se quitan espacios y tildes para evitar errores de TIPO---')
# Quitamos especios y colocamos todo en minuscula
df_limpio['tipo'] = df_limpio['tipo'].str.strip().str.lower()

#Remplazamos tildes por vocales sin tildes

# Función lambda para remplazar
df_limpio['tipo'] = df_limpio['tipo'].astype(str).apply(lambda x: x.translate(tabla_tildes))

print(df_limpio)
print()

# Calculando total de ingresos y de gastos -----------------------------------
print('---Resumen de cuenta---')
# Suma el 'monto' agrupado por cada tipo de 'cuenta'
resumen_cuentas = df_limpio.groupby('tipo')['monto'].sum()

print(f'El tiempo de ingresos es: ${resumen_cuentas["ingreso"]}. Y el total de gastos es ${resumen_cuentas["gasto"]}')
print()

# Calculando balance neto -----------------------------------
print('---Balance neto---')
balance_neto = resumen_cuentas['ingreso']-resumen_cuentas['gasto']

print(f'Nuestro balance neto es: ${balance_neto}')
print()

# Calculando el gasto total por categoría -----------------------------------
# Limpiando columna de tipo
print('---Se quitan espacios y tildes para evitar errores de CATEGORÍA---')
# Quitamos especios y colocamos todo en minuscula
df_limpio['categoria'] = df_limpio['categoria'].str.strip().str.lower()

#Remplazamos tildes por vocales sin tildes

# Función lambda para remplazar
df_limpio['categoria'] = df_limpio['categoria'].astype(str).apply(lambda x: x.translate(tabla_tildes))

print(df_limpio)
print()

# Calculando total de ingresos y de gastos por categoría
print('---Resumen de categorías---')
# Suma el 'monto' agrupado por cada tipo de 'cuenta'
resumen_cateorias = df_limpio.groupby('categoria')['monto'].sum().sort_values(ascending=False)

print(resumen_cateorias)
print()

categoria_mas_costosa = resumen_cateorias.idxmax()

print(f'La categoría más costosa es {categoria_mas_costosa.upper()}')
print()

# Calculando el porcentaje de transacciones por método de pago -----------------------------------
# Limpiando columna de metodo_pago
# Reemplazar nulos en una columna de texto por "No especificado" o "Desconocido"
df['metodo_pago'] = df['metodo_pago'].fillna('No especificado')

# Se quitan espacios y tildes para evitar errores de MÉTODO DE PAGO
df['metodo_pago'] = df['metodo_pago'].str.strip().str.lower()

# Remplazamos tildes por vocales sin tildes
# Función lambda para remplazar
df['metodo_pago'] = df['metodo_pago'].astype(str).apply(lambda x: x.translate(tabla_tildes))

filas_duplicadas = df[df.duplicated(subset=['metodo_pago'], keep=False)]

print(filas_duplicadas)
print()

'''