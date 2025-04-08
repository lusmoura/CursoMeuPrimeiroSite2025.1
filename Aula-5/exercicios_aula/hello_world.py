# Documentação: https://fastapi.tiangolo.com/pt/tutorial/first-steps/#passo-4-defina-uma-funcao-de-rota

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

uvicorn.run(app, host="localhost", port=8001)
