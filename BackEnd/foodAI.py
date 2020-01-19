"""uses word2vec to give a list of similar foods."""

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
            """
        returns a list (no duplicates) of similar foods
        """

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

        # Multi word processing
        for recipe in all_foods:
            # List containing all word vectors
            vectors = None
            for word in recipe.name.split(' '):
                if vectors is None:
                    vectors = self.model(word).vector
                else:
                    vectors = np.dstack((self.model(word).vector, vectors))
            min = np.amin(vectors, axis=1)
            max = np.amax(vectors, axis=2)
            maxmin = np.stack([min, max])
            database.append(maxmin)
            # vec = self.model(recipe.name).vector
            # database.append(vec)

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
        """Returns the 15 recipe indices/ids"""
        term = self.model.vocab[term]
        D, I = self.index.search(np.array([term.vector]), 30)
        print(D)
        print(I)
        return I[0]

#
# if __name__ == '__main__':
#     thing = FoodAi(foodProducer.FoodProducer())
#     print(thing.get_similar_foods('pasta', 15))
#     print(thing.search_index('pizza'))
