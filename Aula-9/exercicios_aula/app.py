import PIL.Image
import streamlit as st
import PIL

# Definindo os posts
def listar_produtos():
    produtos = [
        {
            "nome": "Bolsa",
            "descricao": "Uma bolsa bem linda",
            "nome_do_arquivo": "bolsa.jpg",
            "estoque": 10 
        },
        {
            "nome": "Chapeu",
            "descricao": "Um chapeu de cowboy",
            "nome_do_arquivo": "chapeu.jpg",
            "estoque": 5
        },
        {
            "nome": "Calça",
            "descricao": "Jeans bom",
            "nome_do_arquivo": "calca.jpeg",
            "estoque": 2
        }
    ]
    return produtos

def listar_nomes_dos_produtos():
    produtos = listar_produtos()
    
    nomes = []
    for produto in produtos:
        nome_do_produto = produto["nome"]
        nomes.append(nome_do_produto)
        
    return nomes


def pegar_produto_a_partir_do_nome(nome_alvo):
    produtos = listar_produtos()
    
    produto_alvo = None
    for produto in produtos:
        nome_atual = produto["nome"]
        
        if nome_atual == nome_alvo:
            produto_alvo = produto
    
    return produto_alvo
            

def pagina_principal():
    # Configurações básicas
    st.title("Minha loja")

    # Barra lateral
    st.sidebar.write("Meus produtos")
    nomes = listar_nomes_dos_produtos()
    nome_selecionado = st.sidebar.selectbox("Produtos", nomes)

    # Pagina principal
    produto_alvo = pegar_produto_a_partir_do_nome(nome_alvo=nome_selecionado)

    if produto_alvo:
        nome_do_arquivo = produto_alvo["nome_do_arquivo"]
        imagem = PIL.Image.open(f"imagens/{nome_do_arquivo}")
        st.image(imagem, "Imagem meramente ilustrativa")
        
        descricao_produto = produto_alvo["descricao"]
        st.write(descricao_produto)

        estoque = produto_alvo["estoque"]
        st.number_input("Quantidade", min_value=0, max_value=estoque)

        clicado = st.button("Comprar")
        
        if clicado:
            pagina_comprar()


def pagina_comprar():
    st.title("Pagina de comprar")
    st.write("Voce está na pagina de compras, insira seus detalhes")
    st.text_input("Numero do cartao")
    st.date_input("Validade do cartao")
    st.text_input("CVV")



lista_de_paginas = {
    "produtos": pagina_principal,
    "comprar": pagina_comprar
}
# pega somente os titulos das paginas -- "produtos" e "comprar"
titulos_das_paginas = lista_de_paginas.keys()

pagina_selecionada = st.sidebar.radio("Selecione a pagina", titulos_das_paginas)
lista_de_paginas[pagina_selecionada]()
