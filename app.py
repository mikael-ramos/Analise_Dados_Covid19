import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Analise de dados - Dashborad",
    layout="wide",
    page_icon="📊"
)

st.header("Analise de dados📊 - COVID-19🔍", divider="gray")

pd_dadosCovid = pd.read_csv("dados_covid.csv")
countries = pd_dadosCovid["Country/Region"]
st.write("Paises")
select_countries = st.multiselect(
    "Selecione os paises para a analise",
    countries,default=["Brazil","US","Italy","Spain","Germany"]
)
if select_countries:
    st.header("Grafico de casos confirmados", divider="gray")
    filtred_countries = pd_dadosCovid[pd_dadosCovid["Country/Region"].isin(select_countries)]
    countries_data = filtred_countries.groupby(["Country/Region"])

    fig_confirmed = st.bar_chart(
        filtred_countries,
        x="Country/Region",
        y="Confirmed",
        color="Country/Region",
        height=500,
        use_container_width=False,
        width=900
    )
    st.header("Grafico de mortes confirmadas", divider="gray")
    
    fig_death_confirmed = st.bar_chart(
        filtred_countries,
        x="Country/Region",
        y="Deaths",
        color="Country/Region",
        height=500,
        use_container_width=False,
        width=900
    )
    st.header("Grafico visão geral de mortes e casos confirmados", divider="gray")
    fig_general_visualization = st.bar_chart(
        filtred_countries,
        x="Country/Region",
        y=["Deaths","Confirmed"],
        color="Country/Region",
        height=500,
        use_container_width=False,
        width=900
    )

    
    