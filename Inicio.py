import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import re 
import plotly.graph_objects as go
import plotly.figure_factory as ff


# Funcion para que se vean bonitas las animaciones
def load_lottierurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Cargamos los datos
csv_file1 = "Melbourne_Housing.csv"
csv_file2 = "Melbourne_Housing_NMD.csv"
csv_file3 = 'Melbourne_Housing_NMD&NOD (1).csv'

# activos para la pagina web 
lottie_australia_flag = load_lottierurl("https://assets5.lottiefiles.com/packages/lf20_CxlOOY0FFP.json")
lottie_mapa = load_lottierurl("https://assets1.lottiefiles.com/packages/lf20_vbzjobli.json")

# organizamos la vara 
st.set_page_config(page_title='Resultados del Análisis de Datos', layout = "wide")

# Inicio
with st.container():
    inicio_izq, inicio_centro ,inicio_derecha = st.columns((0.5,1,1))
    with inicio_centro:
        st.markdown("# Análisis Exploratorio de Datos")
        st.markdown("### *Bienes Raíces en Melbourne, Australia*")
    with inicio_derecha:
        col1, col2 = st.columns(2)
        col1.metric("diego.barquero.sanchez", "@est.una.ac.cr", "Correo Institucional")
        col2.metric("506-", "87378612", "Teléfono Personal:")
    with inicio_izq:
        st_lottie(lottie_australia_flag, height = 200, key = "Australia")

# asignamos los datos a variables
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
df3 = pd.read_csv(csv_file3)


with st.container():
    st.write("___")
    izquierda , derecha = st.columns((1,1))
    with derecha:
        st_lottie(lottie_mapa, height = 600)
    with izquierda:
        st.markdown(
            """ 
            ## Descripción original de los datos:
            El diccionario de datos detallado se proporciona a continuación:
            * Suburbio - Suburbio en el que se encuentra la propiedad
            * Habitaciones - Número de habitaciones en la propiedad
            * Tipo - Tipo de propiedad como
                * h - casa, cabaña, villa, semi, terraza,
                * t - casa adosada,
                * u - unidad, dúplex
            * VendedorG - Nombre del agente inmobiliario que vendió la propiedad
            * Fecha - Fecha en que se vendió la propiedad
            * Distancia - Distancia de la propiedad desde CBD en kilómetros. CBD es el distrito central de negocios de la ciudad.
            * Código postal - Código postal de la zona
            * Dormitorios - Número de dormitorios en la propiedad
            * Baño - Número de baños en la propiedad
            * Coche - Número de plazas de aparcamiento en la propiedad
            * Terreno - Tamaño del terreno en metros cuadrados
            * Tamaño-Construido: tamaño del edificio en metros cuadrados.
            * Año-Construcción - Año en que se construyó el edificio.
            * Nombre-Región: nombre de la región en la que se encuentra la propiedad, como Eastern Metropolitan, Western Metropolitan, Northern Victoria, etc.
            * Número-Propiedades - Número de propiedades que están presentes en el suburbio.
            * Precio - precio (en AUD) al que se vendió la propiedad.
            """
                    )
    st.write("___")
    
with st.container():
     izquierda, centro , derecha = st.columns((1,1,1))
     with centro:
         st.header("Sets de Datos")
with st.container():
    st.write("___")
    izquierda, centro , derecha = st.columns((1,1,1))
    with izquierda:
        if st.checkbox("Set de datos Original"):
            st.dataframe(df1, height = 400)
            st.success("Haz desplegado Melbourne_Housing.csv")
    with centro:
        if st.checkbox("Set de datos sin valores no númericos"):
            st.dataframe(df2, height = 400)
            st.success("Haz desplegado Melbourne_Housing_NMD.csv")
    with derecha:
        if st.checkbox("Set de datos sin valores no númericos y sin valores atípicos"):
            st.dataframe(df2, height = 400)
            st.success("Haz desplegado Melbourne_Housing_NMD_NOD.csv")
