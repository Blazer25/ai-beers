from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from models.beer_model import Beer

class BeerAI:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = NearestNeighbors(n_neighbors=5)

    def train(self, beers: list[Beer]):
        descriptions = [beer.description for beer in beers]
        X = self.vectorizer.fit_transform(descriptions)
        self.model.fit(X)

    def predict(self, beers: list[Beer], characteristic: str):
        X = self.vectorizer.transform([characteristic])
        distances, indices = self.model.kneighbors(X)
        return [beers[i] for i in indices[0]]