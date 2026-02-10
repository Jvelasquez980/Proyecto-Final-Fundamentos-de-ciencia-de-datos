import streamlit as st
from groq import Groq

st.set_page_config(page_title="Modulo 3 - IA", layout="wide")

st.markdown(
    """
    <style>
    .module-header {
        font-size: 2.5rem;
        font-weight: 900;
        color: #667eea;
        text-shadow: 1px 1px 2px rgba(118, 75, 162, 0.2);
        margin-bottom: 1rem;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="module-header">🤖 Modulo 3 - Analista Virtual con IA</div>', unsafe_allow_html=True)

if "filtered_df" in st.session_state:
    base_df = st.session_state["filtered_df"]
elif "processed_df" in st.session_state:
    base_df = st.session_state["processed_df"]
else:
    base_df = None
if base_df is None:
    st.info("Primero carga y procesa datos en los modulos anteriores.")
    st.stop()

api_key = st.text_input("Ingresa tu Groq API Key", type="password")

if not api_key:
    st.warning("Debes ingresar una Groq API Key para continuar.")
    st.stop()

model = "llama-3.3-70b-versatile"

summary = base_df.describe(include="all").transpose().fillna("")

prompt = f"""
Eres un analista de datos experto. Tu tarea es generar un informe completo y detallado de análisis de datos en español.

### Información del Dataset

**Características generales:**
- Total de registros: {len(base_df)}
- Total de columnas: {len(base_df.columns)}
- Columnas disponibles: {', '.join(base_df.columns)}

**Resumen estadístico:**
{summary.to_string()}

### Estructura del Informe Requerido

Genera un informe profesional en Markdown con las siguientes secciones en orden:

### Resumen Ejecutivo
- Descripción general y propósito del dataset
- Tamaño, composición y alcance de los datos
- Período de tiempo cubierto (si aplica)

### Análisis Descriptivo
- Estadísticas clave de variables numéricas (media, mediana, desviación estándar, rangos)
- Distribuciones principales de variables categóricas
- Valores faltantes o datos incompletos

### Tendencias e Insights Identificados
- Patrones principales observados en los datos
- Correlaciones relevantes entre variables
- Comportamientos anómalos o excepciones notables
- Evolución temporal (si aplica)

### Oportunidades de Negocio
- Segmentos identificados con alto potencial
- Oportunidades de crecimiento o mejora
- Recomendaciones de enfoque estratégico
- Ventajas competitivas identificadas

### Riesgos y Problemas
- Áreas críticas o de preocupación
- Datos atípicos, outliers o anomalías
- Posibles problemas de calidad en los datos
- Limitaciones identificadas

### Recomendaciones Accionables
- Acciones prioritarias ordenadas por impacto
- Métricas clave a monitorear continuamente
- Próximos pasos sugeridos para profundizar
- Timeline recomendado para implementación

### Estándares de Calidad

- Mantén un tono profesional y ejecutivo
- Sé específico con números, porcentajes y estadísticas
- Utiliza tablas y comparativas cuando sea pertinente
- Justifica cada recomendación con datos
- Evita jerga técnica innecesaria
- Formatea el documento en Markdown limpio y bien estructurado
"""

if st.button("Generar informe con IA"):
    with st.spinner("Generando informe..."):
        client = Groq(api_key=api_key)
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Eres un analista de datos senior especializado en generar reportes profesionales."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
                max_tokens=2000,
            )
            content = response.choices[0].message.content
            st.subheader("📊 Informe de Análisis")
            st.markdown(content)
        except Exception as exc:
            st.error(f"Error al llamar a la API de Groq: {exc}")
