import pandas as pd
import plotly.express as px
import streamlit as st

# Título y encabezado
st.title("Cuadro de mandos de vehículos")
st.header("Análisis del kilometraje y precio de los coches")

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla 1: Histograma
show_hist = st.button("Mostrar histograma del kilometraje")

if show_hist:
    st.write("Creando un histograma del kilometraje de los coches...")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla 2: Gráfico de dispersión
show_scatter = st.button(
    "Mostrar gráfico de dispersión (Kilometraje vs Precio)")

if show_scatter:
    st.write("Creando un gráfico de dispersión: Kilometraje vs Precio")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price"

    )
    st.plotly_chart(fig_scatter, use_container_width=True)
