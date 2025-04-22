from turtle import pos
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Endpoint para retornar todos os posts
@app.get("/posts")
def listar_posts():
    posts = [
            {"titulo": "Post 1", "conteudo": "Conteudo do post 1"},
            {"titulo": "Post 2", "conteudo": "Conteudo do post 2"},
            {"titulo": "Post 3", "conteudo": "Conteudo do post 3"},
        ]
    return posts

# Endpoint para retornar um post específico
@app.get("/posts/{post_id}")
def obter_post(post_id: int):
    posts = [
            {"id": "1", "titulo": "Post 1", "conteudo": "Conteudo do post 1"},
            {"id": "2", "titulo": "Post 2", "conteudo": "Conteudo do post 2"},
            {"id": "3", "titulo": "Post 3", "conteudo": "Conteudo do post 3"},
        ]
    
    post_para_retornar = None
    for post in posts:
        if post["id"] == str(post_id):
            post_para_retornar = post
            break
    
    return post_para_retornar

# Endpoint para criar um novo post
@app.post("/posts")
def criar_post(post: dict):
    posts = [
            {"titulo": "Post 1", "conteudo": "Conteudo do post 1"},
            {"titulo": "Post 2", "conteudo": "Conteudo do post 2"},
            {"titulo": "Post 3", "conteudo": "Conteudo do post 3"},
        ]
    
    posts.append(post)
    return post

# Endpoint para atualizar um post existente
@app.put("/posts/{post_id}")
def atualizar_post(post_id: int, post: dict):
    posts = [
            {"id": "1", "titulo": "Post 1", "conteudo": "Conteudo do post 1"},
            {"id": "2", "titulo": "Post 2", "conteudo": "Conteudo do post 2"},
            {"id": "3", "titulo": "Post 3", "conteudo": "Conteudo do post 3"},
        ]
    
    for i, p in enumerate(posts):
        if p["id"] == str(post_id):
            posts[i] = post
            break
    
    return post

uvicorn.run(app, host="localhost", port=8001)