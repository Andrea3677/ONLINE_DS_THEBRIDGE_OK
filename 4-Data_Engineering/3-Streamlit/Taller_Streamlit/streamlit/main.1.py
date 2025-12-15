import streamlit as st
import pandas as pd
from PIL import Image
from functions import *
#st.beta_expander ahora es expander
# Este es mi script

import streamlit as st
import pandas as pd
from PIL import Image

# Configuración de la página
st.set_page_config(page_title='Cargatron', layout='wide', page_icon=':battery:')
st.title("🔌 Estaciones de Carga para Coches Eléctricos en Madrid")
st.image('img/puntos-recarga-madrid.jpg')
data = pd.read_csv('data/red_recarga_acceso_publico_2021.csv', sep = ';')
data

# Página de inicio
home_page()
   
# Página de datos
data_page()

# Menú lateral
st.sidebar.title("Navegación")

# Cargar datos y guardar en session_state
data = cargar_datos()
st.session_state.data = data

# Selector de página en el sidebar
page = st.sidebar.selectbox(
    "Selecciona una página:",
    ["🏠 Inicio", "📊 Datos y Gráficos"]
)

# Mostrar la página seleccionada
if page == "🏠 Inicio":
    home_page()
elif page == "📊 Datos y Gráficos":
    data_page()

# Información adicional en el sidebar
st.sidebar.markdown("---")
st.sidebar.info("""
**Información de los datos:**
- Total de estaciones: {}
- Total de cargadores: {}
""".format(
    len(st.session_state.data) if 'data' in st.session_state else 0,
    st.session_state.data['Nº CARGADORES'].sum() if 'data' in st.session_state else 0
))