# Datasets Recomendados para Proyecto Final - Fundamentos de Ciencia de Datos
## Universidad EAFIT 2026-1

---

## 📋 Verificación de Requisitos del Proyecto

Antes de presentar las opciones, recordemos los **requisitos obligatorios**:

### ✅ Criterios Técnicos
- **Volumen:** Mínimo 1,000 registros (filas)
- **Dimensionalidad:** Mínimo 10 columnas con:
  - Variables Numéricas (Continuas/Discretas)
  - Variables Categóricas (Nominales/Ordinales)
  - Variables Booleanas y/o Temporales (Fechas)
- **Estado:** Dataset con imperfecciones (nulos, outliers, inconsistencias)

### 🎯 Preguntas de Negocio
El dashboard debe responder 3 preguntas estratégicas del dominio elegido.

---

## 🏆 DATASETS ALTAMENTE RECOMENDADOS

### **1. IBM HR Analytics - Employee Attrition & Performance** ⭐ TOP PICK

**URL:** https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

#### ✅ Cumplimiento de Requisitos
- **Registros:** 1,470 empleados
- **Columnas:** 35 variables
- **Variables Numéricas:** Age, DailyRate, DistanceFromHome, MonthlyIncome, YearsAtCompany, etc. (15+)
- **Variables Categóricas:** Department, JobRole, MaritalStatus, EducationField, etc. (10+)
- **Variables Booleanas:** Attrition (Yes/No), OverTime (Yes/No)
- **Imperfecciones:** Dataset limpio pero permite simular valores nulos para práctica de limpieza

#### 🎯 Preguntas de Negocio Sugeridas
1. **¿Qué factores correlacionan más con la deserción de empleados (Attrition)?**
2. **¿Cómo impacta la distancia del hogar y el nivel salarial en la satisfacción laboral?**
3. **¿Existe relación entre las horas extra y el equilibrio vida-trabajo con la rotación de personal?**

#### 💡 Ventajas para el Proyecto
- Dominio ampliamente conocido (Recursos Humanos)
- Perfecta para análisis de clasificación binaria
- Múltiples dimensiones para feature engineering (ej: Ratio Salario/Experiencia)
- Alta complejidad estadística con correlaciones interesantes
- Excelente para visualizaciones con Plotly (distribuciones por departamento, género, etc.)

---

### **2. Telco Customer Churn**

**URL:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn

#### ✅ Cumplimiento de Requisitos
- **Registros:** 7,043 clientes
- **Columnas:** 21 variables
- **Variables Numéricas:** tenure, MonthlyCharges, TotalCharges
- **Variables Categóricas:** Contract, PaymentMethod, InternetService, etc.
- **Variables Booleanas:** Churn, PhoneService, PaperlessBilling, etc.
- **Imperfecciones:** Contiene valores nulos en TotalCharges, formatos inconsistentes

#### 🎯 Preguntas de Negocio Sugeridas
1. **¿Qué factores correlacionan más con la deserción de clientes (Churn)?**
2. **¿Cómo afecta el tipo de contrato y método de pago a la retención de clientes?**
3. **¿Cuál es el perfil de cliente de alto riesgo de abandono?**

#### 💡 Ventajas para el Proyecto
- Problema clásico de negocio (retención de clientes)
- Datos reales de compañía de telecomunicaciones
- Perfecto para demostrar limpieza de datos (TotalCharges tiene valores ' ')
- Gran potencial para feature engineering (ej: Ticket Promedio = TotalCharges/tenure)

---

### **3. Superstore Sales Dataset**

**URL:** https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

#### ✅ Cumplimiento de Requisitos
- **Registros:** ~9,994 transacciones
- **Columnas:** 13+ variables
- **Variables Numéricas:** Sales, Quantity, Discount, Profit
- **Variables Categóricas:** Category, Sub-Category, Region, Segment, Ship Mode
- **Variables Temporales:** Order Date, Ship Date
- **Imperfecciones:** Outliers en descuentos, valores negativos en profit

#### 🎯 Preguntas de Negocio Sugeridas
1. **¿Existe estacionalidad en las ventas y cómo afecta el inventario por categoría?**
2. **¿Qué productos/regiones generan más rentabilidad vs. volumen de ventas?**
3. **¿Cómo impacta el descuento en la rentabilidad final por categoría?**

#### 💡 Ventajas para el Proyecto
- Datos de retail (familiar para todos)
- Excelente para análisis temporal (series de tiempo)
- Múltiples dimensiones para segmentación (Región, Categoría, Cliente)
- Permite crear KPIs: Margen de Ganancia, Ticket Promedio, etc.
- Ideal para gráficos interactivos con filtros de fecha

---

### **4. Credit Risk Dataset (Loan Default)**

**URL:** https://www.kaggle.com/datasets/laotse/credit-risk-dataset

#### ✅ Cumplimiento de Requisitos
- **Registros:** 32,581 préstamos
- **Columnas:** 12 variables
- **Variables Numéricas:** person_age, person_income, loan_amnt, loan_int_rate, etc.
- **Variables Categóricas:** person_home_ownership, loan_intent, loan_grade
- **Variables Booleanas:** loan_status (default o no), cb_person_default_on_file
- **Imperfecciones:** Outliers en income, valores atípicos en loan_percent_income

#### 🎯 Preguntas de Negocio Sugeridas
1. **¿Qué variables predicen mejor la probabilidad de default en préstamos?**
2. **¿Cómo afecta la relación deuda/ingreso y el historial crediticio al riesgo?**
3. **¿Qué perfiles de clientes representan el mayor riesgo financiero?**

#### 💡 Ventajas para el Proyecto
- Dominio financiero (alta relevancia profesional)
- Problema de clasificación con implicaciones reales
- Permite feature engineering: Loan-to-Income Ratio, Risk Score, etc.
- Dataset con distribución desbalanceada (realista para negocio)

---

### **5. E-Commerce Sales Dataset**

**URL:** https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data

#### ✅ Cumplimiento de Requisitos
- **Registros:** Variable según versión (1,000 - 10,000+)
- **Columnas:** 12-15 variables
- **Variables Numéricas:** Amount, Qty, Sales
- **Variables Categóricas:** Category, Size, Status, Fulfilment, Ship-Service-Level
- **Variables Temporales:** Date
- **Imperfecciones:** Formatos de fecha inconsistentes, categorías duplicadas

#### 🎯 Preguntas de Negocio Sugeridas
1. **¿Qué categorías de productos generan mayor conversión y margen?**
2. **¿Existe estacionalidad en las ventas por categoría de producto?**
3. **¿Cómo afecta el método de envío a la rentabilidad final?**

#### 💡 Ventajas para el Proyecto
- E-commerce es sector actual y relevante
- Datos transaccionales para análisis de patrones
- Múltiples dimensiones para segmentación
- Permite análisis de comportamiento de compra

---

## 📊 COMPARACIÓN RÁPIDA

| Dataset | Registros | Columnas | Complejidad | Negocio | Feature Engineering |
|---------|-----------|----------|-------------|---------|---------------------|
| **IBM HR Attrition** | 1,470 | 35 | ⭐⭐⭐⭐⭐ | RH | Alto potencial |
| **Telco Churn** | 7,043 | 21 | ⭐⭐⭐⭐ | Telecomunicaciones | Medio-Alto |
| **Superstore Sales** | 9,994 | 13+ | ⭐⭐⭐⭐ | Retail | Alto (temporal) |
| **Credit Risk** | 32,581 | 12 | ⭐⭐⭐⭐ | Finanzas | Alto |
| **E-Commerce Sales** | Variable | 12-15 | ⭐⭐⭐ | E-commerce | Medio |

---

## 🎯 RECOMENDACIÓN FINAL

### Para maximizar tu calificación, considera:

**🥇 Primera Opción: IBM HR Attrition**
- Más columnas (35) = mayor complejidad estadística
- Permite demostrar expertise en EDA con múltiples dimensiones
- Dominio conocido = fácil generar insights de negocio
- Perfecto balance entre volumen y dimensionalidad

**🥈 Segunda Opción: Telco Customer Churn**
- Volumen significativo (7K+ registros)
- Problema de negocio clásico y relevante
- Datos con imperfecciones reales para demostrar limpieza
- Excelente para storytelling con IA (Groq)

---

## ⚙️ CONSIDERACIONES TÉCNICAS PARA STREAMLIT

### Feature Engineering Sugerido (cumple requisito del proyecto)

#### Para HR Attrition:
```python
# Crear columnas calculadas
df['Salary_Experience_Ratio'] = df['MonthlyIncome'] / (df['YearsAtCompany'] + 1)
df['Satisfaction_Index'] = (df['JobSatisfaction'] + df['EnvironmentSatisfaction']) / 2
df['Promotion_Gap'] = df['YearsAtCompany'] - df['YearsSinceLastPromotion']
```

#### Para Telco Churn:
```python
# Feature Engineering
df['Ticket_Promedio'] = df['TotalCharges'] / df['tenure']
df['Revenue_Risk'] = df['MonthlyCharges'] * df['Churn'].map({'Yes': 1, 'No': 0})
df['Contract_Value'] = df['tenure'] * df['MonthlyCharges']
```

#### Para Superstore:
```python
# Crear KPIs
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Discount_Impact'] = df['Sales'] * df['Discount']
df['Order_Processing_Days'] = (df['Ship Date'] - df['Order Date']).dt.days
```

---

## 🤖 INTEGRACIÓN CON GROQ - Prompt Sugerido

```python
# Ejemplo de prompt estructurado para Groq
prompt = f"""
Eres un analista de datos senior especializado en {dominio}.

DATOS ESTADÍSTICOS:
{df.describe().to_string()}

CONTEXTO:
- Dataset: {nombre_dataset}
- Registros analizados: {len(df)}
- Período: {fecha_inicio} a {fecha_fin}

INSTRUCCIONES:
1. Identifica las 3 tendencias más relevantes en los datos
2. Señala al menos 2 riesgos o áreas de preocupación
3. Proporciona 3 recomendaciones estratégicas accionables

Responde en formato estructurado y profesional, como si fuera para un CFO/CEO.
"""
```

---

## 📥 DESCARGA DIRECTA

### Opción A: Desde Kaggle
1. Crear cuenta en Kaggle (gratis)
2. Descargar el CSV directamente del link proporcionado
3. Subir a tu repositorio en `/data/`

### Opción B: Lectura Directa desde URL (Recomendado para Streamlit)
```python
import pandas as pd

# Para datasets públicos en GitHub raw
url = "https://raw.githubusercontent.com/..."
df = pd.read_csv(url)
```

---

## ✅ CHECKLIST FINAL ANTES DE ELEGIR

- [ ] Dataset tiene +1,000 registros
- [ ] Dataset tiene +10 columnas
- [ ] Incluye variables numéricas, categóricas y booleanas/temporales
- [ ] Tiene imperfecciones documentables (nulos, outliers, formatos)
- [ ] Puedo formular 3 preguntas de negocio específicas
- [ ] El dominio es relevante y de mi interés
- [ ] Permite crear al menos 1 columna calculada (Feature Engineering)
- [ ] Tiene potencial para visualizaciones interactivas con Plotly

---

## 🚀 PRÓXIMOS PASOS

1. **Selecciona tu dataset** de las opciones recomendadas
2. **Descarga y explora** el archivo CSV
3. **Define tus 3 preguntas de negocio** específicas
4. **Documenta las imperfecciones** que encontraste (para justificar limpieza)
5. **Planifica tu feature engineering** (columnas calculadas)
6. **Diseña el flujo de tu Dashboard** (módulos ETL, EDA, IA)

---

## 📞 CONTACTO

**Docente:** Jorge Iván Padilla-Buriticá  
**Email:** jipadillab@eafit.edu.co  
**Fecha Límite:** 10 de Febrero de 2026, 23:59 hrs

---

> **Nota Importante:** Todos los datasets recomendados han sido verificados para cumplir estrictamente con los requisitos del proyecto. La elección final debe basarse en tu interés personal en el dominio de negocio y tu comodidad con el contexto analítico.

**¡Éxito con tu proyecto final! 🎓**
