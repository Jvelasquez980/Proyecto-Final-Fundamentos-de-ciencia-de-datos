# Proyecto-Final-Fundamentos-de-ciencia-de-datos

## Descripcion del problema

Una empresa de retail necesita entender el desempeño de sus ventas para
identificar tendencias, productos rentables, regiones con alto potencial y
segmentos con riesgo. Este proyecto ofrece una app interactiva para explorar
el dataset de ventas, aplicar filtros y generar insights con IA.

## Instalacion

1. Clona este repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Entra a la carpeta del proyecto:

```bash
cd Proyecto-Final-Fundamentos-de-ciencia-de-datos
```

3. Crea y activa un entorno virtual (opcional):

```bash
python -m venv .venv
```

4. Instala dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecuta la aplicacion:

```bash
streamlit run app.py
```

Si usas la funcionalidad de IA, ingresa tu Groq API Key directamente en el
modulo de IA.

## Módulos de la Aplicación

### 📥 Módulo 1: Ingesta y Procesamiento
- Sube archivos CSV
- Detection de duplicados
- Imputación de valores numéricos (Media, Mediana, Cero)
- Tratamiento de outliers (Eliminar o Recortar)
- Descarga de datos procesados

### 📈 Módulo 2: Visualización Dinámica
- Filtros globales por fecha, categoría, región, estado y ciudad
- Sliders de ventas y ganancia
- KPIs en tiempo real

**Tab 1 - Análisis Univariado:**
- Distribuciones (Histogramas)
- Boxplots de descuento y cantidad

**Tab 2 - Análisis Bivariado:**
- Matriz de correlaciones (Heatmap)
- Scatter plot: Ventas vs Ganancia

**Tab 3 - Reporte:**
- Evolución temporal de ventas y ganancia
- Top 10 productos por ganancia
- Mapa coropletico de ventas por estado
- Análisis de envios por modo
- Resumen estadístico

**Tab 4 - Gráficos Adicionales:**
1. Ganancia por Categoría
2. Ganancia por Segmento
3. Cantidad de Órdenes por Segmento
4. Análisis: Descuento vs Ganancia
5. Top 10 Clientes por Ganancia
6. Ciclo de Entrega por Modo de Envío
7. Ganancia por Región
8. Distribución de Ganancia por Categoría
9. Treemap: Ventas por Categoría y Subcategoría
10. Heatmap: Ganancia por Segmento vs Región

### 🤖 Módulo 3: Analista Virtual con IA
- Integración con API de Groq (LLaMA 3.3-70B)
- Ingreso seguro de API Key
- Generación de informes profesionales con 6 secciones:
  - Resumen Ejecutivo
  - Análisis Descriptivo
  - Tendencias Identificadas
  - Oportunidades de Negocio
  - Riesgos y Problemas
  - Recomendaciones Accionables

## Link al despliegue

https://proyecto-final-fundamentos-de-ciencia-de-datos-6eehmrmw6btxn98.streamlit.app
## Creditos

- Autor: Jeronimo Velasquez Escobar y Manuela Caro Villada
- Fuente de datos: Sample Superstore (Kaggle)