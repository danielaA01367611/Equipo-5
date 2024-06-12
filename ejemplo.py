import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime
import matplotlib.pyplot as plt


st.set_page_config(page_title="TDR Transportes", page_icon="imagenes/logo.png",layout="wide") # page_icon=":fire:"
st.sidebar.image("imagenes/logo.png", use_column_width=True)

dashboard_mode = st.sidebar.selectbox("**Selecciona una pestaña:**", ["Carga", "Mostrar", "Gráfica"])
df_maps,  df_casetas, df_dispatch = None, None, None

# Intenta convertir diferentes formatos de fecha hasta que acepte uno o devuelve False
def check_date_format(date_str):
    date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y', '%d-%m-%Y']
    for date_format in date_formats:
        try:
            pd.to_datetime(date_str, format=date_format)
            return True
        except ValueError:
            pass
        return False

# Convierte
def transform_date_format(date_str):
    date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y', '%d-%m-%Y']
    for date_format in date_formats:
        try:
            return pd.to_datetime(date_str, format=date_format)
        except ValueError:
            pass
        return pd.Timestamp('today')

if dashboard_mode == "Carga":
    st.title(":bar_chart: Menu carga")
    st.divider()
    st.header("Dataframes")
    # Opción para subir archivos
    uploaded_file_inv_1 = st.sidebar.file_uploader('**Subir archivo de Dispatch**', type=['csv', 'xlsx'])
    uploaded_file_inv_2 = st.sidebar.file_uploader('**Subir archivo de Global Maps**', type=['csv', 'xlsx'])
    uploaded_file_inv_3 = st.sidebar.file_uploader('**Subir archivo de Casetas**', type=['csv', 'xlsx'])

    if st.sidebar.button('Procesar Archivos'):
        # Procesar los archivos si se hace clic en el botón
        if uploaded_file_inv_1 and uploaded_file_inv_2 and uploaded_file_inv_3:

            df_dispatch = pd.read_csv(uploaded_file_inv_1) if uploaded_file_inv_1.name.endswith('.csv') else pd.read_excel(uploaded_file_inv_1)
            df_maps = pd.read_csv(uploaded_file_inv_2) if uploaded_file_inv_2.name.endswith('.csv') else pd.read_excel(uploaded_file_inv_2)
            df_casetas = pd.read_csv(uploaded_file_inv_3) if uploaded_file_inv_3.name.endswith('.csv') else pd.read_excel(uploaded_file_inv_3)

            # Filtrar las filas con formato de fecha incorrecto
            df_dispatch['Fechas'] = df_dispatch['Fechas'].apply(transform_date_format) # archivo bueno

            df_maps['Fechas'] = df_maps['Fechas'].apply(transform_date_format) # archivo con problema, se sobreescribe valor con fecha de hoy

            df_casetas = df_casetas[df_casetas['Fechas'].apply(check_date_format)] # archivo con problema, se saltarán errores

            st.write(df_dispatch.head(3))
            st.write(df_maps.head(3))
            st.write(df_casetas.head(3))

            st.session_state['maps']= df_maps
            st.session_state['casetas']=df_casetas
            st.session_state['dispatch']=df_dispatch

            st.write('DataFrames cargados:')
            st.write('Carga DataFrame 1 **Exitoso**: ' + uploaded_file_inv_1.name + str(df_dispatch.shape))
            st.write('Carga DataFrame 2 **Exitoso**: ' + uploaded_file_inv_2.name + str(df_maps.shape))
            st.write('Carga DataFrame 3 **Exitoso**: ' + uploaded_file_inv_3.name + str(df_casetas.shape))
        else:
            st.write('No se ha cargado/validado archivos')
            
elif dashboard_mode == "Mostrar":
        st.title(":bar_chart: DASHBOARD Menu Principal")
        st.header("Menu principal")
        #uploaded_file = st.file_uploader("Cargar archivo CSV o Excel", type=["csv", "xlsx"])
        #st.dataframe(df_maps)        #st.write(df_maps)
        st.write(st.session_state.get('maps'))

elif dashboard_mode == "Gráfica":
    st.subheader('Plotly Chart')
    fig = px.histogram(st.session_state.get('maps')['IMPORTE TOTAL'])
    st.plotly_chart(fig)