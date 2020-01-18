"""uses word2vec to give a list of similar foods."""

import gensim
import tempfile
from gensim import models
import gensim.downloader as api

import spacy



class FoodAi:
    def __init__(self):
        """Load spacy model from dataset"""
        self.model = spacy.load("en_core_web_md")


        loaded = api.load('word2vec-google-news-300')
        for i, word in enumerate(loaded.vocab):
            if i == 10:
                break
            print(word)

        with tempfile.NamedTemporaryFile(prefix='gensim-model-',
                                         delete=False) as tmp:
            temporary_filepath = tmp.name
            loaded.save(temporary_filepath)
            #
            # The model is now safely stored in the filepath.
            # You can copy it to other machines, share it with others, etc.
            #
            # To load a saved model:
            print(temporary_filepath)
        print("Generated model!")
        return loaded


def load_model():
    """
    loads model from file.
    """
    print("Loading model from file...")

    w = models.Word2Vec.load_word2vec_format(
        'GoogleNews-vectors-negative300.bin', binary=True)
    w = models.KeyedVectors.load_word2vec_format('model', binary=True)
    return w # gensim.models.Word2Vec.load("model")


# def get_similar_foods(word: str, topn: int):
#     """
#     returns a list (no duplicates) of similar foods
#     """
#
#     word = nlp.vocab[str(word)]
#     queries = [w for w in word.vocab if
#                w.is_lower == word.is_lower and w.prob >= -15]
#     by_similarity = sorted(queries, key=lambda w: word.similarity(w),
#                            reverse=True)
#     return [(w.lower_, w.similarity(word)) for w in by_similarity[:topn + 1]
#             if w.lower_ != word.lower_]


if __name__ == '__main__':
    model = load_model()
    #
    # get_similar_foods(model, 'pasta', 10)

