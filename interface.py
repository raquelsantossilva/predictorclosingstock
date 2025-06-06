import streamlit as st
import datetime
import joblib
import pandas as pd 
import numpy as np 


modelo =joblib.load('modelo_regressao_acoes_google.pkl')

st.title("Previsão de Preço de Fechamento de Ações do Google (Simulado)")
st.markdown("Use este aplicativo para prever o preço de fechamento de ações do Google para um dia específico.")

st.header("Insira os Dados para a Previsão:")



features_esperadas= ["High","Low","Open","Volume"]
entradas = {}


for feature in features_esperadas:
    if feature == 'Volume':
        entradas[feature] = st.number_input(f"Volume do Dia ({feature})", min_value=0.0, value=5_000_000.0, step=100_000.0)
    else: 
        entradas[feature] = st.number_input(f"{feature} do Dia (USD)", min_value=0.0, value=160.0, step=0.01)


if st.button("Fazer Previsão"):
    try:
        dados_para_prever = pd.DataFrame([entradas])
        
        dados_para_prever = dados_para_prever[features_esperadas]

        previsao = modelo.predict(dados_para_prever)[0] 
        st.success(f" o preço de fechamento previsto é: **${previsao:.2f}**")

    except Exception as e:
        st.error(f"Ocorreu um erro ao fazer a previsão: {e}")
        st.warning("Verifique se todos os campos foram preenchidos corretamente.")

st.sidebar.markdown("---")
st.sidebar.info("Este é um modelo de previsão de ações simulado para fins demonstrativos. Não use para decisões financeiras reais.")