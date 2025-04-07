from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
    id: Optional[int] = None
    titulo: str
    ano: int
    genero: str
    qtd_temporadas: int

    model_config = {
        "from_attributes": True
    }