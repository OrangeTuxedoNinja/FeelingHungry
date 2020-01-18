from typing import List
from fuzzywuzzy import fuzz, process
from epicurcrawler import Crawler
import json


from food import Food


class FoodProducer:
    def __init__(self):
        self.foods = []
        self.load()

    def load(self):
        pass

    def get_food(self, food_id: str) -> Food:
        for food in self.foods:
            if food.id == food_id:
                return food
        return None

    def search_food(self, food_name: str) -> List[int]:
        ids = []
        c = 0
        while len(ids) <= 4:
            c += 1
            if c > 20:
                print("Could not find results")
                return [x.id for x in self.foods[:5]]
            try:
                print([n.name for n in self.foods])
                acc = {}

                # Do the ai thing
                names = process.extract(food_name, [x.name for x in self.foods], limit=5)


                print(names)
                for name in names:
                    acc[name[0]] = name[1]
                names = [name[0] for name in names]
                print(names)
                for food in self.foods:
                    if food.name in names and food.id not in ids:
                        if acc[food.name] > 50:
                            ids.append(food.id)
            except Exception:
                pass
            self.add_food(food_name)
        self.save()
        return ids

    def add_food(self, food_name: str) -> None:
        for new_food in Crawler.get_food(food_name):
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

