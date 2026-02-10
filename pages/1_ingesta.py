import streamlit as st
import pandas as pd

from utils.data_processing import (
    apply_numeric_imputation,
    basic_quality_report,
    handle_outliers_iqr,
    read_csv,
)

st.set_page_config(page_title="Modulo 1 - Ingesta", layout="wide")

st.title("Modulo 1 - Ingesta y Procesamiento")

uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is None:
    st.info("Sube un archivo para continuar.")
    st.stop()

try:
    df_raw = read_csv(uploaded_file)
except Exception as exc:
    st.error(f"No se pudo leer el CSV: {exc}")
    st.stop()

if df_raw.empty:
    st.error("El archivo no contiene filas.")
    st.stop()

st.subheader("Vista previa")
with st.expander("Ver datos crudos", expanded=False):
    st.dataframe(df_raw.head(50), use_container_width=True)

st.subheader("Reporte de calidad")
quality = basic_quality_report(df_raw)
with st.expander("Ver reporte de calidad", expanded=False):
    st.dataframe(quality, use_container_width=True)

st.subheader("Opciones de procesamiento")

col1, col2, col3 = st.columns(3)

with col1:
    drop_duplicates = st.checkbox("Eliminar duplicados", value=True)

with col2:
    numeric_cols = df_raw.select_dtypes(include="number").columns.tolist()
    impute_cols = st.multiselect(
        "Columnas numericas a imputar",
        options=numeric_cols,
        default=numeric_cols,
    )
    impute_method = st.selectbox(
        "Metodo de imputacion",
        options=["Media", "Mediana", "Cero"],
        index=0,
    )

with col3:
    outlier_cols = st.multiselect(
        "Columnas numericas para outliers",
        options=numeric_cols,
        default=numeric_cols,
    )
    outlier_strategy = st.selectbox(
        "Tratamiento de outliers",
        options=["Eliminar filas", "Recortar valores"],
        index=0,
    )

apply_button = st.button("Aplicar procesamiento")

if apply_button:
    try:
        df_processed = df_raw.copy()

        if drop_duplicates:
            df_processed = df_processed.drop_duplicates()

        if impute_cols:
            df_processed = apply_numeric_imputation(df_processed, impute_cols, impute_method)

        if outlier_cols:
            df_processed = handle_outliers_iqr(df_processed, outlier_cols, outlier_strategy)

        st.success("Procesamiento aplicado.")
        st.subheader("Datos procesados")
        with st.expander("Ver datos procesados", expanded=False):
            st.dataframe(df_processed.head(50), use_container_width=True)

        st.session_state["processed_df"] = df_processed
        st.session_state["filtered_df"] = df_processed

        csv_bytes = df_processed.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Descargar CSV procesado",
            data=csv_bytes,
            file_name="datos_procesados.csv",
            mime="text/csv",
        )
    except Exception as exc:
        st.error(f"Error al procesar los datos: {exc}")

st.caption("Los datos se mantienen en memoria durante la sesion.")
