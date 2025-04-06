from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# route params
@app.get('/saudacao/{nome}')
async def home(nome: str):
    texto = f'Olá, {nome}!'
    return {"mensagem": texto}

@app.get('/quadrado/{numero}')
async def quadrado(numero: int):
    resultado = numero * numero
    texto = f'O quadrado de {numero} é {resultado}.'
    return {"mensagem": texto}

# query params
@app.get('/dobro')
async def dobro(numero: int):
    resultado = numero * 2
    texto = f'O dobro de {numero} é {resultado}.'
    return {"mensagem": texto}

@app.get('/area-retangulo')
def area_retangulo(largura: int, altura: int = 1):
    area = largura * altura
    return {'area': area}

class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto ({produto.nome} - R$ {produto.preco}) cadastrado com sucesso!'}