import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

#Funcion para animación
def load_lottieurl(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None
    
    return r.json()

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_0os5xmbh.json")
image_security = Image.open("assets/Image/hero-svg.png")

with st.container():
    st.subheader("Hola bienvenido!")
    st.title("SafeZoneConnect")
    left_column, rigth_column = st.columns(2)
    with left_column:
        st.write(
            """
            ¡Bienvenido a nuestra plataforma de seguridad ciudadana en línea! En nuestro compromiso por mejorar la calidad 
            de vida y reducir la tasa de delitos en nuestro país, te ofrecemos una herramienta poderosa para mantenerte
            informado y protegido.
            """
            )
        st.write("[Ver mas >](#descubre-lo-que-pasa-cerca-de-ti)")

    with rigth_column:
        #st_lottie(lottie_coding, height=500, key="coding")
        st.image(image_security)

with st.container():
    st.write("---")
    st.subheader("Descubre lo que pasa cerca de ti!")
    st.write("La seguridad en tus manos: Accede, comparte, protege")
    st.write("[Noticias >](http://datos.nl.gob.mx/n-l-delitos-por-tipo-por-cada-100-mil-habitantes/)")
