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

#Consumo de datos para el sidebar Top 10 Delitos
topDelitos = []

with open("resources/Reporte-Tipos-Delitos.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            Delito=str(row[0])
            Promedio=row[1]
            topDelitos.append( [Delito,Promedio] )
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

if(selected == "Noticias"):
    # Redirigir automáticamente después de 5 segundos
    redirect_url = "#noticias-destacadas"
    st.markdown(f'<meta http-equiv="refresh" content="url={redirect_url}">', unsafe_allow_html=True)


with st.sidebar:#Top Delitos
    st.write("<h2>Top 10 - Los tipos de delitos más comunes en el estado</h2>", unsafe_allow_html=True)
    for delito in topDelitos:
        st.write(f"<h2>{delito[0]}</h2>", unsafe_allow_html=True)
        st.write(delito[1])

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
    st.write("<h1>Mapas de Calor de Crimenes Del Estado de Nuevo Leon</h1>", unsafe_allow_html=True)
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
    st.write("<h1>Noticias Destacadas</h1>", unsafe_allow_html=True)

    # Primera fila de cartas
    st.write("<div class='row'>", unsafe_allow_html=True)
    with st.container():
        # Carta 1
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://images.telediario.mx/J5sbQmzQShvLpSRe7BYak04pv6w=/958x596/uploads/media/2023/03/31/asesinan-balazo-cabeza-hombre-pelear.jpeg", width=300)
        st.write("<h2>Hombre dispara contra fachada de Secretaría de Seguridad en China, Nuevo León</h2>", unsafe_allow_html=True)
        st.write(
            """
            Hombres armados dispararon contra la fachada del edificio de la Secretaría de Seguridad Pública del municipio de China, Nuevo León.
            El ataque se reportó cerca de las 19:50 horas del martes, en el edificio ubicado sobre la calle Hidalgo. 
            """)
        st.button("Leer más", "btnArt1")
        st.write("</div>", unsafe_allow_html=True)
    with st.container():
        # Carta 2
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://cdn2.excelsior.com.mx/media/styles/image800x600/public/pictures/2023/05/04/2944216.jpg", width=300)
        st.write("<h2>Grupo armado roba 10 mdp a empleados de empresa de seguridad en Nuevo León</h2>", unsafe_allow_html=True)
        st.write(
            """
            Un grupo armado despojó un total de 10 millones de pesos a empleados de una empresa de seguridad en el cruce de las calles Diego de Montemayor y Pedro Noriega, en la colonia Terminal del municipio de Monterrey, Nuevo León.
            """)
        st.button("Leer más", "btnArt2")
        st.write("</div>", unsafe_allow_html=True)

    with st.container():
        # Carta 3
        st.write("<div class='card'>", unsafe_allow_html=True)
        st.image("https://seguridad.sspc.gob.mx/uploads/portadas/thumbs/71c00570-4161-4927-8204-c83ac2552a1d-crop.jpg", width=300)
        st.write("<h2>Guardia Nacional localiza 11 tomas clandestinas utilizadas para sustracción ilegal de hidrocarburo</h2>", unsafe_allow_html=True)
        st.write(
            """
            En el marco del plan conjunto para combatir el robo de hidrocarburo, en los estados de Hidalgo y Nuevo León, elementos de la Guardia Nacional (GN) localizaron 11 tomas clandestinas, aparentemente utilizadas para la sustracción ilegal de combustible, y aseguraron un vehículo que contenía bidones cargados con aparente huachicol.
            """)
        st.button("Leer más", "btnArt3")
        st.write("</div>", unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)

    

    