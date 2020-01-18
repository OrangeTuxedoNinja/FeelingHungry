from typing import List, Optional
from fuzzywuzzy import fuzz, process
from epicurcrawler import Crawler
import json
from mitLoader import MitLoader


import os.path
from food import Food

banned = ["dough", "spice"]


class FoodProducer:
    def __init__(self):
        self.foods = []
        self.load()
        # self.word_model = api.load('glove-wiki-gigaword-50')
        self.cached_foods = {}
        self.crawler = Crawler()

    def get_food(self, food_id: str) -> Optional[Food]:
        for food in self.foods:
            if food.id == food_id:
                return food
        return None

    def search_food(self, food_name: str) -> List[int]:
        if food_name in self.cached_foods:
            return self.cached_foods[food_name]

        ids = []
        chosen = []
        c = 0
        score = 50
        while len(ids) <= 4:
            c += 1
            if c > 20:
                print("Could not find results")
                return [x.id for x in self.foods[:5]]
            try:
                acc = {}

                # Do the ai thing
                names = process.extract(food_name, [x.name for x in self.foods],
                                        limit=20)

                for name in names:
                    acc[name[0]] = name[1]
                names = [name[0] for name in names]

                for food in self.foods:
                    if food.name in names and food.id not in ids and food.name not in chosen and food.num_leaves >= 1:
                        if acc[food.name] > score:
                            ids.append(food.id)
                            chosen.append(food.name)
                            print(food.image_url)
                            print(type(food.image_url))
                            if food.image_url is None:
                                print("Loading image")
                                food.findImage(food_name)
                            if len(ids) == 5:
                                break
            except Exception:
                pass
            if len(ids) != 5:
                self.add_food(food_name)
                score -= 5

        self.cached_foods[food_name] = ids
        self.save()
        return ids

    def add_food(self, food_name: str) -> None:
        for new_food in self.crawler.get_food(food_name):
            if new_food.name not in [x.name for x in self.foods]:
                print("Added food: " + new_food.name)
                self.foods.append(new_food)

    def food_exists(self, food_name: str) -> bool:
        for food in self.foods:
            if food.name == food_name:
                return True
        return False

    def save(self):
        with open('foods.json', 'w') as fp:
            str_food = []
            for food in self.foods:
                str_food.append(food.toJson())
            json.dump(str_food, fp)

    def load(self):
        """Either loads the self.foods array from the self created foods.json save or recreates it using the MIT dataset"""
        if not os.path.isfile("foods.json"):
            loader = MitLoader()
            self.foods = loader.load()
            print("Loaded: " + str(len(self.foods)) + " foods from MIT data source")
            self.save()
            return

        with open('foods.json', 'r') as fp:
            x = json.load(fp)
            for i in x:
                r = json.loads(i)
                allow = True
                for namew in r["name"].split(" "):
                    if namew in banned:
                        allow = False
                        break
                if allow:
                    self.foods.append(Food(r["name"], r["image_url"], r["recipe_url"], r["recipe_html"], r["fat_level"], r["salt_level"], r["saturates_level"], r["sugars_level"]))
        print("Loaded: " + str(len(self.foods)))



