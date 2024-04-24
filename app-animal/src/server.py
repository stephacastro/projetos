from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from typing import Optional
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#origins = ['http://localhost:5500', 'http://localhost:5000', 'http://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str 
    cor: str

banco_animal: List[Animal] = []

@app.get("/animais")
async def listar_animais():
    return banco_animal

@app.get("/animais/{id}")
async def id_animal(id: str):
    for animal in banco_animal:
        if animal.id == id:
            return animal
    return {'ERROR': 'Animal não localizado'}

# endpoint que envia os animais 
@app.post("/animais")
async def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco_animal.append(animal)
    return {"Cadastrado": f'Animal:{animal.nome}, Idade:{animal.idade}, Sexo:{animal.sexo}, Cor:{animal.cor}'}

@app.delete("/animais/{id}")
async def deletar_animais(id: str):
    for i, animal in enumerate(banco_animal):
        if animal.id == id:
            del banco_animal[i]
            return {'Mensagem' f' ID {id} deletado com sucesso!'}
    return {'ERROR': 'ID não localizado'}
    