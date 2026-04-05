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
    
    chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['Producto A', 'Producto B', 'Producto C']
)

st.set_page_config(page_title="Dashboard de Ventas 2026", layout="wide")

st.title("🚀 Panel de Control Pro")

# --- Datos de ejemplo mejorados ---
chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['Producto A', 'Producto B', 'Producto C']
)

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Ventas Totales", "$45,200", "+12%")
col2.metric("Nuevos Clientes", "1,240", "5.4%")
col3.metric("Tasa de Conversión", "3.2%", "-0.5%")

st.divider()

# --- Nueva Sección de Gráficos ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📈 Crecimiento Acumulado")
    st.area_chart(chart_data)

with col_right:
    st.subheader("📊 Comparativa por Categoría")
    st.bar_chart(chart_data)

# --- Gráfico de Dispersión / Mapas (Opcional) ---
st.subheader("📍 Distribución Geográfica de Ventas")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [10.48, -66.90], # Coordenadas ejemplo (Caracas)
    columns=['lat', 'lon']
)
st.map(map_data)

# --- Tabla de datos ---
with st.expander("🔍 Ver detalle de inventario"):
    st.dataframe(chart_data, use_container_width=True)
