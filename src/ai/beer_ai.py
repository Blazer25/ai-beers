from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class BeerAI:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = None

    def train(self, beers):
        descriptions = [beer.descricao for beer in beers]
        self.model = self.vectorizer.fit_transform(descriptions)

    def predict(self, beers, caracteristica, limiar=0.1):
        characteristic_vector = self.vectorizer.transform([caracteristica])
        similarities = cosine_similarity(characteristic_vector, self.model)
        indices = np.argsort(similarities[0])[::-1]

        filtered_indices = [i for i in indices if similarities[0][i] is not None and similarities[0][i] >= limiar]
        return [beers[i] for i in filtered_indices]