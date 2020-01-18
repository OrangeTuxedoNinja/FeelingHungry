"""uses word2vec to give a list of similar foods."""
import spacy
from typing import List


class FoodAi:
    def __init__(self):
        """Load spacy model from dataset"""
        self.model = spacy.load("en_core_web_md")

    def get_similar_foods(self, food: str, num_results: int) -> List[str]:
        """
        returns a list (no duplicates) of similar foods
        """
        pass
