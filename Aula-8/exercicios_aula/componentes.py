import streamlit as st

aceitou_termos_de_uso = st.checkbox("Você aceita os termos de uso?")

if aceitou_termos_de_uso:
    st.button("Continuar")


quantidade_de_coxinhas = st.number_input("Selecione a quantidade de coxinhas", min_value=0, max_value=10)
st.write("Voce escolheu: ", quantidade_de_coxinhas)

arquivo = st.file_uploader("Escolha seu arquivo")

if arquivo:
    st.write("O tamanho do arquivo é: ", arquivo.size)

horario = st.time_input("Escolha um horario")

if horario:
    st.write("O horario selecionado foi: ", horario)


lista_de_materiais = ["vidro", "papel", "plastico", "metal"]
material = st.radio("Escolha um material", lista_de_materiais)
st.write("Voce escolheu o seguinte material: ", material)

lista_de_materiais = ["vidro", "papel", "plastico", "metal"]
material = st.selectbox("Escolha um material", lista_de_materiais)
st.write("Voce escolheu o seguinte material: ", material)


data = st.date_input("Selecione uma data")
if data:
    st.write("A data selecionada foi: ", data)


texto = st.text_input("Digite um texto")
st.write("Seu texto foi: ", texto)