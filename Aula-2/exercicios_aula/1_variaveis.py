# int - número inteiro
numero_inteiro = 10
print(numero_inteiro)

# float - número decimal
numero_decimal = 10.5
print(numero_decimal)

# string - texto
texto = "Hello, World!"
print(texto)

# bool - booleano
booleano = True
print(booleano)

# list - lista
lista = [1, 2, 3, 4, 5]
primeiro_elemento = lista[0]
ultimo_elemento = lista[-1]
print(lista)
print(primeiro_elemento)
print(ultimo_elemento)

# dict - dicionário
dicionario = {"nome": "João", "idade": 20}
nome = dicionario["nome"]
idade = dicionario["idade"]
print(dicionario)
print(nome)
print(idade)

# input
nome = input("Digite seu nome: ")
idade = input("Digite a sua idade:")
frase = f"Seu nome é: {nome}. Sua idade é {idade}"
print(frase)

# lista de dicionarios
post_1 = {
    "titulo": "Programação em Python",
    "resumo": "Programar em Python é muito top" 
}

post_2 = {
    "titulo": "Variaveis",
    "resumo": "Variáveis são caixinhas que armazenam valores. Existem diversos tipos de variáveis. Isso, por exemplo, é uma string em um dicionário"
}

lista_de_posts = [post_1, post_2]
print(lista_de_posts)