import streamlit as st

st.title("Ai Food")
st.write("Pseudo delivery")

def listar_restaurantes():
    return [
        {
            "nome": "Sushi Top",
            "categoria": "Japones",
            "descricao": "Essa é massa"
        },
        {
            "nome": "Pizzaria delis",
            "categoria": "Italiano",
            "descicao": "Pizza gostosa"
        },
        {
            "nome": "Macarrao bom",
            "categoria": "Italiano",
            "descricao": "Nao tem pizza, mas tem macarrao"
        }
    ]
    
def listar_nomes_dos_restaurantes():
    restaurantes = listar_restaurantes()
    
    nomes = []
    for restaurante in restaurantes:
        nome = restaurante["nome"]
        nomes.append(nome)
        
    return nomes

def listar_categorias():
    restaurantes = listar_restaurantes()
    
    categorias = []
    for restaurante in restaurantes:
        categoria = restaurante["categoria"]
        
        if categoria not in categorias:
            categorias.append(categoria)
            
    return categorias

st.sidebar.title("Busque um restaurante")
nome_para_buscar = st.sidebar.text_input("Digite o nome do restaurante")

if nome_para_buscar:
    todos_restaurantes = listar_nomes_dos_restaurantes()
    
    if nome_para_buscar in todos_restaurantes:
        st.write("Restaurante encontrado")
    else:
        st.write("Restaurante nao encontrado")

categorias = listar_categorias()
categoria_para_buscar = st.sidebar.selectbox("Escolha uma categoria: ", categorias)

if categoria_para_buscar:
    numero_de_restaurantes = 0
    todos_restaurantes = listar_restaurantes()
    
    for restaurante in todos_restaurantes:
        if restaurante["categoria"] == categoria_para_buscar:
            numero_de_restaurantes += 1
            
    st.write("Encontramos essa quantidade de restaurantes: ", numero_de_restaurantes)
    