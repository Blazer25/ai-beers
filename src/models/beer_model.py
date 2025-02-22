from pydantic import BaseModel

class Beer(BaseModel):
    nome: str
    estilo: str
    abv: float
    ibu: float
    descricao: str
    rotulo: str = ""