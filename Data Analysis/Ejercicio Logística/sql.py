from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base
import pandas as pd

# Creamos la estructura de las entidades, con sus atributos, restricciones y relaciones
def create_DER ():

    Base = declarative_base()

    class Ciudad(Base):
        __tablename__ = 'ciudad'
        id_ciudad = Column(Integer, primary_key=True)
        nombre_ciudad = Column(String(100), nullable=False)

    class Transportista(Base):
        __tablename__ = 'transportista'
        id_transportista = Column(Integer, primary_key=True)
        nombre_transportista = Column(String(100), nullable=False)
        calificacion_transportista = Column(Float)

    class EstadoEnvio(Base):
        __tablename__ = 'estado_envio'
        id_estado_envio = Column(Integer, primary_key=True)
        nombre_estado_envio = Column(String(50), nullable=False)

    class Almacen(Base):
        __tablename__ = 'almacen'
        id_almacen = Column(Integer, primary_key=True)
        nombre_almacen = Column(String(100), nullable=False)
        id_ciudad = Column(Integer, ForeignKey('ciudad.id_ciudad'), nullable=False)

    class Envio(Base):
        __tablename__ = 'envio'
        id_envio = Column(String(50), primary_key=True)
        id_venta_relacionada = Column(String(50), nullable=False)
        fecha_envio = Column(Date, nullable=False)
        dias_estimados_entrega = Column(Integer, nullable=False)
        costo_envio_mxn = Column(Float, nullable=False)
        peso_kg = Column(Float, nullable=False)    
        id_transportista = Column(Integer, ForeignKey('transportista.id_transportista'), nullable=False)
        id_almacen_origen = Column(Integer, ForeignKey('almacen.id_almacen'), nullable=False)    
        id_estado_envio = Column(Integer, ForeignKey('estado_envio.id_estado_envio'), nullable=False)

    return Base

# Toma el SCV limpio y lo transforma en entidades
def procesar_entidades_envios (df):
    # --- CIUDAD ---
    ciudades_unicas = df['ciudad_origen'].unique()
    df_ciudad = pd.DataFrame({
        'id_ciudad': range(1, len(ciudades_unicas) + 1),
        'nombre_ciudad': ciudades_unicas
    })

    # --- TRANSPORTISTA ---
    transportistas_unicos = df[['transportista', 'calificacion_transportista']].drop_duplicates()
    transportistas_unicos['id_transportista'] = range(1, len(transportistas_unicos) + 1)
    df_transportista = transportistas_unicos[['id_transportista', 'transportista', 'calificacion_transportista']].rename(
        columns={'transportista': 'nombre_transportista'}
    )

    # --- ESTADO ENVIO ---
    estados_unicos = df['estado_envio'].unique()
    df_estado_envio = pd.DataFrame({
        'id_estado_envio': range(1, len(estados_unicos) + 1),
        'nombre_estado_envio': estados_unicos
    })

    # --- ALMACEN ---
    almacenes_unicos = df[['almacen_origen', 'ciudad_origen']].drop_duplicates()
    almacenes_unicos['id_almacen'] = range(1, len(almacenes_unicos) + 1)

    df_almacen = pd.merge(
        almacenes_unicos,
        df_ciudad,
        left_on='ciudad_origen',
        right_on='nombre_ciudad',
        how='left'
    )[['id_almacen', 'id_ciudad', 'almacen_origen']].rename(columns={'almacen_origen': 'nombre_almacen'})

    # --- ENVIOS ---
    df_copia = df.copy()
    df_copia = pd.merge(df_copia, df_transportista, left_on='transportista', right_on='nombre_transportista', how='left')
    df_copia = pd.merge(df_copia, df_almacen, left_on='almacen_origen', right_on='nombre_almacen', how='left')
    df_copia = pd.merge(df_copia, df_estado_envio, left_on='estado_envio', right_on='nombre_estado_envio', how='left')

    df_copia = df_copia[[
        'id_envio',
        'id_venta_relacionada',
        'id_transportista',
        'id_almacen',
        'fecha_envio',
        'dias_estimados_entrega',
        'costo_envio_mxn',
        'id_estado_envio',
        'peso_kg'
    ]].rename(columns={'id_almacen': 'id_almacen_origen'})

    diccionario_entidades = {
        'ciudad': df_ciudad,
        'transportista': df_transportista,
        'estado_envio': df_estado_envio,
        'almacen': df_almacen,
        'envios': df_copia
    }

    carga_a_postgres (diccionario_entidades)

# Carga las entidades en Postgres
def carga_a_postgres (entidades):
    # Configura tus credenciales reales
    USER = 'postgres'
    PASSWORD = '123456'
    HOST = 'localhost'
    PORT = '5432'
    DB_NAME = 'ej5_logistica'

    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

    # 1º Crea las tablas físicamente en Postgres con sus llaves primarias y foráneas
    Base = create_DER()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("🏗️  Tablas y restricciones (PK/FK) creadas en PostgreSQL con éxito.")

    # 2º Poblar las tablas en orden utilizando if_exists='append' (para respetar el esquema creado por SQLAlchemy)
    try:
        # Nivel 1: Padres
        entidades['ciudad'].to_sql('ciudad', con=engine, if_exists='append', index=False)
        entidades['transportista'].to_sql('transportista', con=engine, if_exists='append', index=False)
        entidades['estado_envio'].to_sql('estado_envio', con=engine, if_exists='append', index=False)
        
        # Nivel 2: Dependiente de ciudad
        entidades['almacen'].to_sql('almacen', con=engine, if_exists='append', index=False)
        
        # Nivel 3: Tabla principal de hechos
        entidades['envios'].to_sql('envio', con=engine, if_exists='append', index=False)
        
        print(f'🚀 Datos cargados exitosamente respetando toda la integridad relacional.\n')

    except Exception as e:
        print(f'❌ Error al cargar los datos: {e}\n')

# Nota importante. Debes tener muy en cuenta que todos los nombres de las entidades deben ser escritos iguales. Si algo diferente, te va a dar error