from typing import List
from bs4 import BeautifulSoup
from food import Food
from random import randint
import requests


class Crawler:
    def __init__(self):
        pass

    @staticmethod
    def get_food(name: str) -> List[Food]:
        print("Running the crawler")
        modifiers = ["", "", "vegetarian", "vegan", "healthy", "high-fiber", "low-no-sugar", "low-fat",
                     "low-cholesterol", "low-sodium", "raw", "organic"]
        modifier = modifiers[randint(0, len(modifiers) - 1)]
        if modifier == "":
            req = requests.get("https://www.epicurious.com/search/" + name + "?content=recipe")
        else:
            req = requests.get("https://www.epicurious.com/search/" + name + "?special-consideration=" + modifier + "&content=recipe")

        bs = BeautifulSoup(req.text, "html.parser")
        articles = bs.select(".recipe-content-card")
        foods = []
        for i in range(min(5, len(articles))):
            article = articles[i]
            html_name = article.select(".hed")[0]
            f_name = html_name.text.strip()
            print("Scanning article: " + f_name)
            url = "https://www.epicurious.com" + html_name.find_all("a")[0]["href"]
            recipe = requests.get(url)
            recipe_bs = BeautifulSoup(recipe.text, "html.parser")
            img = None
            for pimg in recipe_bs.find_all("img"):
                if "alt" in pimg.attrs and f_name[:15] in pimg["alt"]:
                    img = pimg
            if img is not None:
                if "srcset" not in img.attrs:
                    print(img)
                iurl = img["srcset"]
            else:
                print("No image found!")
                print(url)
                print(recipe_bs.find_all("img"))
                iurl = "https://elitescreens.com/images/product_album/no_image.png"
            html_recipe = recipe_bs.select(".recipe-content")
            food = Food(f_name, iurl, url, html_recipe)
            foods.append(food)
        return foods
