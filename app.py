import streamlit as st
import pandas as pd
import re
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Análisis del Rendimiento de la Campaña")
st.write("Esta libreta contiene el análisis y las visualizaciones del rendimiento de la campaña.")

# Step 1: Data Cleaning
st.header("Paso 1: Limpieza de Datos")

# Load the data
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Display raw data
st.subheader("Datos Crudos")
st.dataframe(data.head())

# Drop Non-Critical Columns with Excessive Missing Values
columns_to_drop = [
    'Formulario', 'Nombre de Campaña', 'UTM Content', 'ID SEAT', 
    '¿Estás dispuesto a invertir al menos US$2.000 para generar crecimiento? ex - TRABAJAS EN UNA CLINICA', 
    '¿Eres dueño de una clínica?', 
    '¿Cuál es el valor promedio de un tratamiento o servicio en tu clínica? (Dólares estadounidenses) * *', 
    '¿Cuál es tu rol en la clínica?', '¿Qué tipo de publicidad usas?', 
    '¿Cuál es el valor promedio de un tratamiento o servicio en tu clínica? ', 
    '¿Qué tan importante para ti es escalar las ventas de tu negocio?', 'Repesca wz', 'ESPECIALIDAD', 'PreCalifica', 'NOMBRE DEL CENTRO', 
    'Agendó Reunión Automáticamente', 'Fecha de la Reunión (R1)', 'Triaje', 'Fecha de contacto', 'Lead Calificado', 
    'Comentario/Observaciones', 'Agendó R1 (Stefi)', 'Fecha R1 (Stefi)', 'Status R1', 'Agendó R2', 'Status R2', '¿Cierre?', 
    'Fecha de cierre', 'Respuestas Calificatorias'
]
data.drop(columns=columns_to_drop, inplace=True)

# Standardize Date Formats
data['FECHA'] = pd.to_datetime(data['FECHA'], format='%d/%m/%Y', errors='coerce')

# Clean Up Phone Numbers
def clean_phone_number(phone):
    if pd.isna(phone):
        return phone
    return re.sub(r'\D', '', phone)

data['NUMERO'] = data['NUMERO'].apply(clean_phone_number)
data['NUMERO MEXICO'] = data['NUMERO MEXICO'].apply(clean_phone_number)

# Handle Erroneous Entries
data.replace('#REF!', pd.NA, inplace=True)

# Display cleaned data
st.subheader("Datos Limpios")
st.dataframe(data.head())

# Step 2: Descriptive Statistics
st.header("Paso 2: Estadísticas Descriptivas")
descriptive_stats = data.describe()
st.dataframe(descriptive_stats)

# Step 3: Visualizations
st.header("Paso 3: Visualizaciones")

# Visualization 1: Top 10 Countries by Number of Entries
st.subheader("Visualización 1: Distribución de Países (Top 10)")
top_countries = data['PAIS'].value_counts().head(10)
fig, ax = plt.subplots()
top_countries.plot(kind='bar', ax=ax)
ax.set_title('Top 10 Países por Número de Entradas')
ax.set_xlabel('País')
ax.set_ylabel('Número de Entradas')
ax.set_xticklabels(top_countries.index, rotation=45)
st.pyplot(fig)

# Visualization 2: Top 10 Sources by Number of Entries
st.subheader("Visualización 2: Distribución de Fuentes (Top 10)")
top_sources = data['FUENTE'].value_counts().head(10)
fig, ax = plt.subplots()
top_sources.plot(kind='bar', ax=ax)
ax.set_title('Top 10 Fuentes por Número de Entradas')
ax.set_xlabel('Fuente')
ax.set_ylabel('Número de Entradas')
ax.set_xticklabels(top_sources.index, rotation=45)
st.pyplot(fig)

# Visualization 3: Top 10 Campaigns by Number of Entries
st.subheader("Visualización 3: Distribución de Campañas (Top 10)")
top_campaigns = data['UTM Campaing'].value_counts().head(10)
fig, ax = plt.subplots()
top_campaigns.plot(kind='bar', ax=ax)
ax.set_title('Top 10 Campañas por Número de Entradas')
ax.set_xlabel('Campaña')
ax.set_ylabel('Número de Entradas')
ax.set_xticklabels(top_campaigns.index, rotation=45)
st.pyplot(fig)

# Step 4: Campaign Performance Analysis
st.header("Paso 4: Análisis del Rendimiento de la Campaña")

# Step 1: Aggregate Key Metrics by Campaign
campaign_metrics = data.groupby('UTM Campaing').agg({
    'NOMBRE': 'count',  # Total entries
    'Contactados': lambda x: x[x == 'Si'].count(),  # Total contacts
    'CALIFICA': lambda x: x[x == 'Filtrando'].count()  # Total qualified leads
}).rename(columns={
    'NOMBRE': 'Total de Entradas',
    'Contactados': 'Total de Contactos',
    'CALIFICA': 'Leads Calificados'
}).reset_index()

# Step 2: Calculate Conversion Rates
campaign_metrics['Tasa de Conversión de Contacto a Lead'] = campaign_metrics['Leads Calificados'] / campaign_metrics['Total de Contactos']

# Filter to keep only the first 10 campaigns based on the total entries
top_10_campaigns = campaign_metrics.nlargest(10, 'Total de Entradas')

# Visualization: Total Entries per Campaign (Top 10)
st.subheader("Visualización 4: Total de Entradas por Campaña (Top 10)")
fig, ax = plt.subplots()
ax.bar(top_10_campaigns['UTM Campaing'], top_10_campaigns['Total de Entradas'])
ax.set_title('Total de Entradas por Campaña (Top 10)')
ax.set_xlabel('Campaña')
ax.set_ylabel('Total de Entradas')
ax.set_xticklabels(top_10_campaigns['UTM Campaing'], rotation=90)
st.pyplot(fig)

# Visualization: Total Contacts per Campaign (Top 10)
st.subheader("Visualización 5: Total de Contactos por Campaña (Top 10)")
fig, ax = plt.subplots()
ax.bar(top_10_campaigns['UTM Campaing'], top_10_campaigns['Total de Contactos'])
ax.set_title('Total de Contactos por Campaña (Top 10)')
ax.set_xlabel('Campaña')
ax.set_ylabel('Total de Contactos')
ax.set_xticklabels(top_10_campaigns['UTM Campaing'], rotation=90)
st.pyplot(fig)

# Visualization: Qualified Leads per Campaign (Top 10)
st.subheader("Visualización 6: Leads Calificados por Campaña (Top 10)")
fig, ax = plt.subplots()
ax.bar(top_10_campaigns['UTM Campaing'], top_10_campaigns['Leads Calificados'])
ax.set_title('Leads Calificados por Campaña (Top 10)')
ax.set_xlabel('Campaña')
ax.set_ylabel('Leads Calificados')
ax.set_xticklabels(top_10_campaigns['UTM Campaing'], rotation=90)
st.pyplot(fig)

# Visualization: Contact to Lead Conversion Rate per Campaign (Top 10)
st.subheader("Visualización 7: Tasa de Conversión de Contacto a Lead por Campaña (Top 10)")
fig, ax = plt.subplots()
ax.plot(top_10_campaigns['UTM Campaing'], top_10_campaigns['Tasa de Conversión de Contacto a Lead'], marker='o')
ax.set_title('Tasa de Conversión de Contacto a Lead por Campaña (Top 10)')
ax.set_xlabel('Campaña')
ax.set_ylabel('Tasa de Conversión')
ax.set_xticklabels(top_10_campaigns['UTM Campaing'], rotation=90)
st.pyplot(fig)
