from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from fastapi import HTTPException
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositories.series import RepositorioSerie

# Criar a base de dados
criar_bd()

app = FastAPI()

@app.post('/series')
def criar_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada

@app.get('/series')
def listar_serie(db: Session = Depends(get_db)):
    return RepositorioSerie(db).listar()

@app.get('/series/{serie_id}', response_model=schemas.Serie)
def obter_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).obter(serie_id)
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    return serie  

@app.delete('/series/{serie_id}')
def deletar_serie(serie_id: int, db: Session = Depends(get_db)):
    RepositorioSerie(db).remover(serie_id)
    return {"msg": "Série removida com sucesso"}
