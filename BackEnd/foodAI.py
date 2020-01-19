"""uses word2vec to give a list of similar foods."""

import spacy
from typing import List
import faiss


class FoodAi:
    """
import artificialintelligence as ai
ai.dotheworkforme()
    """

    def __init__(self):
        """Load spacy model from dataset"""
        self.model = spacy.load("en_core_web_md")

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
        pass


if __name__ == '__main__':
    thing = FoodAi()
    print(thing.get_similar_foods('pasta', 15))
    #
    # get_similar_foods(model, 'pasta', 10)
