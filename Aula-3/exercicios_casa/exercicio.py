# 1. Ler um número que representa uma quantidade de posts e em seguida ler cada um dos posts
# a. Extra: salvar os posts em uma lista ou em um dicionário
numero_de_posts = int(input("Digite o numero de posts: "))
lista_de_posts = []
for posicao in range(numero_de_posts):
    titulo = input("Digite o titulo: ")
    conteudo = input("Digite o conteudo: ")
    
    dicionario_post = {
        "titulo": titulo,
        "conteudo": conteudo
    }
    
    lista_de_posts.append(dicionario_post)

# 2. Em seguida, definir um menu da seguinte forma:
#    Enquanto o usuário não digitar 0:
#        Se ele digitar 1, imprima o primeiro post da lista
#        Se ele digitar 2, imprima todos os posts da lista
#        Se ele digitar 3, imprima apenas os titulos dos posts
#        Se ele digitar 0, acabe a execução
# Para esse exercício, você pode usar a lista do exercício extra (a) ou você pode criar uma variável no código com os posts
opcao = int(input("Digite uma opcao: "))

while opcao != 0:
    if opcao == 1:
        print(lista_de_posts[0])
    elif opcao == 2:
        print(lista_de_posts)
    elif opcao == 3:
        for post in lista_de_posts:
            print(post["titulo"])
    else:
        print("Voce digitou uma opcao invalida")
    
    opcao = int(input("Digite uma opcao: "))

# b. Extra: Limitar o conteúdo do post a um número de caracteres. Adicionar uma opção 4 no menu para imprimir apenas o que cabe no limite.

