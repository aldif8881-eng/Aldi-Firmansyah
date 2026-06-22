import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Aldi Frsh Analytics",
    page_icon="📊",
    layout="wide"
)


# =====================
# CSS MODERN
# =====================

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#0f2027,
#203a43,
#2c5364
);
color:white;
}


.block-container{
padding-top:2rem;
}


h1,h2,h3{
color:white;
}


.card{

background:rgba(255,255,255,0.15);

padding:20px;

border-radius:20px;

backdrop-filter:blur(10px);

box-shadow:0 8px 30px rgba(0,0,0,0.2);

}


.metric{

font-size:30px;

font-weight:bold;

}


.small{

color:#dddddd;

}


</style>
""",unsafe_allow_html=True)



# =====================
# LOAD DATA
# =====================


@st.cache_data

def load():

    df=pd.read_csv(
        "data.csv"
    )

    return df



df=load()



# =====================
# HEADER
# =====================


st.title(
"📊 Aldi Frsh Analytics"
)


st.write(
"Business Employment Intelligence Dashboard"
)



# =====================
# SIDEBAR
# =====================


menu=st.sidebar.selectbox(

"Menu Analisis",

[
"Dashboard",
"Statistik",
"Trend",
"Kategori",
"Insight"
]

)



# =====================
# DASHBOARD
# =====================


if menu=="Dashboard":


    st.subheader(
    "Overview"
    )


    a,b,c,d=st.columns(4)



    with a:

        st.markdown(
        f"""
        <div class="card">
        <div>Total Data</div>
        <div class="metric">{len(df):,}</div>
        </div>
        """,
        unsafe_allow_html=True
        )



    with b:

        st.markdown(
        f"""
        <div class="card">
        <div>Rata-rata</div>
        <div class="metric">
        {df['Data_value'].mean():.2f}
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )



    with c:

        st.markdown(
        f"""
        <div class="card">
        <div>Nilai Tertinggi</div>
        <div class="metric">
        {df['Data_value'].max():.2f}
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )


    with d:

        st.markdown(
        f"""
        <div class="card">
        <div>Variabel</div>
        <div class="metric">
        {len(df.columns)}
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )



    st.divider()



    fig=px.histogram(

        df,

        x="Data_value",

        title="Distribusi Data"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )




# =====================
# STATISTIK
# =====================


elif menu=="Statistik":


    st.header(
    "📈 Statistik Deskriptif"
    )


    st.dataframe(

    df.describe(),

    use_container_width=True

    )



# =====================
# TREND
# =====================


elif menu=="Trend":


    st.header(
    "📊 Trend Perkembangan"
    )



    trend=(

    df.groupby("Period")
    ["Data_value"]
    .mean()
    .reset_index()

    )



    fig=px.line(

        trend,

        x="Period",

        y="Data_value",

        markers=True

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )




# =====================
# KATEGORI
# =====================


elif menu=="Kategori":


    st.header(
    "🏢 Analisis Kategori"
    )


    pilihan=st.selectbox(

    "Pilih kategori",

    [
    "Group",
    "Subject",
    "Series_title"
    ]

    )



    hasil=(

    df.groupby(pilihan)
    ["Data_value"]
    .mean()
    .sort_values(
    ascending=False
    )
    .head(10)
    .reset_index()

    )


    fig=px.bar(

        hasil,

        x=pilihan,

        y="Data_value",

        title="Top 10"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )




# =====================
# INSIGHT
# =====================


elif menu=="Insight":


    st.header(
    "🧠 Automatic Insight"
    )



    rata=df["Data_value"].mean()

    maksimum=df["Data_value"].max()



    st.markdown(
    f"""

<div class="card">


Berdasarkan hasil analisis:


Dataset memiliki **{len(df):,} data**.


Nilai rata-rata indikator adalah:

**{rata:.2f}**


Nilai tertinggi:

**{maksimum:.2f}**


Secara umum data menunjukkan adanya
perbedaan nilai antar periode dan kategori.


</div>

""",
unsafe_allow_html=True

)
