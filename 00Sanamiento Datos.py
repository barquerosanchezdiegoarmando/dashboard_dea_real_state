import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import re 
import plotly.graph_objects as go
import plotly.figure_factory as ff

csv_file1 = "Melbourne_Housing.csv"
df1 = pd.read_csv(csv_file1)

st.set_page_config(page_title='Resultados del Análisis de Datos', layout = "wide")
with st.container():
    izquierda, centro , derecha = st.columns((1,1,1))
    with centro:
        st.header("Sanamiento de los Datos")
with st.container():
    st.write("___")
    st.markdown("#### Set de Datos Original  (24114, 16)")
    if st.checkbox("Set de datos Original"):
            st.dataframe(df1, height = 200)
            st.success("Haz desplegado Melbourne_Housing.csv")
    st.write("___")
    st.markdown("#### Sanamiento de los datos")
    st.markdown("""
                    - Originalmente las columnas BuildingArea asi como Date su tipo de dato era de str. 
                    En el caso de la fecha simplemente se implemento el siguiente código para transformar el Dtype a datetime64.
                    """)  
    st.code("df1[""Date""] = pd.to_datetime(df1[""Date""])")
    st.markdown("""
                    - En el caso de BuildingArea fue necesario identificar la existencia de las palabras inf y missing dentro de los valores únicos que deberían ser exclusivamente numericos. Con la inteción facilitar el tratamiento de los datos se intercambiaron todos las entradas que contuvieran dichas str´s por nan o en español como valores no numericos a traves del siguiente código.
                    """)  
    st.code("df1[""BuildingArea""] = df1[""BuildingArea""].replace([""inf"", ""missing""], np.nan)")
    st.markdown("- Sin embargo, los datos seguian siendo strings, por lo que se transformaron todos los datos de la columna BuildingArea a floats.")
    st.code("""df1[""BuildingArea""] = df1[""BuildingArea""].astype(float)""")
    st.markdown(" - Otro problema a primera vista del set de datos es la gran cantidad de valores no numéricos o nan, siendo concretos en las siguientes columnas.")
    st.markdown(""" 
                    *Bedroom           6436* \n
                    *Bathroom          6442* \n
                    *Car               6817* \n
                    *Landsize          9241* \n
                    *BuildingArea     16585* \n
                    *YearBuilt        15129* \n
                    """)
    st.markdown("- Por último se observo la existencia de valores repetidos, los cuales fueron eliminados considerando el hecho de que hay plena cantidad de datos aún y sin olvidar reiniciar el indice para fácilitar el análisis en los próximos apartados.")
    st.code("df1.drop_duplicates(inplace=True)")
    st.code("df1.reset_index(drop=True, inplace=True)")