# Lê um único post e imprime
def le_post():
    titulo = input("Digite o título do post: ")
    conteudo = input("Digite o conteúdo do post: ")
    post = {
        "titulo": titulo,
        "conteudo": conteudo
    }
    print(f"Post lido: {post}")
    
le_post()

# Utiliza a função le_post() para ler vários posts
def le_varios_posts():
    numero_de_posts = int(input("Digite a quantidade de posts: "))
    
    for i in range(numero_de_posts):
        le_post()

le_varios_posts()

# Utiliza a função le_post() para ler vários posts, mas dessa vez o número de posts é passado como argumento
def le_posts(numero):
    for i in range(numero):
        le_post()
        
le_posts(3)

# Utiliza uma função com retorno para ler o número de posts
def le_numero_de_posts():
    numero_de_posts = int(input("Digite a quantidade de posts: "))
    return numero_de_posts

numero_de_posts = le_numero_de_posts()
le_posts(numero_de_posts)