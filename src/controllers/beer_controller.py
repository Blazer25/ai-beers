from typing import Optional
from fastapi import APIRouter, HTTPException
from services import beer_service
from models.beer_model import Beer

router = APIRouter()

@router.get("/cervejas-caracteristicas", response_model=list[Beer])
def get_beers(caracteristica: str, limiar: Optional[float] = 0.1 , limite: int = 10):
    beers = beer_service.find_beers_by_characteristic(caracteristica, limiar)
    if not beers:
        raise HTTPException(status_code=404, detail="Cervejas não foram encontradas com essas caracteristicas")
    return beers[:limite]

@router.post("/treinar-modelo")
def train_model():
    beer_service.train_model()
    return {"mensagem": "Modelo treinado com sucesso!"}