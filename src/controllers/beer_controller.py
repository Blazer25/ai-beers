from fastapi import APIRouter, HTTPException, Query
from services import beer_service
from models.beer_model import Beer
from googletrans import Translator
from typing import List, Dict

router = APIRouter()
translator = Translator()

def translate_input(caracteristica: str, language: str) -> str:
    if language in {"pt-br", "eng"}:
        return translator.translate(caracteristica, src='auto', dest='en').text
    raise HTTPException(
        status_code=400, 
        detail="Idioma não suportado, deve ser 'pt-br' ou 'eng' | Language not supported, must be 'pt-br' or 'eng'"
    )


def translate_output(beers: List[Beer], language: str) -> List[Dict]:
    translated_beers = []
    if language == "pt-br":
        for beer in beers:
            translated_beers.append({
                "nome": beer.nome,
                "estilo": beer.estilo,
                "descricao": translator.translate(beer.descricao, src='en', dest='pt').text,
                "rotulo": beer.rotulo,
                "abv": beer.abv,
                "ibu": beer.ibu,
            })
    elif language == "eng":
        for beer in beers:
            translated_beers.append({
                "name": beer.nome,
                "style": beer.estilo,
                "description": beer.descricao,
                "label": beer.rotulo,
                "abv": beer.abv,
                "ibu": beer.ibu,
            })
    return translated_beers

@router.get("/cervejas-caracteristicas", response_model=List[Dict])
def get_beers(
    caracteristica: str,
    limiar: float = 0.1,
    limite: int = 10,
    language: str = Query("eng", regex="^(eng|pt-br)$")
) -> List[Dict]:
    try:
        caracteristica = translate_input(caracteristica, language)
        beers = beer_service.find_beers_by_characteristic(caracteristica, limiar)
        if not beers:
            raise HTTPException(status_code=404, detail="Cervejas não foram encontradas com essas caracteristicas")
        beers = beers[:limite]
        beers = translate_output(beers, language)
        return beers
    except HTTPException as e:
        raise e

@router.post("/treinar-modelo")
def train_model() -> Dict[str, str]:
    beer_service.train_model()
    return {"mensagem": "Modelo treinado com sucesso!"}