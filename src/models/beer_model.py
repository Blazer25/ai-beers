from pydantic import BaseModel

class Beer(BaseModel):
    name: str
    style: str
    abv: float
    ibu: float
    description: str
    labels: str = ""