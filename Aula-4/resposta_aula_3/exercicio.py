# 1. Ler um número que representa uma quantidade de posts e em seguida ler cada um dos posts
numero_de_posts = int(input("Digite a quantidade de posts: "))
posts = []
for i in range(numero_de_posts):
    titulo = input(f"Digite o título do post {i + 1}: ")
    conteudo = input(f"Digite o conteúdo do post {i + 1}: ")
    
    # a. Extra: salvar os posts em uma lista ou em um dicionário
    post = {
        "titulo": titulo,
        "conteudo": conteudo
    }
    posts.append(post)


# 2. Em seguida, definir um menu da seguinte forma:
#    Enquanto o usuário não digitar 0:
#        Se ele digitar 1, imprima o primeiro post da lista
#        Se ele digitar 2, imprima todos os posts da lista
#        Se ele digitar 3, imprima apenas os titulos dos posts
#        Se ele digitar 0, acabe a execução
# Para esse exercício, você pode usar a lista do exercício extra (a) ou você pode criar uma variável no código com os posts
opcao = int(input("Digite uma opção (1: primeiro post, 2: todos os posts, 3: títulos, 0: sair): "))

while opcao != 0:
    if opcao == 1:
        print(f"Primeiro post: {posts[0]}")
    elif opcao == 2:
        print(f"Posts: {posts}")
    elif opcao == 3:
        for post in posts:
            print(f"Título: {post['titulo']}")

    opcao = int(input("Digite uma opção (1: primeiro post, 2: todos os posts, 3: títulos, 0: sair): "))


# b. Extra: Limitar o conteúdo do post a um número de caracteres. Adicionar uma opção 4 no menu para imprimir apenas o que cabe no limite.
opcao = int(input("Digite uma opção (1: primeiro post, 2: todos os posts, 3: títulos, 4: limite, 0: sair): "))
limite = int(input("Digite o número de caracteres para o limite: "))

while opcao != 0:
    if opcao == 1:
        print(f"Primeiro post: {posts[0]}")
    elif opcao == 2:
        print(f"Posts: {posts}")
    elif opcao == 3:
        for post in posts:
            print(f"Título: {post['titulo']}")
    elif opcao == 4:
        for post in posts:
            conteudo_limitado = post['conteudo'][:limite]
            print(f"Conteúdo limitado: {conteudo_limitado}")

    opcao = int(input("Digite uma opção (1: primeiro post, 2: todos os posts, 3: títulos, 4: limite, 0: sair): "))