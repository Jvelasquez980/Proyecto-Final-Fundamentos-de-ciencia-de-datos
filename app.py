import streamlit as st

st.set_page_config(
    page_title="Proyecto Final - App de Datos",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        filter: drop-shadow(2px 2px 2px rgba(102, 126, 234, 0.3));
    }
    .subtitle {
        font-size: 1.3rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .feature-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 1rem;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
    }
    .feature-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 0.5rem;
    }
    .feature-desc {
        color: #666;
        font-size: 0.95rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-header">📊 Analizador de Datos Inteligente</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Una plataforma completa para explorar, visualizar y analizar tus datos con IA</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📥 Módulo 1", "Ingesta", "CSV")
with col2:
    st.metric("📈 Módulo 2", "Visualización", "Filtros")
with col3:
    st.metric("🤖 Módulo 3", "IA", "Groq")

st.divider()

st.markdown(
    """
    ### ¿Cómo empezar?
    
    Esta aplicación está organizada en **4 módulos principales**:
    """,
)

st.markdown(
    """
    <div class="feature-box">
        <div class="feature-title">📥 Módulo 1: Ingesta y Procesamiento</div>
        <div class="feature-desc">
            Sube tu archivo CSV y aplica transformaciones:
            • Eliminación de duplicados
            • Imputación de valores (Media, Mediana, Cero)
            • Detección y tratamiento de outliers
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="feature-box">
        <div class="feature-title">📈 Módulo 2: Visualización Dinámica</div>
        <div class="feature-desc">
            Explora tus datos con filtros globales y gráficos interactivos:
            • Filtros por fecha, categoría, región, estado y ciudad
            • Análisis univariado, bivariado y temporal
            • Mapa geográfico de ventas
            • KPIs en tiempo real
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="feature-box">
        <div class="feature-title">🤖 Módulo 3: Analista Virtual con IA</div>
        <div class="feature-desc">
            Genera informes profesionales con el modelo Llama 3.3:
            • Análisis descriptivo automático
            • Identificación de tendencias y oportunidades
            • Detección de riesgos
            • Recomendaciones accionables
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

st.markdown(
    """
    ### 🚀 Próximos pasos
    1. Ve a **Módulo 1** y sube tu archivo CSV
    2. Aplica el procesamiento necesario
    3. Explora los datos en **Módulo 2**
    4. Genera un informe con IA en **Módulo 3**
    """,
)

st.info(
    "💡 **Tip:** Usa el menú lateral para navegar entre módulos. Los datos se mantienen en memoria durante tu sesión.",
)
