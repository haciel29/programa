import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


#config
st.set_page_config(page_title="taller mecanico", page_icon="👨‍🔧", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
email_address ="emailcontact@gmail.com"

lottie_file ="https://lottie.host/02ac28ca-3c63-45ad-be15-4394d34c0230/NqoJMa3okg.json"

with st.container():
    st.subheader("Hola, somos un taller mecanico:🙋‍♂️:")
    st.title("Creamos soluciones para reparar tu auto")
    st.write(
        "somos unos apacionadaos de los autos especializados en las reparaciones, nos gusta solucionar los problemas de tu auto"
    )



# sobre nosotros
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Sobre nosotros")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a tu auto a traves de un buen servicio que sea el necesario para tu auto, temas en los que te podemos ayudar son:

            - tienes un carro y quieres mejorar sus servicios 
            - si tu carro es automatico y no hace bien su funcion
            - No tienes claras las fallas de tu auto
            - Quieres mejorar la experiencia de tus servicios

            ***Si esto te es interesante puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """
        )

    with right_column:
        st_lottie(load_lottieurl(lottie_file), height=400)

# servicios
with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/servicio.jpg")
        st.image(image, use_container_width=True)
    with text_column:
        st.subheader("servicios")
        st.write(
            """
            Si deseas servicio de frenos, servicio de transmicione (automatica o estandar), afinacion de tu auto  
            """
        )


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/motor.jpg")
        st.image(image, use_container_width=True)
    with text_column:
        st.subheader("reparacion de motores")
        st.write(
            """
            _si tu auto sufrio un calentamiento y necesita reparacion de culata
            _si tu auto se quedo sin aceite y se necesita reparar
            """
        )


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/caja.png")
        st.image(image, use_container_width=True)
    with text_column:
        st.subheader("reparacion de transmiciones automaticas")
        st.write(
            """
            si tu auto es automatico y no hace sus funciones adecuadamente y necesita repararse.
            """
        )


# contacto
with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros!")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
