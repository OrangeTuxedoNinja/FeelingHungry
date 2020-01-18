from typing import List
from bs4 import BeautifulSoup
from food import Food
import requests


class Crawler:
    def __init__(self):
        pass

    @staticmethod
    def get_food(name: str) -> List[Food]:
        print("Running the crawler")
        req = requests.get("https://www.epicurious.com/search/" + name + "?content=recipe")
        bs = BeautifulSoup(req.text, "html.parser")
        articles = bs.select(".recipe-content-card")
        foods = []
        for i in range(min(5, len(articles))):
            article = articles[i]
            html_name = article.select(".hed")[0]
            f_name = html_name.text
            print("Scanning article: " + f_name)
            url = "https://www.epicurious.com" + html_name.find_all("a")[0]["href"]
            recipe = requests.get(url)
            recipe_bs = BeautifulSoup(recipe.text, "html.parser")
            for pimg in recipe_bs.find_all("img"):
                if "alt" in pimg.attrs and name in pimg["alt"]:
                    img = pimg
            if img is not None:
                iurl = img["srcset"]
            else:
                print("No image found!")
                iurl = "https://elitescreens.com/images/product_album/no_image.png"
            html_recipe = recipe_bs.select(".recipe-content")
            food = Food(f_name, iurl, url, html_recipe)
            foods.append(food)
        return foods
