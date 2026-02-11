# 📊 Manual del Usuario - Analizador de Datos Inteligente

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Instalación y Configuración](#instalación-y-configuración)
3. [Descripción General](#descripción-general)
4. [Módulo 1: Ingesta y Procesamiento](#módulo-1-ingesta-y-procesamiento)
5. [Módulo 2: Visualización Dinámica](#módulo-2-visualización-dinámica)
6. [Módulo 3: Analista Virtual con IA](#módulo-3-analista-virtual-con-ia)
7. [Columnas Calculadas](#columnas-calculadas)
8. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## Introducción

**Analizador de Datos Inteligente** es una aplicación web interactiva construida con Streamlit que permite:
- 📥 Cargar y procesar archivos CSV
- 📈 Crear visualizaciones dinámicas e interactivas
- 🤖 Generar análisis automático con IA
- 🧮 Calcular métricas derivadas automáticamente

La aplicación está diseñada para analistas de datos, científicos de datos y cualquier persona que necesite explorar y comprender sus datos rápidamente.

---

## Instalación y Configuración

### Requisitos Previos
- Python 3.10+
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto-Final-Fundamentos-de-ciencia-de-datos
   ```

2. **Crear un entorno virtual**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # MacOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

---

## Descripción General

### Estructura de la Aplicación

La aplicación tiene una página principal (home) y tres módulos principales:

```
📊 Analizador de Datos Inteligente
├── 🏠 Home (Página Principal)
├── 📥 Módulo 1: Ingesta y Procesamiento
├── 📈 Módulo 2: Visualización Dinámica
│   ├── Análisis Univariado
│   ├── Análisis Bivariado
│   ├── Reporte
│   ├── Gráficos Adicionales
│   └── Columnas Calculadas
└── 🤖 Módulo 3: Analista Virtual con IA
```

### Navegación

- Usa la **barra lateral izquierda** para navegar entre módulos
- Cada módulo tiene pestañas para diferentes tipos de análisis
- Los datos se comparten automáticamente entre módulos

---

## Módulo 1: Ingesta y Procesamiento

### Objetivo
Cargar, inspeccionar e limpiar tus datos antes del análisis.

### Paso a Paso

#### 1. Cargar un Archivo CSV
- Haz clic en "Sube tu archivo CSV"
- Selecciona el archivo desde tu computadora
- La aplicación detecta automáticamente la codificación (UTF-8 o Latin-1)

#### 2. Revisar Datos Crudos
- En el expander "Ver datos crudos" ves las primeras 50 filas
- Verifica que los datos se hayan cargado correctamente
- Observa los tipos de datos y estructura

#### 3. Inspeccionar Calidad de Datos
- En "Ver reporte de calidad" ves:
  - Columnas con valores faltantes
  - Porcentaje de valores faltantes
  - Tipo de dato de cada columna

#### 4. Configurar Procesamiento

**Opción 1: Eliminar Duplicados**
- ✓ Elimina filas completamente idénticas
- Recomendado: Activar siempre

**Opción 2: Imputación de Datos Faltantes**
- Selecciona columnas numéricas con NaN
- Elige método:
  - **Media**: Usa el promedio de la columna
  - **Mediana**: Usa el valor central (mejor para outliers)
  - **Cero**: Rellena con 0 (para conteos)

**Opción 3: Tratamiento de Outliers**
- Selecciona columnas para análisis de outliers
- Elige estrategia:
  - **Eliminar filas**: Borra registros con outliers
  - **Recortar valores**: Limita outliers al rango IQR

#### 5. Aplicar Procesamiento
- Haz clic en "Aplicar procesamiento"
- Espera a que termine (puede tomar segundos con datasets grandes)
- Verás las nuevas columnas calculadas agregadas automáticamente

#### 6. Descargar Datos Procesados
- Usa "Descargar CSV procesado" para exportar los datos limpios
- Archivo guardado como `datos_procesados.csv`

---

## Módulo 2: Visualización Dinámica

### Objetivo
Explorar datos con visualizaciones interactivas y generar insights.

### Filtros Globales

Todos los gráficos responden a estos filtros:

| Filtro | Tipo | Uso |
|--------|------|-----|
| Rango de fechas | Rango | Analizar período específico |
| Segmento | Multiselect | Analizar por tipo de cliente |
| Categoría | Multiselect | Filtrar por categoría de producto |
| Región | Multiselect | Analizar geografía |
| Subcategoría | Multiselect | Profundizar en categorías |
| Estado | Multiselect | Filtrar por estado (USA) |
| Ciudad | Multiselect | Análisis a nivel ciudad |
| Rango de ventas | Slider | Filtrar por monto de venta |
| Rango de ganancia | Slider | Filtrar por monto de ganancia |

**Tip**: Los multiselects tienen un botón "Todos" para revertir filtros rápidamente.

### Indicadores Clave (KPIs)

Mostrados en tiempo real según los filtros:
- **Ventas**: Suma total de todas las ventas
- **Ganancia**: Ganancia total (Profit)
- **Pedidos**: Cantidad total de órdenes únicas
- **Descuento promedio**: Porcentaje promedio de descuento

### Pestaña 1: Análisis Univariado

Distribuciones individuales de variables:

| Gráfico | Uso |
|---------|-----|
| Distribución de ventas | Ver rango y concentración de ventas |
| Distribución de ganancia | Analizar distribución de ganancias |
| Distribución de descuento | Identificar patrones de descuentos |
| Distribución de cantidad | Ver cantidad de items por orden |

**Interactividad**: Zoom, pan, y exportar como PNG.

### Pestaña 2: Análisis Bivariado

Relaciones entre dos variables:

| Gráfico | Análisis |
|---------|----------|
| Heatmap de correlación | Relaciones numéricas entre variables |
| Ventas vs Ganancia | Relación entre ingresos y ganancias |

**Heatmap**: Verde = correlación positiva, Rojo = negativa

### Pestaña 3: Reporte

Análisis temáticos completos:

1. **Evolución Temporal** (Ventas y Ganancia por mes)
   - Identifica tendencias estacionales
   - Compara meses históricos

2. **Top 10 Productos por Ganancia**
   - Productos más rentables
   - Contribución al resultado total

3. **Mapa por Estado (Ventas)**
   - Visualización geográfica USA
   - Colores indican nivel de ventas
   - Pasa mouse para ver detalles

4. **Ventas y Ganancia por Modo de Envío**
   - Comparación de performance entre modos
   - Identifica modo de envío más rentable

5. **Resumen Estadístico**
   - Cuantitativo: Media, mediana, desviación estándar
   - Categórico: Conteos y moda

### Pestaña 4: Gráficos Adicionales

10 visualizaciones especializadas:

| # | Gráfico | Propósito |
|---|---------|----------|
| 1 | Ganancia por Categoría | Qué categoría gana más |
| 2 | Ganancia por Segmento | Qué segmento de cliente es más rentable |
| 3 | Órdenes por Segmento | Volumen de pedidos por segmento |
| 4 | Descuento vs Ganancia | Impacto de descuentos en ganancia |
| 5 | Top 10 Clientes por Ganancia | Clientes más valiosos |
| 6 | Ciclo de Entrega | Días de envío por modo |
| 7 | Ganancia por Región | Performance regional |
| 8 | Distribución Ganancia/Categoría | Variabilidad por categoría |
| 9 | Ventas: Categoría → Subcategoría | Jerquía de ventas |
| 10 | Ganancia: Segmento vs Región | Matriz de performance |

### Pestaña 5: Columnas Calculadas ⭐

Análisis específico de métricas derivadas:

1. **Distribución del Ticket Promedio**
   - Precio promedio por item vendido

2. **Distribución del Margen de Ganancia (%)**
   - Rentabilidad porcentual

3. **Ticket Promedio vs Margen Ganancia**
   - Relación: productos caros = más margen?

4. **Descuento (Dinero) vs Margen Ganancia**
   - Impacto monetario de descuentos

5. **Ticket Promedio por Categoría**
   - Qué categoría vende items más caros

6. **Margen Ganancia por Segmento**
   - Qué segmento es más rentable

7. **Variabilidad del Ticket Promedio**
   - Box plot por categoría

8. **Evolución del Ticket Promedio (Mensual)**
   - Tendencia temporal

---

## Módulo 3: Analista Virtual con IA

### Objetivo
Generar análisis automático y recomendaciones usando Inteligencia Artificial.

### Requisitos

**Obtener tu Groq API Key:**

1. Visita [console.groq.com](https://console.groq.com)
2. Crea una cuenta (gratis)
3. Ve a "API Keys"
4. Copia tu API Key

### Cómo Usar

1. **Ingresa tu Groq API Key**
   - Campo de contraseña (no se muestra el texto)
   - Se usa solo para esta sesión, no se guarda

2. **Los datos se carga automáticamente**
   - De Módulo 2 si hay filtros aplicados
   - Del Módulo 1 si es la primera vez

3. **Genera el informe**
   - La IA analiza tus datos
   - Tarda 10-30 segundos
   - Espera el spinner "Generando informe..."

### Contenido del Informe

El análisis genera 6 secciones:

```
📋 INFORME GENERADO POR IA
├── 1. Resumen Ejecutivo
│   └── Overview de hallazgos clave
├── 2. Análisis Descriptivo
│   └── Estadísticas y distribuciones
├── 3. Tendencias Identificadas
│   └── Patrones temporales y comportamientos
├── 4. Oportunidades de Negocio
│   └── Áreas de crecimiento potencial
├── 5. Riesgos Identificados
│   └── Alertas y problemas potenciales
└── 6. Recomendaciones Accionables
    └── Pasos específicos a tomar
```

### Ejemplo de Prompts

El sistema construye automáticamente prompts detallados como:

```
"Eres un analista de datos senior...

Dataset Information:
- Total registros: 9,994
- Período: 2015-2017
- Columnas: 21 (ventas, ganancias, categorías, etc.)

Columnas: Row ID, Order Date, Sales, Profit, Quantity...

Summary Statistics:
Sales: μ=229.86, σ=623.17
Profit: μ=28.66, σ=234.18
...

Generate a professional report with these sections:
1. Executive Summary
2. Descriptive Analysis
3. Identified Trends
..."
```

---

## Columnas Calculadas

La aplicación crea automáticamente 3 columnas derivadas:

### 1. Ticket Promedio
**Fórmula**: `Sales / Quantity`
**Rango de ejemplo**: $50 - $500 por item

**Interpretar**:
- Valores altos = productos premium
- Valores bajos = productos de volumen
- Varianza = mezcla de productos

**Uso**: Segmentación de clientes, estrategia de precios

### 2. Margen Ganancia (%)
**Fórmula**: `(Profit / Sales) * 100`
**Rango de ejemplo**: -100% a +80%

**Interpretar**:
- Positivo = ganancia
- Negativo = pérdida
- 0-10% = margen bajo
- 20%+ = margen excelente

**Uso**: Identificar productos poco rentables, decisiones de descuentos

### 3. Descuento Dinero
**Fórmula**: `Sales * Discount`
**Rango de ejemplo**: $0 - $100+

**Interpretar**:
- Cuánto dinero se "deja" con cada descuento
- Multiplicador de descuento %

**Uso**: Control de cost de promociones, análisis de impacto

---

## Flujo de Trabajo Recomendado

### Análisis Completo (15 minutos)

```
1. MÓDULO 1 (3 min)
   ├── Cargar CSV
   ├── Revisar datos crudos
   ├── Revisar reporte de calidad
   ├── Aplicar procesamiento
   └── Descargar (opcional)
   
2. MÓDULO 2 (10 min)
   ├── Explorar Análisis Univariado
   ├── Revisar Análisis Bivariado
   ├── Verificar Reporte
   ├── Analizar Gráficos Adicionales
   └── Profundizar en Columnas Calculadas
   
3. MÓDULO 3 (2 min)
   ├── Generar informe con IA
   ├── Leer recomendaciones
   └── Tomar decisiones
```

### Quick Stats (5 minutos)

Solo necesitas KPIs y un gráfico:
1. Módulo 2 → Filtrar datos
2. Leer KPIs (Ventas, Ganancia, Pedidos)
3. Ver cualquier tab según tu interés

---

## Solución de Problemas

### "Error al leer el CSV"
**Causa**: Codificación no soportada
**Solución**: 
- Abre el CSV en Excel
- Guarda como "CSV UTF-8" o "CSV ANSI"
- Reintentar carga

### "ModuleNotFoundError: statsmodels"
**Causa**: Paquete faltante
**Solución**:
```bash
pip install statsmodels
```

### "No se visualiza un gráfico"
**Causa**: Datos insuficientes o filtro sin resultados
**Solución**:
- Revisar filtros
- Cambiar a "Todos" en multiselects
- Probar con otro período

### "La API Key no funciona"
**Causa**: Key expirada, inválida o sin créditos
**Solución**:
- Verificar en console.groq.com
- Verificar que esté activada
- Generar nueva si es necesario

### "Los datos no cambian con filtros"
**Causa**: Caché del navegador
**Solución**:
- Recarga la página (F5 o Ctrl+R)
- Limpia caché del navegador

---

## Características Avanzadas

### Exportar Gráficos
- Hover en la esquina superior derecha del gráfico
- Haz clic en 📷 (camera icon)
- Se descarga como PNG

### Hover Information
- Pasa mouse sobre puntos de datos
- Ver detalles como:
  - Valores exactos
  - Categorías
  - Cantidades

### Zoom y Pan
- **Zoom**: Dibuja un rectángulo con mouse
- **Reset**: Home button en toolbar superior
- **Pan**: Click y arrastra

### Resetear Session
- Si algo se comporta raro:
  ```
  Settings ⚙️ → Clear Cache → Clear All
  ```

---

## Límites y Consideraciones

| Aspecto | Límite | Nota |
|--------|--------|------|
| Tamaño de archivo | ~100 MB | Depende de RAM |
| Filas de data | 1M+ | Performance puede disminuir |
| Columnas mostradas | 30 | UI se vuelve abarrotada |
| Sesión activa | 2 horas | Después recarga app |
| Groq API calls | 30/min | Plan free |

---

## Contacto y Soporte

### Reportar Errores
Si encuentras un error:
1. Anota el mensaje de error exacto
2. Describe qué estabas haciendo
3. Intenta reproducir
4. Contacta al desarrollador

### Mejoras Sugeridas
¿Ideas para mejorar? Comunícalas con:
- Descripción clara de la feature
- Caso de uso
- Beneficio esperado

---

## Glosario

| Término | Definición |
|---------|-----------|
| **KPI** | Key Performance Indicator - métrica clave |
| **Outlier** | Valor anormalmente alto o bajo |
| **IQR** | Rango Intercuartil (Q3-Q1) |
| **Correlación** | Relación entre dos variables |
| **Margen** | Diferencia entre ingreso y costo |
| **Ticket** | Valor promedio de transacción |
| **Segmento** | Grupo de clientes o productos |
| **Imputación** | Llenar valores faltantes |

---

## Changelog

### Versión 1.0 (Feb 2026)
- ✅ Módulo 1: Ingesta y procesamiento
- ✅ Módulo 2: Visualización con 5 tabs
- ✅ Módulo 3: Análisis con IA (Groq)
- ✅ Columnas calculadas automáticas
- ✅ Filtros globales avanzados
- ✅ 10 gráficos especializados
- ✅ Manejo robusto de errores

---

## Documentos Relacionados

- `README.md` - Información técnica y instalación
- `requirements.txt` - Dependencias del proyecto
- `CHANGELOG.md` - Historial de versiones

---

**Última actualización**: Febrero 2026
**Versión**: 1.0
**Autor**: AI Assistant

*¡Gracias por usar el Analizador de Datos Inteligente! 📊*
