from typing import List
from bs4 import BeautifulSoup
from food import Food
import requests

class Crawler:
    def __init__(self):
        pass

    def get_food(self, name: str) -> List[Food]:
        req = requests.get("https://www.epicurious.com/search/" + name + "?content=recipe")
        print(req)
        bs = BeautifulSoup(req.text, "html.parser")
        items = bs.select(".recipe-content-card")