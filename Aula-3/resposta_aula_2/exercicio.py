# 1. Implementar um código que leia um título e um conteúdo de um post e imprima na tela.
titulo = input("Digite o título do post: ")
conteudo = input("Digite o conteúdo do post: ")
print(f"Título: {titulo}")
print(f"Conteúdo: {conteudo}")

# a. Extra: Imprimir na tela o tamanho do conteúdo do post.
tamanho_conteudo = len(conteudo)
# Dá para usar o len ^ para pegar o tamanhao de uma string
print(f"Tamanho do conteúdo: {tamanho_conteudo}")

# b. Extra: Definir um tamanho máximo para o conteúdo do post e imprimir na tela o quanto falta para atingir o limite.
tamanho_maximo = int(input("Digite o tamanho máximo do conteúdo: "))
tamanho_restante = tamanho_maximo - tamanho_conteudo
print(f"Tamanho restante: {tamanho_restante}")

# Extra do Extra: Se o tamanho do conteúdo for maior que o tamanho máximo, imprimir uma mensagem de erro.
# Isso é conteúdo da aula 3!!
if tamanho_conteudo > tamanho_maximo:
    print("Erro: o conteúdo ultrapassou o tamanho máximo permitido.")
else:
    print("Conteúdo dentro do limite de tamanho.")