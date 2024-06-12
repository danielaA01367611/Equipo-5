import streamlit as st
from PIL import Image
import pandas as pd
from io import StringIO
#import plotly.express as px
from datetime import datetime
import numpy as np
import altair as alt
#import folium
from streamlit_folium import folium_static
import requests
from streamlit_lottie import st_lottie
    
# Función para recortar la imagen
def crop_image(image_path, crop_box):
    image = Image.open(image_path)
    cropped_image = image.crop(crop_box)
    return cropped_image

st.set_page_config(page_title='TDR transportes', page_icon='🚚', layout='wide')
st.sidebar.image('imagenes/logo.png', use_column_width=True)
dashboard_mode = st.sidebar.selectbox("**Selecciona una pestaña:**", ['Inicio','Carga','Pre-procesamiento de datos', 'Tabla', 'Gráficos', 'Rutas'])
#df_scroll_order,  df_casetas, df_project, df_capufe, df_televia, df_gm = None, None, None, None, None, None

# Función para cargar y procesar archivos
if dashboard_mode == "Carga":
    st.title("📥 Menú de carga")
    st.divider()
    st.header("Dataframes")
    # Opción para subir archivos
    uploaded_file_project =st.sidebar.file_uploader("Proyecto Seleccionado Final (Excel)", type=["csv", "xlsx"])
    uploaded_file_capufe =st.sidebar.file_uploader("Archivo de Capufe (Excel)", type=["csv", "xlsx"])
    uploaded_file_televia =st.sidebar.file_uploader("Archivo de Televia (Excel)", type=["csv", "xlsx"])
    uploaded_file_global_map =st.sidebar.file_uploader("Archivo de Global Map (Excel)", type=["csv", "xlsx"])

    if st.sidebar.button('Procesar Archivos'):
        # Procesar los archivos si se hace clic en el botón
        if uploaded_file_project and uploaded_file_capufe and uploaded_file_televia and uploaded_file_global_map :
            global df_project, df_capufe, df_televia, df_gm
            df_project = pd.read_csv(uploaded_file_project) if uploaded_file_project.name.endswith('.csv') else pd.read_excel(uploaded_file_project)
            df_capufe = pd.read_csv(uploaded_file_capufe) if uploaded_file_capufe.name.endswith('.csv') else pd.read_excel(uploaded_file_capufe)
            df_televia = pd.read_csv(uploaded_file_televia) if uploaded_file_televia.name.endswith('.csv') else pd.read_excel(uploaded_file_televia)
            df_gm = pd.read_csv(uploaded_file_global_map) if uploaded_file_global_map.name.endswith('.csv') else pd.read_excel(uploaded_file_global_map)

            st.write(df_project.head(3))
            st.write(df_capufe.head(3))
            st.write(df_televia.head(3))
            st.write(df_gm.head(3))

            st.session_state['project']= df_project
            st.session_state['capufe']=df_capufe
            st.session_state['televia']=df_televia
            st.session_state['global map']=df_gm

            st.write('DataFrames cargados:')
            st.write('Carga DataFrame 1 **Exitoso**: ' + uploaded_file_project.name + str(df_project.shape))
            st.write('Carga DataFrame 2 **Exitoso**: ' + uploaded_file_capufe.name + str(df_capufe.shape))
            st.write('Carga DataFrame 3 **Exitoso**: ' + uploaded_file_televia.name + str(df_televia.shape))
            st.write('Carga DataFrame 4 **Exitoso**: ' + uploaded_file_global_map.name + str(df_gm.shape))
        else:
            st.write('No se ha cargado/validado archivos')
  
# Mostrar el contenido basado en la opción seleccionada
if dashboard_mode == 'Inicio':  

    # Encabezado de la página principal
    with st.container():
        header_image_path = 'imagenes/TDR 2.jpeg'
        crop_box = (50, 300, 800, 500)  # Ajusta estos valores según sea necesario (left, upper, right, lower)
        header_image = crop_image(header_image_path, crop_box)
        st.image(header_image, use_column_width=True)
        st.title('TDR transportes: PORTAL DE PAGO DE CASETAS')
        st.header('La grandeza de TDR es gracias a la grandeza de su gente')
        st.write('Somos TDR, trabajando siempre en la creación e implementación de soluciones integrales de transporte, rentables, eficientes e innovadoras.')
        st.write('[Saber más >](https://www.tdr.com.mx/index.html)')
        
    with st.container():
        st.write('---')
        text_column, image_column = st.columns(2)
        with text_column:
            st.header('¿Qué puedes hacer en este portal? 🔍')
            st.write(
                """
                El objetivo de este portal es verificar el costo acumulado de casetas según el número de orden.
                Aquí puedes visualizar:
                
                - **Fechas de inicio y fin de las órdenes:** Consulta las fechas clave de tus órdenes de transporte.

                - **Ciudad de origen y ciudad destino de las órdenes:** Identifica los puntos de partida y destino de cada orden.

                - **Número del camión que completó la orden:** Verifica cuál camión fue asignado a cada orden.

                - **Total acumulado pagado en casetas por orden:** Revisa el costo total de casetas por cada orden específica.

                - **Presupuesto del pago total de casetas por ruta:** Compara los costos reales con los presupuestos previstos para cada ruta.

                - **Gráficos y apoyos visuales de los datos:** Visualiza la información de manera gráfica para facilitar su comprensión.
                """
            )
        with image_column:
            st.image('imagenes/TDR1.jpeg', use_column_width=True)

       
    with st.container():
        st.write('---')
        st.header('Servicios')
        st.write('')

    with st.container():
        st.write('---')
        st.write('')
        image_column, text_column = st.columns((2, 1))
        with image_column:
            image = Image.open('imagenes/df.png')
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader('Dataframe registro de ordenes 🧾')
            st.write(
                """
                En el siguiente apartado podrás visualizar en detalle cada orden,
                  incluyendo su fecha de inicio y finalización, lugar de partida
                    y destino (la ruta completa), número del camión que realizó la orden,
                      etiqueta registrada en la caseta, proveedor, monto total pagado y 
                      monto total presupuestado.

                """
            )
    with st.container():
        st.write('---')
        st.write('')
        image_column, text_column = st.columns((2, 1))
        with image_column:
            image = Image.open('imagenes/grafs.png')
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader('Gráficos 📊')
            st.write(
                """
                En este apartado, puedes visualizar gráficos que muestran los resultados
                  mensuales de las operaciones de TDR. Estos gráficos facilitan la 
                  identificación visual de casos extraordinarios, permitiendo analizar qué ocurrió,
                    cómo solucionarlo y, sobre todo, cómo prevenir que vuelva a suceder.
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
            st.subheader('Gráficos detallados 📈')
            st.write(
                """
                En este apartado, puedes visualizar gráficos mucho más detallados,
                  que permiten encontrar detalles específicos de las órdenes según
                    su fecha de inicio y finalización, o según el total gastado por número de camión.
                """
            )

    with st.container():
        st.write('---')
        st.write('')
        image_column, text_column = st.columns((2, 1))
        with image_column:
            image = Image.open('imagenes/rutas.png')
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader('Rutas 🗺')
            st.write(
                """
                 En este apartado, puedes visualizar en detalle las rutas que se siguieron representadas en un mapa.
                """
            )
if 'Pre-procesamiento' not in st.session_state:
    st.session_state['Pre-procesamiento'] = {}

if dashboard_mode == 'Pre-procesamiento de datos':
    st.markdown("<h1 style='font-weight: bold;'>Sube aquí tus archivos a procesar 📁</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Subir y mostrar archivo de Scroll Order
    st.markdown("### Archivo de Scroll Order")
    uploaded_file_scroll_order = st.file_uploader("Sube tu archivo del scroll order (Excel)", type=["xls", "xlsx"])

    # Subir y mostrar archivo de Casetas
    st.markdown("### Archivo de Casetas")
    uploaded_file_casetas = st.file_uploader("Sube tu archivo de casetas (Excel)", type=["xls", "xlsx"])

    if uploaded_file_scroll_order and uploaded_file_casetas:
        # Todos los archivos han sido subidos
        st.success("Todos los archivos se han cargado correctamente. Puedes proceder con el procesamiento de datos.")

        # Ahora puedes leer los archivos y realizar el procesamiento de datos
        df_scroll_order = pd.read_excel(uploaded_file_scroll_order)
        df_casetas = pd.read_excel(uploaded_file_casetas)

        # Filtrar y procesar los datos
        df_scroll_order = df_scroll_order[(df_scroll_order.orderby_cmp_id == 'GNV') | (df_scroll_order.orderby_cmp_id == 'GNVMTY01')]
        df_casetas = df_casetas[['Unidad', 'TAG']]
        df_casetas['Unidad'] = df_casetas['Unidad'].astype(str)
        df_casetas = df_casetas[(df_casetas.Unidad == '1710') |
                                (df_casetas.Unidad == '1712') |
                                (df_casetas.Unidad == '1713') |
                                (df_casetas.Unidad == '1778') |
                                (df_casetas.Unidad == '1780') |
                                (df_casetas.Unidad == '1784') |
                                (df_casetas.Unidad == '1786') |
                                (df_casetas.Unidad == '1835') |
                                (df_casetas.Unidad == '1868') |
                                (df_casetas.Unidad == '1711')]
        df_casetas = df_casetas.drop_duplicates()
        df_scroll_order = df_scroll_order.reset_index(drop=True)
        df_casetas = df_casetas.reset_index(drop=True)
        df_scroll_order = df_scroll_order.rename(columns={'ord_tractor': 'Unidad'})
        df_scroll_order['Unidad'] = df_scroll_order['Unidad'].astype(str)
        df_final = pd.merge(df_casetas, df_scroll_order, on="Unidad")
        df_final = df_final[['Unidad', 'TAG', 'ord_number', 'billto_cmp_id', 'ord_startdate', 'ord_completiondate', 'ord_revtype4', 'ord_totalcharge', 'origin_cty_nmstct', 'dest_cyt_nmstct', 'ord_totalmiles']]

        st.write("Resultado final del procesamiento:")
        st.dataframe(df_final)

    else:
        # Alguno o todos los archivos no se han subido correctamente
        st.error("Por favor, asegúrate de cargar todos los archivos antes de continuar.")

elif dashboard_mode == 'Tabla':
    # Contenido del apartado 'Tabla'
    st.markdown("<h1 style='font-weight: bold;'>Tabla de órdenes mensuales por proyecto 📋</h1>", unsafe_allow_html=True)
    st.markdown("---")

    df_project=(st.session_state.get('project'))
    df_capufe=(st.session_state.get('capufe'))
    df_televia=(st.session_state.get('televia'))
    df_gm=(st.session_state.get('global map'))

    df_project['ord_startdate'] = pd.to_datetime(df_project['ord_startdate'], format='%d-%m-%Y %H:%M:%S')
    df_project['ord_completiondate'] = pd.to_datetime(df_project['ord_completiondate'], format='%d-%m-%Y %H:%M:%S')
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
            

    merged_dfs = pd.merge(df_televia, df_project, how='inner', on='TAG')
    cumple = (merged_dfs['Fecha'] >= merged_dfs['ord_startdate'] - pd.Timedelta(minutes=10)) & (merged_dfs['Fecha'] <= merged_dfs['ord_completiondate'] + pd.Timedelta(minutes=10))
        #merged_dfs[cumple]

    cumplen = merged_dfs[cumple]
    grouped_df = cumplen.groupby(cumplen['ord_number']).agg({
            'Importe': ['sum'], 'TAG': 'max'
        })

    grouped_df = grouped_df.reset_index()
    grouped_df.columns = ['_'.join(col).strip() if type(col) is tuple else col for col in grouped_df.columns.values]
    grouped_df.columns = ['ord_number', 'IMPORTE TELEVIA', 'TAG']

    merged_dfs2 = pd.merge(df_capufe, df_project, how='inner', on='TAG')
    cumple2 = (merged_dfs2['FECHA Y HORA CRUCE'] >= merged_dfs2['ord_startdate'] - pd.Timedelta(minutes=10)) & (merged_dfs2['FECHA Y HORA CRUCE'] <= merged_dfs2['ord_completiondate'] + pd.Timedelta(minutes=10))
        #merged_dfs2[cumple2]

    cumplen2 = merged_dfs2[cumple2]
    grouped_df2 = cumplen2.groupby(cumplen2['ord_number']).agg({
            'IMPORTE COBRADO': ['sum'], 'TAG': 'max'
        })

    grouped_df2 = grouped_df2.reset_index()
    grouped_df2.columns = ['_'.join(col).strip() if type(col) is tuple else col for col in grouped_df2.columns.values]
    grouped_df2.columns = ['ord_number', 'IMPORTE CAPUFE', 'TAG']

    imp = pd.concat([grouped_df, grouped_df2], ignore_index=True)
    Costos = pd.merge(imp, df_project, on="ord_number")
    Costos['origin_cty_nmstct'] = Costos['origin_cty_nmstct'].str.replace('MONTERREY,NX/', 'MONTERREY,NX')
    Costos['dest_cyt_nmstct'] = Costos['dest_cyt_nmstct'].str.replace('MONTERREY,NX/', 'MONTERREY,NX')

    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('Cuautitlan Izcalli', 'CUAUTITLAN IZCALLI,EM')
    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('Gustavo A. Madero', 'GUSTAVO A. MADERO,DF/Mex')
    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('Iztapalapa', 'IZTAPALAPA,DF')
    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('Monterrey', 'MONTERREY,NX')
    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('San Miguel Xoxtla', 'SAN MIGUEL XOXTLA,PU')
    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('Zapotlanejo', 'ZAPOTLANEJO,JA/Mex')
    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('Tonala', 'TONALA,JA')
    df_gm['origin_cty_nmstct'] = df_gm['origin_cty_nmstct'].str.replace('Juarez', 'JUAREZ,NX')

    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('Cuautitlan Izcalli', 'CUAUTITLAN IZCALLI,EM')
    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('Gustavo A. Madero', 'GUSTAVO A. MADERO,DF/Mex')
    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('Iztapalapa', 'IZTAPALAPA,DF')
    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('Monterrey', 'MONTERREY,NX')
    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('San Miguel Xoxtla', 'SAN MIGUEL XOXTLA,PU')
    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('Zapotlanejo', 'ZAPOTLANEJO,JA/Mex')
    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('Tonala', 'TONALA,JA')
    df_gm['dest_cyt_nmstct'] = df_gm['dest_cyt_nmstct'].str.replace('Juarez', 'JUAREZ,NX')

    ComparativaV2 = pd.merge(Costos, df_gm, on=['origin_cty_nmstct', 'dest_cyt_nmstct'], how='inner')
    ComparativaV2['IMPORTE TOTAL'] = ComparativaV2['IMPORTE TELEVIA'].fillna(0) + ComparativaV2['IMPORTE CAPUFE'].fillna(0)
    ComparativaV2.drop(columns=['TAG_x', 'TAG_y', 'IMPORTE TELEVIA', 'IMPORTE CAPUFE', 'Column1', 'ord_revtype4', 'ord_totalcharge', 'origin_cty_nmstct', 'dest_cyt_nmstct', 'ord_totalmiles'], inplace=True)

    ComparativaV2.rename(columns={'billto_cmp_id': 'Cliente'}, inplace=True)
    ComparativaV2.rename(columns={'Costo total': 'Costo presupuestado (Global Maps)'}, inplace=True)
    ComparativaV2.rename(columns={'IMPORTE TOTAL': 'Costo calculado'}, inplace=True)
    ComparativaV2.rename(columns={'ord_number': 'Núm. de orden'}, inplace=True)
    ComparativaV2.rename(columns={'ord_startdate': 'Fecha inicio'}, inplace=True)
    ComparativaV2.rename(columns={'ord_completiondate': 'Fecha final'}, inplace=True)

    tabla_fin = ComparativaV2[ComparativaV2['Ruta'] != 'San Miguel Xoxtla-Gustavo A. Madero']
    tabla_fin= tabla_fin.reset_index(drop=True)
    st.header("Resultado final:")
    st.dataframe(tabla_fin)
    st.session_state['tabla_fin']=tabla_fin

    st.markdown("<h1 style='font-weight: bold;'>Búsqueda por número de orden o por unidad 🔍</h1>", unsafe_allow_html=True)
    st.markdown("---")
    search_option = st.selectbox(
        'Seleccione el tipo de búsqueda:',
        ('Número de Orden', 'Número de Camión')
    )   

    if search_option == 'Número de Orden':
        order_number = st.number_input('Ingrese el Número de Orden:')
        if st.button('Buscar por Número de Orden'):
            # Lógica de búsqueda por número de orden
            results = tabla_fin[tabla_fin['Núm. de orden'] == order_number]
            if not results.empty:
                st.write(f'Resultados para el Número de Orden: {order_number}')
                st.dataframe(results)
            else:
                st.write(f'No se encontraron resultados para el Número de Orden: {order_number}')

    elif search_option == 'Número de Camión':
        tractor_number = st.number_input('Ingrese el Número de Camión:')
        if st.button('Buscar por Número de Camión'):
            # Lógica de búsqueda por número de tractor
            results = tabla_fin[tabla_fin['Unidad'] == tractor_number]
            if not results.empty:
                st.write(f'Resultados para el Número de Camión: {tractor_number}')
                st.dataframe(results)
            else:
                st.write(f'No se encontraron resultados para el Número de Camión: {tractor_number}')

elif dashboard_mode == 'Gráficos':
    st.markdown("<h1 style='font-weight: bold;'>Gráficos 📊</h1>", unsafe_allow_html=True)
    st.markdown("---")

        #Códigos para gráficas
    caputag =  (st.session_state.get('capufe'))
    teletag = (st.session_state.get('televia'))

    teletag['Fecha'] = pd.to_datetime(teletag['Fecha'], format='%d-%m-%Y %H:%M:%S')
    caputag['FECHA Y HORA CRUCE'] = pd.to_datetime(caputag['FECHA Y HORA CRUCE'], format='%d/%m/%Y %H:%M')

    tagss = pd.concat([caputag, teletag], ignore_index=True)

    tagss['IMPORTE TOTAL'] = tagss['IMPORTE COBRADO'].fillna(0) + tagss['Importe'].fillna(0)

    tagss['Fechas'] = tagss['FECHA Y HORA CRUCE'].combine_first(tagss['Fecha'])

    tags = tagss.drop(columns=['IMPORTE COBRADO', 'Importe'])

    tags = tagss.drop(columns=['FECHA Y HORA CRUCE', 'Fecha'])

    fechatag = tags[['TAG', 'IMPORTE TOTAL', 'Fechas']]

    df_cu = (st.session_state.get('project'))

    df_cu= df_cu[['Unidad', 'TAG']]

    fechatag = pd.merge(fechatag, df_cu, how='inner', on='TAG')
    fechatag = fechatag.drop_duplicates()
    fechatag = fechatag.reset_index(drop=True)


    fechatagsum = fechatag.groupby('Unidad')['IMPORTE TOTAL'].sum().reset_index()

    fechatagsum['Unidad'] = fechatagsum['Unidad'].astype(str)

    df=(st.session_state.get('tabla_fin'))

    df['Unidad'] = df['Unidad'].astype(str)


    # Contenido del apartado 'Gráficos'
    st.markdown("<h1 style='font-weight: bold;'>Gráficos Generales TDR</h1>", unsafe_allow_html=True)
    st.markdown("---")

    costo_calculado_total = df['Costo calculado'].sum()
    costo_presupuestado_total = df['Costo presupuestado (Global Maps)'].sum()

    # Mostrar los resultados en dos cajas en la parte superior
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Costo Calculado Total", value=f"${costo_calculado_total:,.2f}")

    with col2:
        st.metric(label="Costo Presupuestado Total (Global Maps)", value=f"${costo_presupuestado_total:,.2f}")

    chart1, chart2 = st.columns(2)
    with chart1:

        bar = alt.Chart(fechatagsum).mark_bar().encode(
            x='Unidad',
            y=alt.Y('IMPORTE TOTAL'),
            color=alt.condition(
                alt.datum['IMPORTE TOTAL'] == max(fechatagsum['IMPORTE TOTAL']),
                alt.value('#ff0000'),
                alt.value('lightgrey'))  # Condición, ValorVerdadero, ValorFalso
        ).transform_window(
            max_importe='max(IMPORTE TOTAL)'
        ).properties(
            title='Tag con mayor gasto del mes')

        st.altair_chart(bar, use_container_width= True)

    with chart2:
        fechatagsum

    palette = [
        "#005D7E",
        "#008995",
        "#00B492",
        "#89DB7E",
        "#F9F871",
        "#496185",
        "#DEF2FF",
        "#DCA11C",
        "#00C6BA",
        "#FFF7D6",
        "#D7F4F0"]

    # Crear la escala de colores personalizada
    color_scale = alt.Scale(domain=list(df['Ruta'].unique()), range=palette[:len(df['Ruta'].unique())])


    boxplot1 = alt.Chart(df).mark_bar().encode(
        y='Ruta',
        x='Costo calculado',
        color = alt.Color('Ruta', scale=color_scale)).properties(
        title='Costo calculado por ruta')

    boxplot2 = alt.Chart(df).mark_bar().encode(
        y='Ruta',
        x='Costo presupuestado (Global Maps)',
        color = 'Ruta').properties(
        title='Costo presupuestado por ruta según Global Maps')

    boxplot1 & boxplot2

    # Contenido del apartado 'Gráficos detallados'
    st.markdown("<h1 style='font-weight: bold;'>Gráficos Gráficos detallados TDR</h1>", unsafe_allow_html=True)
    st.markdown("---")

    fechatag['Unidad'] = fechatag['Unidad'].astype(str)

    palette = ['#0e131c', '#132031', '#162c47', '#264061', '#435c7f',
                '#61799e', '#8097be', '#163355', '#181655', '#165355']

    # Crear la escala de colores personalizada
    color_scale = alt.Scale(domain=list(fechatag['Unidad'].unique()), range=palette[:len(fechatag['Unidad'].unique())])

    click=alt.selection_multi(encodings=['color'])
    barra1 = alt.Chart(fechatag).mark_bar().encode(
        x='Unidad',
        y='max(IMPORTE TOTAL)',
        color=alt.condition(click,'Unidad', alt.value('lightgray'), scale=color_scale)
        ).add_selection(click).properties(
        title='Registro de el pago más alto por No. de Unidad')

    linea1=alt.Chart(fechatag).mark_line().encode(
        x='Fechas',
        y='IMPORTE TOTAL',
        color='Unidad').properties(
        width=700).transform_filter(click).properties(
        title='Registro de pagos por fecha')

    barra1 | linea1

    palette = [
        "#005D7E",
        "#008995",
        "#00B492",
        "#89DB7E",
        "#F9F871",
        "#496185",
        "#DEF2FF",
        "#DCA11C",
        "#00C6BA",
        "#FFF7D6",
        "#D7F4F0"]

    click=alt.selection_multi(encodings=['color']) # 1

    color_scale = alt.Scale(domain=list(df['Ruta'].unique()), range=palette[:len(df['Ruta'].unique())])

    barra1_1=alt.Chart(df).mark_bar().encode(
        x='Costo calculado',
        y='Ruta',
        color=alt.condition(click,'Ruta', alt.value('lightgray'), scale=color_scale)
        ).add_selection(click).properties(
            title='Costo calculado por ruta')

    # graf secundaria
    barra1_2=alt.Chart(df).mark_bar().encode(
        x='Costo calculado',
        y='Unidad',
        color='Costo calculado'
        ).transform_filter(click).properties(
            title='Registro de cobras por ruta')

    barra1_1&barra1_2

elif dashboard_mode == 'Rutas':
    def add_marker(map_object, lat, lon, popup_text, marker_color='blue'):
        folium.Marker(
            location=[lat, lon],
            popup=popup_text,
            icon=folium.Icon(color=marker_color)
        ).add_to(map_object)
        
    def add_polyline(map_object, locations, color='blue'):
        folium.PolyLine(locations, color=color, weight=2.5, opacity=1).add_to(map_object)


    def clean_coordinates(df, columns):
            for col in columns:
                df[col] = df[col].astype(str).str.replace(r'[^\d.-]', '', regex=True)
                df[col] = pd.to_numeric(df[col], errors='coerce')
            return df

# SE ejecuta la app de streamlit
    st.title("Rutas y casetas en el mapa 🗺")

# Botón para subir archivos excel o csv,con sus respectivas leyendas
    uploaded_file = st.file_uploader("Sube tu archivo de Excel o CSV", type=["xlsx", "csv"])

    if uploaded_file:
        st.write("Asegúrese de que su archivo contenga las coordenadas correctas.")
        if st.button("Procesar archivo"):
            # Se determina el tipo de archivo y se lee la data
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file, sheet_name='Hoja1')
            elif uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)

        # Se extraen las columnas limpias de latitud y longitud de las variables: origen, destino y casetas
                df = clean_coordinates(df, ['latitudO', 'longitudO', 'latitudD', 'longitudD', 'latitudC', 'longitudC'])

        # Se despliega el dataframe para su previa visualización
        st.dataframe(df)

        # Se crea el mapa inicial con México centralizado
        m = folium.Map(location=[23.6345, -102.5528], zoom_start=5)

        # Iteración de  markups por destino, origen y casetas
        for ruta in df['Ruta'].unique():
            route_data = df[df['Ruta'] == ruta]

            if len(route_data) > 0:
                locations = []

                # Se agregan los marcadores de destino y origen  para el mapa
                for index, row in route_data.iterrows():
                    if not pd.isna(row['latitudO']) and not pd.isna(row['longitudO']):
                        add_marker(m, row['latitudO'], row['longitudO'], f"Inicio: {row['origin_cty_nmstct']}", 'green')
                        locations.append((row['latitudO'], row['longitudO']))
                    if not pd.isna(row['latitudD']) and not pd.isna(row['longitudD']):
                        add_marker(m, row['latitudD'], row['longitudD'], f"Fin: {row['dest_cty_nmstct']}", 'red')
                        locations.append((row['latitudD'], row['longitudD']))

                # Añade los marcadores de peaje y los incluye en la polilínea
                for index, row in route_data.iterrows():
                    if not pd.isna(row['latitudC']) and not pd.isna(row['longitudC']):
                        add_marker(m, row['latitudC'], row['longitudC'], f"Caseta: {row['Casetas']}", 'blue')
                        locations.append((row['latitudC'], row['longitudC']))

                # Añade la polilínea para marcar / generar la ruta.
                if locations:
                    add_polyline(m, locations)

        # Despliegue del mapa en la app de streamlit
        folium_static(m)