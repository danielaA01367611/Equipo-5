import streamlit as st
from PIL import Image
import pandas as pd
from io import StringIO
import plotly.express as px
from datetime import datetime


st.set_page_config(page_title='TDR transportes', page_icon='🚚', layout='wide')


def crop_image(image_path, crop_box):
    image = Image.open(image_path)
    cropped_image = image.crop(crop_box)
    return cropped_image

#sidebar
st.sidebar.image('imagenes/logo.png', use_column_width=True)
dashboard_mode=st.sidebar.radio('Seleccionar el apartado que deseas visualizar', ('Inicio', 'Tabla', 'Gráficos', 'Gráficos detallados','Rutas'))
rutas_df=None

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



    if uploaded_file is None:
        df = pd.read_excel("SALIDA A FABRICACION Limpia.xlsx")
        st.warning("Por favor, carga un dataset para comenzar.")
    else:
        df = None
        file_extension = uploaded_file.name.split(".")[-1]

        # Cargar el archivo según su extensión
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extension in ["xls", "xlsx"]:
            df = pd.read_excel(uploaded_file)
 
#¿que quieres realizar?

with st.container():
    st.write('---')
    text_column, animation_column= st.columns(2)
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


#subir archivos

def check_date_format(date_str):
    try:
        pd.to_datetime(date_str, format='%Y-%m-%d')
        return True
    except ValueError:
        return False

# Función principal para la aplicación de Streamlit
with st.container():
    st.write('---')
    st.header('¿Qué deseas realizar?')
    st.write('##')

    # Widget para subir archivo
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

    if uploaded_file is not None:
        # Leer el archivo CSV
        file_content = StringIO(uploaded_file.getvalue().decode("utf-8"))
        df = pd.read_csv(file_content)

        # Mostrar el DataFrame cargado
        st.write("Archivo cargado:")
        st.dataframe(df)

        # Verificar formato de las fechas
        date_column = st.selectbox("Selecciona la columna de fecha", df.columns)
        df["Valid_Date_Format"] = df[date_column].apply(check_date_format)

        if df["Valid_Date_Format"].all():
            st.success("Todas las fechas tienen el formato correcto (YYYY-MM-DD).")
        else:
            st.error("Algunas fechas no tienen el formato correcto (YYYY-MM-DD).")
            st.write(df[~df["Valid_Date_Format"]])

#servicios

with st.container():
    st.write('---')
    st.header('Servicios')
    st.write('')

with st.container():
    st.write('---')
    st.write('')
    image_column, text_column=st.columns((2,1))
    with image_column:
        image= Image.open('imagenes/tabla.png')
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader('Dataframe registro de ordenes')
        st.write(
            """
            En el siguiente apartado podrás visualizar en detalle cada orden,
            incluyendo su fecha de inicio y finalización, lugar de partida y destino,
            número del camión que realizó la orden, etiqueta registrada en la caseta,
            proveedor, monto total pagado y monto total presupuestado.
            """
        )
    

with st.container():
    st.write('---')
    st.write('')
    image_column, text_column=st.columns((2,1))
    with image_column:
        image= Image.open('imagenes/graficas.png')
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
    image_column, text_column=st.columns((2,1))
    with image_column:
        image= Image.open('imagenes/ruta.png')
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader('Ruta')
        st.write(
            """
            Visualización detallada de las rutas de cada orden, en este apartado se analizan los
            trayectos específicos desde el punto de partida hasta el destino, 
            incluyendo la duración del viaje y el costo asociado. 
            Esta información te permitirá evaluar la eficiencia de las rutas, 
            identificar posibles áreas de mejora y optimizar los costos operativos. 
            Además, podrás comparar diferentes rutas para encontrar las más rápidas y económicas, 
            contribuyendo a una gestión más eficaz y rentable de las operaciones logísticas.
            """
        )