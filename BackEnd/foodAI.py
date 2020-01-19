"""uses spacy to give a list of similar foods."""
import spacy
from typing import List
import faiss
import foodProducer
import pickle
import os.path
import numpy as np


class FoodAi:
    """
    import artificialintelligence as ai
    ai.dotheworkforme()"""

    def __init__(self, foodprod):
        """Load spacy model from dataset"""
        self.model = spacy.load("en_core_web_md")
        self.foodprod = foodprod
        self.index = self.create_index()

    def get_similar_foods(self, word: str, topn: int) -> List[str]:
        """Outdated: returns a list (no duplicates) of similar foods"""
        word = self.model.vocab[word]
        queries = [w for w in word.vocab if
                   w.is_lower == word.is_lower and w.prob >= -15]
        by_similarity = sorted(queries, key=lambda w: word.similarity(w),
                               reverse=True)
        return [w.lower_ for w in by_similarity[:topn + 1]
                if w.lower_ != word.lower_]

    def create_index(self):
        """ Creates index in Faiss."""
        # Get word embeddings from model
        xb = self.create_database()

        index = faiss.IndexFlatL2(600)  # build the index
        print(index.is_trained)
        index.add(xb)  # add vectors to the index
        print(index.ntotal)
        return index

    def create_database(self):
        """Make xb database using spacy"""
        if os.path.exists('database'):
             return self.load_database()
        print("Creating new database...")
        database = []
        all_foods = self.foodprod.foods
        for recipe in all_foods:
            vec = self.model(recipe.name).vector
            database.append(vec)

        # Save to file
        with open('database', 'wb') as f:
            pickle.dump(database, f)

        return np.array(database)

    def load_database(self):
        """Load xb database from file"""
        print("Loading database from file")
        with open('database', 'rb') as f:
            database = pickle.load(f)
        return np.array(database)

    def search_index(self, term: str):
        """Returns 30 recipe indices/ids"""
        terms = term.split(" ")
        possibilites = []
        for t in terms:
            term = self.model.vocab[t]
            D, I = self.index.search([np.hstack([term.vector, term.vector])], 30 // len(terms))
            possibilites.extend(I[0])
        return possibilites


if __name__ == '__main__':
    thing = FoodAi(foodProducer.FoodProducer())
    print(thing.search_index('pizza'))
