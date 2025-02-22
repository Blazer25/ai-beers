from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class BeerAI:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = None

    def train(self, beers):
        descriptions = [beer.description for beer in beers]
        self.model = self.vectorizer.fit_transform(descriptions)

    def predict(self, beers, characteristic):
        characteristic_vector = self.vectorizer.transform([characteristic])
        similarities = cosine_similarity(characteristic_vector, self.model)
        indices = np.argsort(similarities[0])[::-1]  # Ordena os índices pela similaridade
        return [beers[i] for i in indices]