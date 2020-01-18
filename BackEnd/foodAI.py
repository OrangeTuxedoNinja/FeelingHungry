"""uses word2vec to give a list of similar foods."""
import gensim
import tempfile
from gensim.models import word2vec
import gensim.downloader as api


def generate_model():
    """save model to file, hopefully"""

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

    return gensim.models.Word2Vec.load("model")


def get_similar_foods(model, food: str, num_results: int):
    """
    returns a list (no duplicates) of similar foods
    """
    foods = list(set(model.similar_by_word(food, num_results)))
    print(foods)
