import streamlit as st

st.set_page_config(
    page_title="Proyecto Final - App de Datos",
    page_icon="📊",
    layout="wide",
)

st.title("App de Analisis de Datos")

st.markdown(
    """
    Esta aplicacion esta organizada en tres modulos:

    1. Ingesta y procesamiento de datos.
    2. Visualizacion dinamica con filtros globales.
    3. Analista virtual con IA (Groq).

    Usa el menu lateral para navegar.
    """
)

st.info("Sube un CSV en el modulo 1 para empezar.")
