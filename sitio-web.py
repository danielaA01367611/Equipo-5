import streamlit as st
from PIL import Image
import pandas as pd
from io import StringIO
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title='TDR transportes', page_icon='🚚', layout='wide')

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

                st.write("Archivo de scroll order cargado:")
                st.dataframe(df_scroll_order)

                # Verificar formato de las fechas
                date_column_scroll_order = st.selectbox("Selecciona la columna de fecha en scroll order", df_scroll_order.columns)
                df_scroll_order["Valid_Date_Format"] = df_scroll_order[date_column_scroll_order].apply(check_date_format)

                if df_scroll_order["Valid_Date_Format"].all():
                    st.success("Todas las fechas tienen el formato correcto (YYYY-MM-DD).")
                else:
                    st.error("Algunas fechas no tienen el formato correcto (YYYY-MM-DD).")
                    st.write(df_scroll_order[~df_scroll_order["Valid_Date_Format"]])

            # Widget para subir archivo de Televia
            uploaded_file_televia = st.file_uploader("Sube tu archivo xls de Televia", type=["xls"])

            if uploaded_file_televia is not None:
                df_televia = pd.read_excel(uploaded_file_televia)
                st.write("Archivo de Televia cargado:")
                st.dataframe(df_televia)

                date_column_televia = st.selectbox("Selecciona la columna de fecha en Televia", df_televia.columns)
                df_televia["Valid_Date_Format"] = df_televia[date_column_televia].apply(check_date_format)

                if df_televia["Valid_Date_Format"].all():
                    st.success("Todas las fechas tienen el formato correcto (YYYY-MM-DD).")
                else:
                    st.error("Algunas fechas no tienen el formato correcto (YYYY-MM-DD).")
                    st.write(df_televia[~df_televia["Valid_Date_Format"]])

            # Widget para subir archivo de Capufe
            uploaded_file_capufe = st.file_uploader("Sube tu archivo xls de Capufe", type=["xls"])

            if uploaded_file_capufe is not None:
                df_capufe = pd.read_excel(uploaded_file_capufe)
                st.write("Archivo de Capufe cargado:")
                st.dataframe(df_capufe)

                date_column_capufe = st.selectbox("Selecciona la columna de fecha en Capufe", df_capufe.columns)
                df_capufe["Valid_Date_Format"] = df_capufe[date_column_capufe].apply(check_date_format)

                if df_capufe["Valid_Date_Format"].all():
                    st.success("Todas las fechas tienen el formato correcto (YYYY-MM-DD).")
                else:
                    st.error("Algunas fechas no tienen el formato correcto (YYYY-MM-DD).")
                    st.write(df_capufe[~df_capufe["Valid_Date_Format"]])

            # Widget para subir archivo de Casetas
            uploaded_file_casetas = st.file_uploader("Sube tu archivo xls de Casetas", type=["xls"])

            if uploaded_file_casetas is not None:
                df_casetas = pd.read_excel(uploaded_file_casetas)
                st.write("Archivo de Casetas cargado:")
                st.dataframe(df_casetas)

                date_column_casetas = st.selectbox("Selecciona la columna de fecha en Casetas", df_casetas.columns)
                df_casetas["Valid_Date_Format"] = df_casetas[date_column_casetas].apply(check_date_format)

                if df_casetas["Valid_Date_Format"].all():
                    st.success("Todas las fechas tienen el formato correcto (YYYY-MM-DD).")
                else:
                    st.error("Algunas fechas no tienen el formato correcto (YYYY-MM-DD).")
                    st.write(df_casetas[~df_casetas["Valid_Date_Format"]])
       
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

    uploaded_file = st.file_uploader("Cargar archivo CSV o Excel", type=["csv", "xlsx"])

    st.write('---')
    st.header('Busca una orden en específico')

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

