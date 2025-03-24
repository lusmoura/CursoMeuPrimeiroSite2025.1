# 1. Limitar o conteúdo do post a um número de caracteres. Imprimir apenas o que cabe no limite.
limite_caracteres = 280
titulo = input("Digite o título do post: ")
conteudo = input("Digite o conteúdo do post: ")

if len(conteudo) > limite_caracteres:
    conteudo_limitado = conteudo[:limite_caracteres]
    print(conteudo_limitado)
else:
    print(conteudo)


# 2. Ler um número que representa uma quantidade de posts e em seguida ler cada um dos posts.
numero_posts = int(input("Digite a quantidade de posts: "))
posts = []
for _ in range(numero_posts):
    titulo = input("Digite o título do post: ")
    conteudo = input("Digite o conteúdo do post: ")
    post = {"titulo": titulo, "conteudo": conteudo}
    posts.append(post)
    
print(posts)