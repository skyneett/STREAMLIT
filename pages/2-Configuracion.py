import streamlit as st

# Título
st.title("Mi primera app con Streamlit 🚀")

# Texto
st.write("Hola, esta es una aplicación sencilla creada con Streamlit")

# Entrada de usuario
nombre = st.text_input("¿Cómo te llamas?")

if nombre:
    st.success(f"Hola {nombre}, ¡bienvenido/a!")

# Slider
edad = st.slider("Selecciona tu edad", 0, 100, 18)
st.write(f"Tienes {edad} años")

# Botón
if st.button("Saludar"):
    st.write("¡Hola! 👋")

# Imagen
st.image("https://via.placeholder.com/300", caption="Imagen de ejemplo")

# Gráfico simple
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(data)
