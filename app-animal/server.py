from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str] = None
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get('/animais')
def listar_animais():
    return banco

@app.get('/animais/{id}')
def obter_animal(id: str):
    for animal in banco:
        if animal.id == id:
            return animal
    return {'erro': 'Animal não encontrado'}

@app.delete('/animais/{id}')
def remover_animal(id: str):
    # buscar o animal
    posicao = -1
    for index, animal in enumerate(banco):
        if animal.id == id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'mensagem': 'Animal não encontrado'}

@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None