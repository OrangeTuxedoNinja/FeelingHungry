from typing import List
from bs4 import BeautifulSoup
from food import Food
from random import randint
import requests


class Crawler:
    def __init__(self):
        self.searched = []

    def get_food(self, search_name: str) -> List[Food]:
        print("Running the crawler")
        modifiers = ["", "", "vegetarian", "vegan", "healthy", "high-fiber", "low-no-sugar", "low-fat",
                     "low-cholesterol", "low-sodium", "raw", "organic"]
        modifier = modifiers[randint(0, len(modifiers) - 1)]
        if modifier == "":
            req = requests.get("https://www.epicurious.com/search/" + search_name + "?content=recipe")
        else:
            req = requests.get("https://www.epicurious.com/search/" + search_name + "?special-consideration=" + modifier + "&content=recipe")

        bs = BeautifulSoup(req.text, "html.parser")
        articles = bs.select(".recipe-content-card")
        foods = []
        for i in range(min(5, len(articles))):
            article = articles[min(i + randint(0, 5), len(articles) - 1)]
            html_name = article.select(".hed")[0]
            f_name = html_name.text.strip()
            if f_name in self.searched:
                continue
            self.searched.append(f_name)
            print("Scanning article: " + f_name)
            url = "https://www.epicurious.com" + html_name.find_all("a")[0]["href"]
            recipe = requests.get(url)
            recipe_bs = BeautifulSoup(recipe.text, "html.parser")
            img = None
            images = recipe_bs.find_all("img")
            for pimg in images:
                if "alt" in pimg.attrs and (f_name[:10] in pimg["alt"] or "Photo by" in pimg["alt"]):
                    img = pimg
                    break
            if img is not None:
                if "srcset" not in img.attrs:
                    iurl = img["data-srcset"]
                else:
                    iurl = img["srcset"]
            else:
                print("No image found!")
                print(url)
                print(recipe_bs.find_all("img"))
                iurl = "https://elitescreens.com/images/product_album/no_image.png"
                continue
            html_recipe = recipe_bs.select(".recipe-content")[0].text
            food = Food(f_name, iurl, url, html_recipe, "green", "green", "green", "green")
            foods.append(food)
        return foods
