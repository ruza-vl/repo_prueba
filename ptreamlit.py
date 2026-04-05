import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas 2026", layout="wide")

st.title("🚀 Panel de Control Actualizado")

# Generar datos de ejemplo
datos = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['oducto A', 'oducto B', 'oducto C']
)

# Diseño de columnas para KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Ventas Totales", "$45,200", "+12%")
col2.metric("Nuevos Clientes", "1,240", "5.4%")
col3.metric("Tasa de Conversión", "3.2%", "-0.5%")

# Gráfico interactivo
st.subheader("Tendencia de Rendimiento")
st.line_chart(datos)

# Tabla de datos filtrable
if st.checkbox('Mostrar datos crudos'):
    st.write(datos)
