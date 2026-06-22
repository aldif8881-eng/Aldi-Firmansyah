import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go


# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="Aldi Frsh Business Analytics",
    page_icon="📊",
    layout="wide"
)



# ==========================
# STYLE
# ==========================

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#e3f2fd,
#ffffff
);
}

h1{
text-align:center;
}

</style>

""", unsafe_allow_html=True)



# ==========================
# LOAD DATA
# ==========================


@st.cache_data
def load_data():

    df = pd.read_csv(
        "data.csv"
    )

    return df



df = load_data()



# ==========================
# TITLE
# ==========================


st.title(
    "📊 Aldi Frsh Business Employment Analytics"
)


st.write(
    "Dashboard analisis data bisnis dan ketenagakerjaan"
)



# ==========================
# SIDEBAR
# ==========================


menu = st.sidebar.radio(

    "Menu",

    [
        "Dashboard",
        "Statistik",
        "Trend Data",
        "Analisis Kategori",
        "Kesimpulan"
    ]

)



# ==========================
# DASHBOARD
# ==========================


if menu=="Dashboard":


    st.header(
        "Dashboard Utama"
    )


    a,b,c,d = st.columns(4)


    a.metric(
        "Jumlah Data",
        len(df)
    )


    b.metric(
        "Jumlah Kolom",
        len(df.columns)
    )


    c.metric(
        "Nilai Rata-rata",
        round(df["Data_value"].mean(),2)
    )


    d.metric(
        "Nilai Maksimum",
        round(df["Data_value"].max(),2)
    )



    st.subheader(
        "Data Preview"
    )


    st.dataframe(
        df.head(20),
        use_container_width=True
    )



# ==========================
# STATISTIK
# ==========================


elif menu=="Statistik":


    st.header(
        "📈 Statistik Deskriptif"
    )


    st.dataframe(
        df.describe(),
        use_container_width=True
    )



    fig = px.histogram(

        df,

        x="Data_value",

        title="Distribusi Data Value"

    )


    st.plotly_chart(fig)



# ==========================
# TREND
# ==========================


elif menu=="Trend Data":


    st.header(
        "📊 Perkembangan Data"
    )


    trend = (

        df.groupby("Period")
        ["Data_value"]
        .mean()
        .reset_index()

    )


    fig = px.line(

        trend,

        x="Period",

        y="Data_value",

        markers=True,

        title="Trend Data Value"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ==========================
# KATEGORI
# ==========================


elif menu=="Analisis Kategori":


    st.header(
        "Analisis Berdasarkan Kategori"
    )


    kolom = st.selectbox(

        "Pilih kategori",

        [
            "Group",
            "Subject",
            "Series_title"
        ]

    )


    hasil = (

        df.groupby(kolom)
        ["Data_value"]
        .mean()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()

    )


    fig = px.bar(

        hasil,

        x=kolom,

        y="Data_value",

        title="10 Kategori Tertinggi"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ==========================
# KESIMPULAN
# ==========================


else:


    st.header(
        "📝 Kesimpulan Otomatis"
    )


    rata = df["Data_value"].mean()


    maks = df["Data_value"].max()



    st.info(

f"""
Berdasarkan hasil analisis:

Dataset memiliki jumlah data sebanyak 
**{len(df):,} baris**.

Nilai rata-rata indikator adalah 
**{rata:.2f}**.

Nilai tertinggi yang tercatat adalah
**{maks:.2f}**.

Data menunjukkan adanya variasi nilai
antar periode dan kategori yang dianalisis.

Dashboard ini dapat digunakan untuk melihat
pola perkembangan dan perbandingan indikator
bisnis ketenagakerjaan.
"""

)
