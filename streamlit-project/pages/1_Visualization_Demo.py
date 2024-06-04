import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.figure_factory as ff 
import folium
import branca.colormap as cm
from streamlit_folium import folium_static
import plotly.express as px
import plotly.graph_objects as go

st.title('Visualizing')


df = pd.read_csv('dataset/dataheart_cleaned.csv')

# Fungsi untuk memuat data dengan caching
@st.cache_data
def load_data():
    return pd.read_csv('dataset/dataheart_cleaned.csv')

@st.cache_data
def generate_visualizations(df, selected_factor):
    # Daftar faktor risiko
    risk_factors = ['AlcoholDrinking', 'Smoking', 'Sex', 'DiffWalking', 'Stroke', 'KidneyDisease']

    # Filter data berdasarkan heart disease
    no_heart_disease = df[df['HeartDisease'] == 'No']
    heart_disease = df[df['HeartDisease'] == 'Yes']

    # Plot tanpa heart disease
    fig1 = px.histogram(no_heart_disease, x='AgeCategory', color=selected_factor, 
                        title=f"{selected_factor} Among Different Age Groups (No Heart Disease)",
                        labels={'AgeCategory': 'Age Category', 'count': 'Individuals'})

    # Plot dengan heart disease
    fig2 = px.histogram(heart_disease, x='AgeCategory', color=selected_factor, 
                        title=f"{selected_factor} Among Different Age Groups (Heart Disease)",
                        labels={'AgeCategory': 'Age Category', 'count': 'Individuals'})

    return fig1, fig2

# Fungsi utama aplikasi
def main():
    # Judul aplikasi
    st.title("Analisis Faktor Risiko Berdasarkan Kategori Usia")

    # Memuat data
    df = load_data()

    # Select box untuk memilih faktor risiko
    selected_factor = st.selectbox("Pilih Faktor Risiko:", ['AlcoholDrinking', 'Smoking', 'Sex', 'DiffWalking', 'Stroke', 'KidneyDisease'])

    # Generate visualizations
    fig1, fig2 = generate_visualizations(df, selected_factor)

    # Tampilkan plot
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

# Pastikan script dijalankan sebagai modul utama
if __name__ == "__main__":
    main()


@st.cache_data
def calculate_means(df):
    return df.groupby(['AgeCategory', 'HeartDisease']).agg({
        'BMI': 'mean', 
        'PhysicalHealth': 'mean', 
        'MentalHealth': 'mean', 
        'SleepTime': 'mean'
    }).reset_index()



# Fungsi untuk membuat visualisasi menggunakan Plotly
@st.cache_data
def create_plot(df, selected_factor, heart_disease):
    fig = px.line(df[df['HeartDisease'] == heart_disease], 
                  x='AgeCategory', y=selected_factor, 
                  title=f"{selected_factor} Among Different Age Groups ({heart_disease})",
                  labels={'AgeCategory': 'Age Category', selected_factor: 'Mean Values'})
    return fig

# Fungsi utama aplikasi
def main():
    # Judul aplikasi
    st.title("Analisis Faktor Risiko Berdasarkan Kategori Usia")

    # Memuat data
    df = load_data()

    # Select box untuk memilih fitur
    selected_factor = st.selectbox("Pilih Faktor Risiko:", ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime'])

    # Tabs untuk memilih HeartDisease 'Yes' atau 'No'
    tab1, tab2 = st.tabs(["Heart Disease", "No Heart Disease"])

    # Menghitung rata-rata fitur berdasarkan kategori
    other_risk_factor_among_agegroups = calculate_means(df)

    with tab1:
        st.subheader(f"{selected_factor} Among Different Age Groups (Heart Disease)")
        # Membuat visualisasi untuk Heart Disease
        fig1 = create_plot(other_risk_factor_among_agegroups, selected_factor, 'Yes')
        st.plotly_chart(fig1)
        
    with tab2:
        st.subheader(f"{selected_factor} Among Different Age Groups (No Heart Disease)")
        # Membuat visualisasi untuk No Heart Disease
        fig2 = create_plot(other_risk_factor_among_agegroups, selected_factor, 'No')
        st.plotly_chart(fig2)

# Pastikan script dijalankan sebagai modul utama
if __name__ == "__main__":
    main()