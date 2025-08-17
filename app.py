import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Controle Financeiro", layout="centered")

st.title("💰 Controle Financeiro Pessoal")

# Inicializa a sessão
if "dados" not in st.session_state:
    st.session_state.dados = []

# Formulário de entrada
with st.form("formulario"):
    descricao = st.text_input("Descrição")
    valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
    categoria = st.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Saúde", "Outros"])
    data = st.date_input("Data", value=date.today())
    enviado = st.form_submit_button("Salvar")

    if enviado and descricao:
        nova_transacao = {
            "Descrição": descricao,
            "Valor": valor,
            "Categoria": categoria,
            "Data": data.strftime("%d/%m/%Y")
        }
        st.session_state.dados.append(nova_transacao)
        st.success("Transação salva com sucesso!")

# Exibe os dados salvos
if st.session_state.dados:
    st.markdown("---")
    st.subheader("📋 Histórico de Transações")
    df = pd.DataFrame(st.session_state.dados)
    st.dataframe(df, use_container_width=True)

    # Resumo por categoria
    st.markdown("---")
    st.subheader("📊 Resumo por Categoria")
    resumo = df.groupby("Categoria")["Valor"].sum().reset_index()
    st.bar_chart(resumo.set_index("Categoria"))
else:
    st.info("Nenhuma transação registrada ainda.")
