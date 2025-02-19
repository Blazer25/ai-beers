import json
import os
import logging
from models.beer_model import Beer
from ai.beer_ai import BeerAI
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

logging.basicConfig(level=logging.INFO)

DATA_DIR = "beers"
beer_ai = BeerAI()

def load_beers():
    beers = []
    required_fields = ["name", "style", "abv", "ibu", "description"]

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as file:
                data = json.load(file)
                if "data" in data:
                    for beer_data in data["data"]:
                        for field in required_fields:
                            if field not in beer_data:
                                beer_data[field] = 0.0 if field in ["abv", "ibu"] else ""

                        if isinstance(beer_data.get("style"), dict):
                            beer_data["style"] = beer_data["style"].get("name", "")

                        if isinstance(beer_data.get("ibu"), str):
                            try:
                                beer_data["ibu"] = float(beer_data["ibu"])
                            except ValueError:
                                beer_data["ibu"] = 0.0

                        description = beer_data["description"].strip()
                        if description and not all(word in ENGLISH_STOP_WORDS for word in description.split()):
                            beers.append(Beer(**beer_data))
                        else:
                            logging.info(f"Descrição inválida no arquivo  {filename}: {description}")

    logging.info(f"Carregadas {len(beers)} cervejas válidas")
    return beers

def find_beers_by_characteristic(characteristic: str):
    beers = load_beers()
    return beer_ai.predict(beers, characteristic)

def train_model():
    beers = load_beers()
    valid_beers = [beer for beer in beers if beer.description and not all(word in ENGLISH_STOP_WORDS for word in beer.description.split())]
    if not valid_beers:
        raise ValueError("Sem cervejas válidas para treinar o modelo.")
    beer_ai.train(valid_beers)