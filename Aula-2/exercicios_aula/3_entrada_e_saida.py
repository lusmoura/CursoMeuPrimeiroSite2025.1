# Entrada
nome = input()
sobrenome = input()

nome_completo = nome + " " + sobrenome
print(nome_completo)

# Entrada com instruções - outro exemplo
titulo_do_post = input("Digite o título do post: ")
print(titulo_do_post)

# Entrada com conversão de tipo
quantidade_maxima_de_posts = int(input("Digite a quantidade máxima de posts: "))
quantidade_atual_de_posts = int(input("Digite a quantidade atual de posts: "))

quantidade_restante_de_posts = quantidade_maxima_de_posts - quantidade_atual_de_posts
print(quantidade_restante_de_posts)

# Saída com instruções
nome = input("Digite seu nome: ")
print("Olá,", nome)

# Saída com formatação
nome = input("Digite seu nome: ")
print(f"Olá, {nome}")