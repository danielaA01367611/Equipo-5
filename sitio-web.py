import streamlit as st
from PIL import Image

st.set_page_config(page_title='TDR transportes', page_icon='🚚', layout='wide')

#inicio
with st.container():
    st.header('TDR transportes portal del pago de casetas 🚚')
    st.title('La grandeza de TDR es gracias a la grandeza de su gente')
    st.write('Somos TDR, trabajando siempre en la creación e implementación de soluciones integrales de transporte, rentables, eficientes e innovadoras')
    st.write('[Saber más >] (https://www.tdr.com.mx/cultura.html)')

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

#servicios

with st.container():
    st.write('---')
    st.header('Servicios')
    st.write('')
    image_column, text_column=st.columns((2,1))
    with image_column:
        image= Image.open('imagenes/sitio-web.png')
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader('Dataframe registro de ordenes')
        st.write(
            """"
            Detalle de cada orden
            """
        )
    

with st.container():
    st.write('---')
    st.header('Servicios')
    st.write('')
    image_column, text_column=st.columns((2,1))
    with image_column:
        image= Image.open('imagenes/sitio-web.png')
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader('Dataframe registro de ordenes')
        st.write(
            """"
            Detalle de cada orden
            """
        )