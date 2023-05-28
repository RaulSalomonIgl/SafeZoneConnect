import streamlit as st
import requests
import pandas as pd
import numpy as np
import csv

from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
from map import Map

st.set_page_config(layout="wide")
#Consumo de datos para el mapa de calor
delitos = []
lstCords = []

with open("resources/Delitos_Municipio.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            Delito=str(row[0])
            Municipio=str(row[1])
            Cantidad=int(row[2])
            Longitud=float(row[3])
            Latitud= float(row[4])
            delitos.append( [Delito,Municipio,Cantidad,Longitud,Latitud] )
        line_count += 1
    print(f'Processed {line_count} lines.')

#Funcion para animación
def load_lottieurl(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None
    
    return r.json()

#Local Css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("./assets/css/main.css")


lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_0os5xmbh.json")
image_security = Image.open("assets/Image/hero-svg.png")

selected = option_menu(
    menu_title=None,
    options=["Inicio", "Noticias", "Comunidad", "Asesoria"],
    icons=["house", "newspaper", "chat-dots", "file-medical"],
    menu_icon="shield",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"top": "0", "z-index": "9999"},
        "nav-link": {
            "--hover-color": "#FF4B4B"
        }
    }
)

if(selected == "Inicio"):
    # Redirigir automáticamente después de 5 segundos
    redirect_url = "#safezoneconnect"
    st.markdown(f'<meta http-equiv="refresh" content="url={redirect_url}">', unsafe_allow_html=True)

elif(selected == "Noticias"):
    # Redirigir automáticamente después de 5 segundos
    redirect_url = "#descubre-lo-que-pasa-cerca-de-ti"
    st.markdown(f'<meta http-equiv="refresh" content="url={redirect_url}">', unsafe_allow_html=True)

with st.container(): #Inicio
    st.write("""<h1 class="title-hero">SafeZoneConnect</h1>""", unsafe_allow_html=True)
    left_column, rigth_column = st.columns(2)
    with left_column:
        st.write(
            """
            <p class="txt-hero">¡Bienvenido a nuestra plataforma de seguridad ciudadana en línea! En nuestro compromiso por mejorar la calidad 
            de vida y reducir la tasa de delitos en nuestro país, te ofrecemos una herramienta poderosa para mantenerte
            informado y protegido.
            Únete a nuestra plataforma y descubre cómo la tecnología puede marcar la diferencia en la seguridad pública. Estamos comprometidos en brindarte una experiencia confiable, intuitiva y orientada a tu bienestar. Tu seguridad es nuestra prioridad.

            ¡Comienza ahora y ayuda a crear un entorno más seguro para todos!"</p>
            """,
            unsafe_allow_html=True
            )
        st.write('<a class="btn btn-primary" href="#descubre-lo-que-pasa-cerca-de-ti">Ver más ></a>', unsafe_allow_html=True)

    with rigth_column:
        #st_lottie(lottie_coding, height=500, key="coding")
        st.image(image_security)
with st.container(): #Mapa de calor
    st.title("Mapas de Calor de Crimenes Del Estado de Nuevo Leon")
    for i in range( 0, len(delitos)-1 ):
        Map.getPoints(delitos[i][4], delitos[i][3], delitos[i][2], lstCords)

    df = pd.DataFrame(
        lstCords,
        columns=['lat', 'lon'])
    
    st.map(df)

    left_column, rigth_column = st.columns(2)
    with left_column:
        st.write("Descubre la distribución y concentración de crímenes en el estado de Nuevo León con nuestro mapa de calor interactivo. Visualiza de manera intuitiva las áreas donde se han reportado incidentes delictivos, permitiéndote tener una visión clara de la seguridad en diferentes localidades.")
    with rigth_column:
        st.write("Nuestro mapa de calor de crímenes en Nuevo León te ofrece una herramienta poderosa para mejorar tu conciencia de seguridad y tomar decisiones informadas. Únete a nuestra comunidad comprometida con la prevención del delito y contribuye a crear entornos más seguros para todos.")

with st.container(): #Noticias
    st.write("---")
    # Título de la sección
    st.title("Noticias Destacadas")
    left_column, center_column, rigth_column = st.columns(3)

    # Primera fila de cartas
    st.write("<div class='row'>", unsafe_allow_html=True)
    with left_column:
        # Carta 1
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://images.telediario.mx/J5sbQmzQShvLpSRe7BYak04pv6w=/958x596/uploads/media/2023/03/31/asesinan-balazo-cabeza-hombre-pelear.jpeg", width=300)
        st.write("Título de la Noticia 1")
        st.write("Contenido de la noticia 1")
        st.button("Leer más", "btnArt1")
        st.write("</div>", unsafe_allow_html=True)
    with center_column:
        # Carta 2
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://images.telediario.mx/J5sbQmzQShvLpSRe7BYak04pv6w=/958x596/uploads/media/2023/03/31/asesinan-balazo-cabeza-hombre-pelear.jpeg", width=300)
        st.write("Título de la Noticia 2")
        st.write("Contenido de la noticia 2")
        st.button("Leer más", "btnArt2")
        st.write("</div>", unsafe_allow_html=True)
    with rigth_column:
        # Carta 3
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://images.telediario.mx/J5sbQmzQShvLpSRe7BYak04pv6w=/958x596/uploads/media/2023/03/31/asesinan-balazo-cabeza-hombre-pelear.jpeg", width=300)
        st.write("Título de la Noticia 3")
        st.write("Contenido de la noticia 3")
        st.button("Leer más", "btnArt3")
        st.write("</div>", unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)

    # Segunda fila de cartas
    st.write("<div class='row'>", unsafe_allow_html=True)
    with left_column:
        # Carta 4
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://images.telediario.mx/J5sbQmzQShvLpSRe7BYak04pv6w=/958x596/uploads/media/2023/03/31/asesinan-balazo-cabeza-hombre-pelear.jpeg", width=300)
        st.write("Título de la Noticia 4")
        st.write("Contenido de la noticia 4")
        st.button("Leer más", "btnArt4")
        st.write("</div>", unsafe_allow_html=True)
    with center_column:
        # Carta 5
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://images.telediario.mx/J5sbQmzQShvLpSRe7BYak04pv6w=/958x596/uploads/media/2023/03/31/asesinan-balazo-cabeza-hombre-pelear.jpeg", width=300)
        st.write("Título de la Noticia 5")
        st.write("Contenido de la noticia 5")
        st.button("Leer más", "btnArt5")
        st.write("</div>", unsafe_allow_html=True)
    with rigth_column:
        # Carta 6
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://images.telediario.mx/J5sbQmzQShvLpSRe7BYak04pv6w=/958x596/uploads/media/2023/03/31/asesinan-balazo-cabeza-hombre-pelear.jpeg", width=300)
        st.write("Título de la Noticia 6")
        st.write("Contenido de la noticia 6")
        st.button("Leer más", "btnArt6")
        st.write("</div>", unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)

    