import streamlit as st
from PIL import Image
import pandas as pd
from io import StringIO
import plotly.express as px
from datetime import datetime


st.set_page_config(page_title='TDR transportes', page_icon='🚚', layout='wide')
email_contact = 'tu_correo@example.com'
st.sidebar.image('imagenes/logo.png', use_column_width=True)
dashboard_mode=st.sidebar.radio('Seleccionar el dashboard a visualizar', ('Tabla', 'Gráficos', 'Rutas'))
rutas_df=None
#inicio
with st.container():
    def crop_image(image_path, crop_box):
        image = Image.open(image_path)
        cropped_image = image.crop(crop_box)
        return cropped_image
    
    header_image_path = 'imagenes/TDR 2.jpeg'
    crop_box = (50, 300, 800, 500)  # Ajusta estos valores según sea necesario (left, upper, right, lower)
    header_image = crop_image(header_image_path, crop_box)
    st.image(header_image, use_column_width=True)
    st.header('TDR transportes portal del pago de casetas 🚚')
    st.title('La grandeza de TDR es gracias a la grandeza de su gente')
    st.write('Somos TDR, trabajando siempre en la creación e implementación de soluciones integrales de transporte, rentables, eficientes e innovadoras.')
    st.write('[Saber más >] (https://www.tdr.com.mx/index.html)')

 
#¿que quieres realizar?

with st.container():
    st.write('---')
    text_column, animation_column= st.columns(2)
    with text_column:
        st.header('¿Qué puedes hacer en este portal? 🔍')
        st.write(
                """
            El objetivo de este portal es corroborar el costo acumulado de casetas por número de orden según el número el camión.
            Aquí puedes visualizar: 

            - Fechas de inicio y fin de las ordenes

            - Ciudad de origen y ciudad destino de las ordenes

            - Total acumulado pagado en casetas por orden

            - Número de camión que completó la orden

            - Presupuesto del pago total de casetas por ruta

            - Representaciones visuales de las ordenes

            """
        )
    with animation_column:
        st.empty()

#botón de email
with st.container():
    st.write('---')
    st.header('¿Qué deseas realizar?')
    st.write('##')
    contact_form=f"""
    <form action='https://formsubmit.co/{email_contact}' method='POST'>
    <input type='text' name='name' placeholder='Tu nombre' required>
    <input type='email' name='email' placeholder='Tu email' required>
    <textarea type='email' name='message' placeholder='Tu mensaje aqui' required></textarea>
    <button type='submit'>Enviar</button>
    </from>
    """
    left_column, rigth_column= st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with rigth_column:
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