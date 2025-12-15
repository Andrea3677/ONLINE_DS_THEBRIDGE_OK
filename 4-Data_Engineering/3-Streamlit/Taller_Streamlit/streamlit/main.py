import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from functions import *
#st.beta_expander ahora es expander
# Este es mi script

st.set_page_config(page_title='Estaciones carga Madrid', layout='wide', page_icon="⚡")
st.title("🔌 Estaciones de Carga para Coches Eléctricos en Madrid")
st.image('img/puntos-recarga-madrid.jpg')
data = pd.read_csv('data/red_recarga_acceso_publico_2021.csv', sep = ';')
data


uploaded_file = st.file_uploader("Sube un archivo .csv", type= ['.csv'])

# Configuración de la página
st.set_page_config(page_title="Estaciones de Carga Madrid", page_icon="⚡", layout="wide")



# Cargar datos al inicio
if 'df' not in st.session_state:
    df = cargar_datos()
    st.session_state.df = df

# Configuración de la página
st.set_page_config(page_title="Estaciones de Carga Madrid", page_icon="⚡", layout="wide")

# Cargar los datos
@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv('estaciones_carga.csv', encoding='utf-8')
        return df
    except FileNotFoundError:
        st.error("Archivo 'estaciones_carga.csv' no encontrado.")
        return None
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

# Página de inicio
def mostrar_home():
    st.title("⚡ Estaciones de Carga para Coches Eléctricos en Madrid")
    st.markdown("---")
    
    st.header("Bienvenido/a")
    st.write("""
    Esta aplicación te permite explorar las estaciones de carga para coches eléctricos 
    disponibles en la ciudad de Madrid.
    
    ### Funcionalidades:
    - 📊 Visualizar estadísticas de cargadores por operador
    - 🔍 Filtrar estaciones por distrito, operador y número de cargadores
    - 📍 Ver la ubicación en un mapa interactivo
    - 🗺️ Explorar distribución de estaciones por distrito y operador
    """)
    
    # Mostrar algunos datos generales si tenemos el dataframe
    if 'df' in st.session_state and st.session_state.df is not None:
        df = st.session_state.df
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Estaciones", len(df))
        with col2:
            st.metric("Total Cargadores", df['Nº CARGADORES'].sum())
        with col3:
            st.metric("Operadores", df['OPERADOR'].nunique())

# Página de datos
def mostrar_datos():
    st.title("📊 Análisis de Datos")
    st.markdown("---")
    
    if 'df' not in st.session_state or st.session_state.df is None:
        st.warning("No hay datos disponibles. Por favor, carga el archivo CSV.")
        return
    
    df = st.session_state.df
    
    # Bar chart de cargadores por operador
    st.header("Número de Cargadores por Operador")
    cargadores_por_operador = df.groupby('OPERADOR')['Nº CARGADORES'].sum().sort_values(ascending=False)
    st.bar_chart(cargadores_por_operador)
    
    # También podemos mostrar la tabla de datos si el usuario lo desea
    with st.expander("Ver datos tabulares"):
        st.dataframe(df)

# Cargar datos al inicio
if 'df' not in st.session_state:
    df = cargar_datos()
    st.session_state.df = df

# Sidebar con selector de página
with st.sidebar:
    st.image(width=100)
    st.title("Navegación")
    
    # Selector de página
    pagina = st.selectbox(
        "Selecciona una página:",
        ["🏠 Inicio", "📊 Datos y Gráficos", "🔍 Filtros y Mapa"]
    )

# Mostrar la página seleccionada
if pagina == "🏠 Inicio":
    mostrar_home()
elif pagina == "📊 Datos y Gráficos":
    mostrar_datos()
elif pagina == "🔍 Filtros y Mapa":
    mostrar_filtros()
