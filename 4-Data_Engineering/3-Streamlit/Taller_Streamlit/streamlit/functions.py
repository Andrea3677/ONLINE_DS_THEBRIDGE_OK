
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt


# Cargar los datos
@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv('data/red_recarga_acceso_publico_2021.csv',sep = ';', encoding='utf-8')
        return df
    except FileNotFoundError:
        st.error("Archivo 'estaciones_carga.csv' no encontrado.")
        return None
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None


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
    - 📍 Buscar estaciones por distrito
    - 🗺️ Ver la ubicación en un mapa interactivo
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

# Página de filtros
def mostrar_filtros():
    st.title("🔍 Filtros de Estaciones de Carga")
    st.markdown("---")
    
    if 'df' not in st.session_state or st.session_state.df is None:
        st.warning("No hay datos disponibles. Por favor, carga el archivo CSV.")
        return
    
    df = st.session_state.df
    
    # Inicializar variables para filtros
    filtro_distrito = None
    filtro_operador = None
    filtro_cargadores = None
    
    # Sidebar con filtros
    with st.sidebar:
        st.header("🎛️ Filtros")
        
        # Checkbox y filtro para distrito
        usar_distrito = st.checkbox("Filtrar por Distrito", value=False)
        if usar_distrito:
            distritos = sorted(df['DISTRITO'].unique())
            filtro_distrito = st.selectbox(
                "Seleccionar Distrito:",
                distritos
            )
        
        # Checkbox y filtro para operador
        usar_operador = st.checkbox("Filtrar por Operador", value=False)
        if usar_operador:
            operadores = sorted(df['OPERADOR'].unique())
            filtro_operador = st.selectbox(
                "Seleccionar Operador:",
                operadores
            )
        
        # Checkbox y filtro para número de cargadores
        usar_cargadores = st.checkbox("Filtrar por Nº de Cargadores", value=False)
        if usar_cargadores:
            min_cargadores = int(df['Nº CARGADORES'].min())
            max_cargadores = int(df['Nº CARGADORES'].max())
            valores_cargadores = list(range(min_cargadores, max_cargadores + 1))
            
            filtro_cargadores = st.select_slider(
                "Rango de Nº de Cargadores:",
                options=valores_cargadores,
                value=(min_cargadores, max_cargadores)
            )
    
    # Aplicar filtros al dataframe
    df_filtrado = df.copy()
    
    if usar_distrito and filtro_distrito:
        df_filtrado = df_filtrado[df_filtrado['DISTRITO'] == filtro_distrito]
    
    if usar_operador and filtro_operador:
        df_filtrado = df_filtrado[df_filtrado['OPERADOR'] == filtro_operador]
    
    if usar_cargadores and filtro_cargadores:
        min_val, max_val = filtro_cargadores
        df_filtrado = df_filtrado[
            (df_filtrado['Nº CARGADORES'] >= min_val) & 
            (df_filtrado['Nº CARGADORES'] <= max_val)
        ]
    
    # Verificar si el dataframe filtrado está vacío
    if df_filtrado.empty:
        st.warning("⚠️ No se encontraron estaciones con los filtros seleccionados.")
        st.stop()
    
    # Mostrar estadísticas de los filtros aplicados
    st.subheader(f"📈 Estaciones encontradas: {len(df_filtrado)}")
    
    # Organizar en columnas (3:2)
    col_map, col_stats = st.columns([3, 2])
    
    with col_map:
        st.subheader("📍 Mapa de Estaciones")
        
        # Crear dataframe para el mapa (con columnas lat/lon)
        df_mapa = df_filtrado[['latidtud', 'longitud', 'DIRECCION', 'Nº CARGADORES', 'OPERADOR']].copy()
        df_mapa.columns = ['lat', 'lon', 'direccion', 'cargadores', 'operador']
        
        # Configurar zoom según filtro de distrito
        zoom = 13 if (usar_distrito and filtro_distrito) else 11
        
        # Mostrar mapa
        st.map(df_mapa, zoom=zoom)
    
    with col_stats:
        st.subheader("📊 Distribuciones")
        
        # 8. Si no hemos utilizado el filtro de distrito vamos a mostrar la distribución de las estaciones en los distritos
        if not usar_distrito:
            st.markdown("**Distribución por Distrito**")
            distrito_counts = df_filtrado['DISTRITO'].value_counts()
            if len(distrito_counts) > 0:
                st.bar_chart(distrito_counts)
            else:
                st.write("No hay datos para mostrar")
        
        # 9. Si no hemos utilizado el filtro de operador vamos a mostrar la distribución de las estaciones de cada operador
        if not usar_operador:
            st.markdown("**Distribución por Operador**")
            operador_counts = df_filtrado['OPERADOR'].value_counts()
            if len(operador_counts) > 0:
                st.bar_chart(operador_counts)
            else:
                st.write("No hay datos para mostrar")
        
        # 10. Vamos a mostrar cuantos cargadores hay de cada tamaño
        st.markdown("**Distribución por Nº de Cargadores**")
        cargadores_counts = df_filtrado['Nº CARGADORES'].value_counts().sort_index()
        if len(cargadores_counts) > 0:
            st.bar_chart(cargadores_counts)
        else:
            st.write("No hay datos para mostrar")
    
    # Mostrar tabla con resultados filtrados
    with st.expander("📋 Ver estaciones filtradas"):
        st.dataframe(df_filtrado[['DISTRITO', 'DIRECCION', 'Nº CARGADORES', 'OPERADOR']])