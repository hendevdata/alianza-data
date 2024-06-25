# Análisis del Rendimiento de la Campaña

Este repositorio contiene una aplicación de Streamlit para analizar y visualizar el rendimiento de diversas campañas de marketing. La aplicación se basa en un conjunto de datos proporcionado y sigue varios pasos para limpiar, analizar y visualizar los datos.

## Descripción

La aplicación de Streamlit está diseñada para proporcionar una visión detallada del rendimiento de las campañas de marketing. Los pasos incluyen:

1. **Limpieza de Datos**
2. **Estadísticas Descriptivas**
3. **Visualizaciones**
4. **Análisis del Rendimiento de la Campaña**

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu_usuario/analisis-campana.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd analisis-campana
    ```
3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Asegúrate de tener el archivo de datos `data.csv` en el directorio del proyecto.
2. Ejecuta la aplicación de Streamlit:
    ```sh
    streamlit run app.py
    ```
3. Abre tu navegador y navega a `http://localhost:8501` para ver la aplicación.

## Estructura de la Aplicación

### Paso 1: Limpieza de Datos

La aplicación elimina columnas no críticas con valores faltantes excesivos, estandariza los formatos de fechas, limpia los números de teléfono y maneja entradas erróneas.

### Paso 2: Estadísticas Descriptivas

Se muestran las estadísticas descriptivas para las columnas numéricas del conjunto de datos.

### Paso 3: Visualizaciones

La aplicación genera varias visualizaciones para entender mejor la distribución y las características de los datos:

- **Distribución de Países (Top 10)**
- **Distribución de Fuentes (Top 10)**
- **Distribución de Campañas (Top 10)**

### Paso 4: Análisis del Rendimiento de la Campaña

La aplicación agrega métricas clave por campaña y calcula tasas de conversión. Las visualizaciones incluyen:

- **Total de Entradas por Campaña (Top 10)**
- **Total de Contactos por Campaña (Top 10)**
- **Leads Calificados por Campaña (Top 10)**
- **Tasa de Conversión de Contacto a Lead por Campaña (Top 10)**

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, envía un pull request o abre un issue para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
