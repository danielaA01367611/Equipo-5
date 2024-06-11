import streamlit as st
from PIL import Image
import pandas as pd
from io import StringIO
import plotly.express as px
from datetime import datetime
import numpy as np
import os

# Función para recortar la imagen
def crop_image(image_path, crop_box):
    image = Image.open(image_path)
    cropped_image = image.crop(crop_box)
    return cropped_image

# Función para verificar el formato de la fecha
def check_date_format(date_str):
    try:
        pd.to_datetime(date_str, format='%d/%m/%Y %H:%M')
        return True
    except ValueError:
        return False

if 'Inicio' not in st.session_state:
    st.session_state['Inicio'] = {}

st.set_page_config(page_title='TDR transportes', page_icon='🚚', layout='wide')


# Sidebar
st.sidebar.image('imagenes/logo.png', use_column_width=True)
dashboard_mode = st.sidebar.radio('Seleccionar el apartado que deseas visualizar', ('Inicio', 'Tabla', 'Gráficos', 'Gráficos detallados', 'Rutas'))


# Mostrar el contenido basado en la opción seleccionada
if dashboard_mode == 'Inicio':

    # Encabezado de la página principal
    with st.container():
        header_image_path = 'imagenes/TDR 2.jpeg'
        crop_box = (50, 300, 800, 500)  # Ajusta estos valores según sea necesario (left, upper, right, lower)
        header_image = crop_image(header_image_path, crop_box)
        st.image(header_image, use_column_width=True)
        st.title('TDR transportes: PORTAL DE PAGO DE CASETAS 🚚')
        st.header('La grandeza de TDR es gracias a la grandeza de su gente')
        st.write('Somos TDR, trabajando siempre en la creación e implementación de soluciones integrales de transporte, rentables, eficientes e innovadoras.')
        st.write('[Saber más >](https://www.tdr.com.mx/index.html)')
        
        with st.container():
            st.write('---')
            text_column, animation_column = st.columns(2)
            with text_column:
                st.header('¿Qué puedes hacer en este portal? 🔍')
                st.write(
                    """
                    El objetivo de este portal es corroborar el costo acumulado de casetas según el número de orden.
                    Aquí puedes visualizar: 

                    - Fechas de inicio y fin de las ordenes

                    - Ciudad de origen y ciudad destino de las ordenes

                    - Número de camión que completó la orden

                    - Total acumulado pagado en casetas por orden

                    - Presupuesto del pago total de casetas por ruta

                    - Gráficos y apoyos visuales de los datos
                    """
                )
            with animation_column:
                st.empty()
                
        with st.container():
            st.write('---')
            st.header('Sube los archivos necesarios:')
            st.write('##')

            # Widget para subir archivo scroll order
            uploaded_file_scroll_order = st.file_uploader("Sube tu archivo xls de scroll order", type=["xls"])
        
        if uploaded_file_scroll_order is not None:
            df_scroll_order = pd.read_excel(uploaded_file_scroll_order)
            st.session_state['Inicio']['scroll_order'] = df_scroll_order

            st.write("Archivo de scroll order cargado:")
            st.dataframe(df_scroll_order)

        # Repetir para otros archivos
        uploaded_file_capufe = st.file_uploader("Sube tu archivo xls de CAPUFE", type=["xls"])
        if uploaded_file_capufe is not None:
            df_capufe = pd.read_excel(uploaded_file_capufe)
            st.session_state['Inicio']['capufe'] = df_capufe
            st.write("Archivo de CAPUFE cargado:")
            st.dataframe(df_capufe)

        uploaded_file_televia = st.file_uploader("Sube tu archivo xls de Televia", type=["xls"])
        if uploaded_file_televia is not None:
            df_televia = pd.read_excel(uploaded_file_televia)
            st.session_state['Inicio']['televia'] = df_televia
            st.write("Archivo de Televia cargado:")
            st.dataframe(df_televia)

        uploaded_file_rutas = st.file_uploader("Sube tu archivo xls de rutas", type=["xls"])
        if uploaded_file_rutas is not None:
            df_rutas = pd.read_excel(uploaded_file_rutas)
            st.session_state['Inicio']['rutas'] = df_rutas
            st.write("Archivo de rutas cargado:")
            st.dataframe(df_rutas)
       
        with st.container():
            st.write('---')
            st.header('Servicios')
            st.write('')

        with st.container():
            st.write('---')
            st.write('')
            image_column, text_column = st.columns((2, 1))
            with image_column:
                image = Image.open('imagenes/tabla.png')
                st.image(image, use_column_width=True)
            with text_column:
                st.subheader('Dataframe registro de ordenes')
                st.write(
                    """
                    En el siguiente apartado podrás visualizar en detalle cada orden,
                    incluyendo su fecha de inicio y finalización, lugar de partida y destino (la ruta completa),
                    número del camión que realizó la orden, etiqueta registrada en la caseta,
                    proveedor, monto total pagado y monto total presupuestado.
                    """
                )
        with st.container():
            st.write('---')
            st.write('')
            image_column, text_column = st.columns((2, 1))
            with image_column:
                image = Image.open('imagenes/ej.graf.png')
                st.image(image, use_column_width=True)
            with text_column:
                st.subheader('Gráficos')
                st.write(
                    """
                    En este apartado puedes visualizar gráficos que muestran los resultados del mes de operaciones de TDR.
                    Estos gráficos facilitan la identificación visual de casos extraordinarios,
                    permitiendo analizar qué ocurrió, cómo solucionarlo y,
                    sobre todo, cómo prevenir que vuelva a suceder.
                    """
                )

        with st.container():
            st.write('---')
            st.write('')
            image_column, text_column = st.columns((2, 1))
            with image_column:
                image = Image.open('imagenes/graficas.png')
                st.image(image, use_column_width=True)
            with text_column:
                st.subheader('Gráficos detallados')
                st.write(
                    """
                    En este apartado puedes visualizar gráficos mucho más detallados,
                    con los que se pueden encontrar detalles más específicos de las órdenes
                    según la fecha de inicio y finalización de estas, o según el total gastado
                    por número decamión.
                    """
                )

        with st.container():
            st.write('---')
            st.write('')
            image_column, text_column = st.columns((2, 1))
            with image_column:
                image = Image.open('imagenes/ruta.png')
                st.image(image, use_column_width=True)
            with text_column:
                st.subheader('Rutas')
                st.write(
                    """
                    En este apartado puedes visualizar a detalle las rutas que se tuvieron que seguir,
                    el costo de cada una en Global Map, así como visualizarlas
                    en un mapa.
                    """
                )

elif dashboard_mode == 'Tabla':
    # Contenido del apartado 'Tabla'
    st.markdown("<h1 style='font-weight: bold;'>Búsqueda por órdenes o por camiones 🔍</h1>", unsafe_allow_html=True)
    st.markdown("---")

    with st.container():
        st.write('##')

        # Formulario de búsqueda
        search_option = st.selectbox(
            'Seleccione el tipo de búsqueda:',
            ('Número de Orden', 'Número de Camión')
        )

        if search_option == 'Número de Orden':
            order_number = st.text_input('Ingrese el Número de Orden:')
            if st.button('Buscar por Número de Orden'):
                # Lógica de búsqueda por número de orden
                st.write(f'Resultados para el Número de Orden: {order_number}')
                # Aquí puedes agregar el código para buscar y mostrar los resultados

        elif search_option == 'Número de Camión':
            tractor_number = st.text_input('Ingrese el Número de Camión:')
            if st.button('Buscar por Número de Camión'):
                # Lógica de búsqueda por número de tractor
                st.write(f'Resultados para el Número de Camión: {tractor_number}')
                # Aquí puedes agregar el código para buscar y mostrar los resultados

        if 'scroll_order' in st.session_state['Inicio'] and 'capufe' in st.session_state['Inicio'] and 'televia' in st.session_state['Inicio'] and 'rutas' in st.session_state['Inicio']:
            df_scroll_order = st.session_state['Inicio']['scroll_order']
            df_capufe = st.session_state['Inicio']['capufe']
            df_televia = st.session_state['Inicio']['televia']
            df_rutas = st.session_state['Inicio']['casetas']

            df_scroll_order['ord_startdate'] = pd.to_datetime(df_scroll_order['ord_startdate'], format='%d-%m-%Y %H:%M:%S')
            df_scroll_order['ord_completiondate'] = pd.to_datetime(df_scroll_order['ord_completiondate'], format='%d-%m-%Y %H:%M:%S')
            df_televia['Fecha'] = pd.to_datetime(df_televia['Fecha'], format='%d-%m-%Y %H:%M:%S')
            df_capufe['FECHA Y HORA CRUCE'] = pd.to_datetime(df_capufe['FECHA Y HORA CRUCE'], format='%d/%m/%Y %H:%M')    

    class display(object):
        """Display HTML representation of multiple objects"""
        template = """<div style="float: left; padding: 10px;">
        <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
        </div>"""
        def __init__(self, *args):
            self.args = args

        def _repr_html_(self):
            return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                            for a in self.args)

        def __repr__(self):
            return '\n\n'.join(a + '\n' + repr(eval(a))
                               for a in self.args)
               
    merged_dfs = pd.merge(df_televia, df_scroll_order, how='inner', on='TAG')
    cumple = (merged_dfs['Fecha'] >= merged_dfs['ord_startdate'] - pd.Timedelta(minutes=10)) & (merged_dfs['Fecha'] <= merged_dfs['ord_completiondate'] + pd.Timedelta(minutes=10))
    merged_dfs[cumple]

    cumplen = merged_dfs[cumple]
    grouped_df = cumplen.groupby(cumplen['ord_number']).agg({
        'Importe': ['sum'], 'TAG': 'max'
    })

    grouped_df = grouped_df.reset_index()

    grouped_df.columns = ['_'.join(col).strip() if type(col) is tuple else col for col in grouped_df.columns.values]

    grouped_df.columns = ['ord_number', 'IMPORTE TELEVIA', 'TAG']

    merged_dfs2 = pd.merge(df_capufe, df_scroll_order, how='inner', on='TAG')
    cumple2 = (merged_dfs2['FECHA Y HORA CRUCE'] >= merged_dfs2['ord_startdate'] - pd.Timedelta(minutes=10)) & (merged_dfs2['FECHA Y HORA CRUCE'] <= merged_dfs2['ord_completiondate'] + pd.Timedelta(minutes=10))
    merged_dfs2[cumple2]

    cumplen2 = merged_dfs2[cumple2]
    grouped_df2 = cumplen2.groupby(cumplen2['ord_number']).agg({
        'IMPORTE COBRADO': ['sum'], 'TAG': 'max'
    })

    grouped_df2 = grouped_df2.reset_index()

    grouped_df2.columns = ['_'.join(col).strip() if type(col) is tuple else col for col in grouped_df2.columns.values]

    grouped_df2.columns = ['ord_number', 'IMPORTE CAPUFE', 'TAG']

    imp = pd.concat([grouped_df, grouped_df2], ignore_index=True)

    Costos = pd.merge(imp, df_scroll_order, on="ord_number")
    combinaciones = Costos.groupby(['origin_cty_nmstct', 'dest_cyt_nmstct']).size().reset_index(name='conteo')

    Costos['origin_cty_nmstct'] = Costos['origin_cty_nmstct'].str.replace('MONTERREY,NX/', 'MONTERREY,NX')
    Costos['dest_cyt_nmstct'] = Costos['dest_cyt_nmstct'].str.replace('MONTERREY,NX/', 'MONTERREY,NX')

    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('Cuautitlan Izcalli', 'CUAUTITLAN IZCALLI,EM')
    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('Gustavo A. Madero', 'GUSTAVO A. MADERO,DF/Mex')
    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('Iztapalapa', 'IZTAPALAPA,DF')
    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('Monterrey', 'MONTERREY,NX')
    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('San Miguel Xoxtla', 'SAN MIGUEL XOXTLA,PU')
    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('Zapotlanejo', 'ZAPOTLANEJO,JA/Mex')
    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('Tonala', 'TONALA,JA')
    df_rutas['origin_cty_nmstct'] = df_rutas['origin_cty_nmstct'].str.replace('Juarez', 'JUAREZ,NX')

    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('Cuautitlan Izcalli', 'CUAUTITLAN IZCALLI,EM')
    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('Gustavo A. Madero', 'GUSTAVO A. MADERO,DF/Mex')
    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('Iztapalapa', 'IZTAPALAPA,DF')
    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('Monterrey', 'MONTERREY,NX')
    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('San Miguel Xoxtla', 'SAN MIGUEL XOXTLA,PU')
    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('Zapotlanejo', 'ZAPOTLANEJO,JA/Mex')
    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('Tonala', 'TONALA,JA')
    df_rutas['dest_cyt_nmstct'] = df_rutas['dest_cyt_nmstct'].str.replace('Juarez', 'JUAREZ,NX')

    ComparativaV2 = pd.merge(Costos, df_rutas, on=['origin_cty_nmstct', 'dest_cyt_nmstct'], how='inner')
    ComparativaV2['IMPORTE TOTAL'] = ComparativaV2['IMPORTE TELEVIA'].fillna(0) + ComparativaV2['IMPORTE CAPUFE'].fillna(0)
    ComparativaV2.drop(columns=['TAG_x', 'TAG_y', 'IMPORTE TELEVIA', 'IMPORTE CAPUFE', 'Column1', 'ord_revtype4', 'ord_totalcharge', 'origin_cty_nmstct', 'dest_cyt_nmstct', 'ord_totalmiles'], inplace=True)

    ComparativaV2.rename(columns={'billto_cmp_id': 'Cliente'}, inplace=True)
    ComparativaV2.rename(columns={'Costo total': 'Costo presupuestado (Global Maps)'}, inplace=True)
    ComparativaV2.rename(columns={'IMPORTE TOTAL': 'Costo calculado'}, inplace=True)

    tabla_fin = ComparativaV2[ComparativaV2['Ruta'] != 'San Miguel Xoxtla-Gustavo A. Madero']
    tabla_fin= tabla_fin.reset_index(drop=True)
    print(tabla_fin)

