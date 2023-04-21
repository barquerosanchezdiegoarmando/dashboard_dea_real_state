import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import re 
import plotly.graph_objects as go
import plotly.figure_factory as ff

# organizamos la vara 
st.set_page_config(page_title='AnalisisUni/EDA', layout = "wide")

# Cargamos los datos
csv_file1 = "Melbourne_Housing.csv"
csv_file2 = "Melbourne_Housing_NMD.csv"
csv_file3 = 'Melbourne_Housing_NMD&NOD (1).csv'

# asignamos los datos a variables
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
df3 = pd.read_csv(csv_file3)


# Análisis univariado 

with st.container():
    st.markdown("## Análisis Univariable")
    st.write("___")
    
    # Distancia
with st.container():
    izquierda, centro , derecha = st.columns((2.22,1,2))
    with centro:
        st.markdown("### *Distancia*")
    st.write("___")
with st.container():
    centro , derecha = st.columns((1,1))
    with centro:
        x = df1["Distance"]
        fig = px.histogram(df1, x="Distance",
                   labels={'Distance':'Distancia', "count":"Frecuencia"}, # can specify one label per df column
                   color_discrete_sequence=['indianred'] # color of histogram bars
                   )
        st.write(fig)
        st.info("Nota: La distribución esta levemente inclinada a la derecha.")
    with derecha:
        y = df1["Distance"]
        fig = go.Figure()
        fig.add_trace(go.Box(y=y,name='Distancia',marker_color = 'indianred'))
        st.write(fig)
        st.info("Nota: Existe una gran cantidad de valores atípicos, en este caso en los valores altos de los datos. Si el Y>25.2 se considera un valor atípico.")
    
    # Tamaño de la propiedad
with st.container():
    st.write("___")
    izquierda, centro , derecha = st.columns((1.8,1,2))
    with centro:
        st.markdown("### *Tamaño de la Propiedad*")
    st.write("___")
with st.container():
    centro , derecha = st.columns((1,1))
    with centro:
        x = df1["Landsize"]
        fig = px.histogram(df1, x="Landsize",
                   labels={'Landsize':'Tamaño-Propiedad', "count":"Frecuencia"}, # can specify one label per df column
                   color_discrete_sequence=['indianred'] # color of histogram bars
                   )
        st.write(fig)
        st.info("Nota: La distribución esta sumamente inclinada a la derecha. Y se puede intuir facilmente que es muy complicado encontrar una propiedad con más de 1500 m^2")
    with derecha:
        y = df1["Landsize"]
        fig = go.Figure()
        fig.add_trace(go.Box(y=y,name='Distancia',marker_color = 'indianred'))
        st.write(fig)
        st.info("Nota: Existe una gran cantidad de valores atípicos, en este caso en los valores altos de los datos. Si el Y>1330 m^2 se considera un valor atípico.")
    
    # Area construida
with st.container():
    st.write("___")
    izquierda, centro , derecha = st.columns((2,1,2))
    with centro:
        st.markdown("### *Área Construida*")
    st.write("___")
with st.container():
    centro , derecha = st.columns((1,1))
    with centro:
        x = df1["BuildingArea"]
        fig = px.histogram(df1, x="BuildingArea",
                   labels={'BuildingArea':'Área-Construida', "count":"Frecuencia"}, # can specify one label per df column
                   color_discrete_sequence=['indianred'] # color of histogram bars
                   )
        st.write(fig)
        st.info("Nota: La distribución esta inclinada a la derecha. Seria relevante analizar individualmente las casas que posean más de 2000m^2 de construicción para verificar que no sea un error.")
    with derecha:
        y = df1["BuildingArea"]
        fig = go.Figure()
        fig.add_trace(go.Box(y=y,name='Área-Construida',marker_color = 'indianred'))
        st.write(fig)
        st.info("Nota: Existe una gran cantidad de valores atípicos, en este caso en los valores altos de los datos. Si el Y>306m^2 se consideran valores atípicos.")
    
    # Precio
with st.container():
    st.write("___")
    izquierda, centro , derecha = st.columns((2.27,1,2))
    with centro:
        st.markdown("### *Precio*")
    st.write("___")
with st.container():
    centro , derecha = st.columns((1,1))
    with centro:
        x = df1["Price"]
        fig = px.histogram(df1, x="Price",
                   labels={'Price':'Precio', "count":"Frecuencia"}, # can specify one label per df column
                   color_discrete_sequence=['indianred'] # color of histogram bars
                   )
        st.write(fig)
        st.info("Nota: La distribución esta inclinada a la derecha. Aquellas propiedades que su precio de venta fuera mayor a 7M necesitarán un análisis individualizado.")
    with derecha:
        y = df1["Price"]
        fig = go.Figure()
        fig.add_trace(go.Box(y=y,name='Precio',marker_color = 'indianred'))
        st.write(fig)
        st.info("Nota: Existe una gran cantidad de valores atípicos, en este caso en los valores altos de los datos. Si el Y>2.295M se consideran valores atípicos.")
        
    # Habitaciones
with st.container():
    st.write("___")
    izquierda, centro , derecha = st.columns((2.15,1,2))
    with centro:
        st.markdown("### *Habitaciones*")
    st.write("___")
with st.container():
    centro , derecha = st.columns((1,1))
    with centro:
        x = df1["Rooms"]
        fig = px.histogram(df1, x="Rooms",
                   labels={'Rooms':'Habitaciones', "count":"Frecuencia"}, # can specify one label per df column
                   color_discrete_sequence=['indianred'] # color of histogram bars
                   )
        st.write(fig)
        st.info("Nota: La distribución esta inclinada a la derecha pero levemente. Se realizo el análisis para saber cuales son el tipo de propiedad que poseen más de 7 habitaciones, el resultado fue que más del 90% son tipo casas y el resto son unidades.")
    with derecha:
        y = df1["Rooms"]
        fig = go.Figure()
        fig.add_trace(go.Box(y=y,name='Habitaciones',marker_color = 'indianred'))
        st.write(fig)
        st.info("Nota: Existe una gran cantidad de valores atípicos, en este caso en los valores altos de los datos. Si el Y>8 habitaciones se consideran valores atípicos.")

with st.container():
    st.write("___")
    izquierda , derecha = st.columns((1,1))
    with derecha:
        st.markdown("### Estadísticos Relevantes")
        tablaestadisticas = df1.describe()
        st.write(tablaestadisticas)
    with izquierda:
        st.markdown(
            """ 
            ### Nombre-Región
            """
                    )
        fig = px.histogram(df1, x="Regionname", color="Regionname")
        st.write(fig)
    st.write("___")

with st.container():
    st.markdown("### Este Dashboard-Web sigue en desarrollo, próxima actualización después de examenes ...")