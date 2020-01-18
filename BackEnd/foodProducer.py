from typing import List
from difflib import get_close_matches

from food import Food


class FoodProducer:
    def __init__(self):
        self.foods = []
        self.load()
        for name in ["apple", "burger", "veggie burger"]:
            self.add_food(name)

    def load(self):
        pass

    def get_food(self, food_id: str) -> Food:
        for food in self.foods:
            if food.id == food_id:
                return food
        return None

    def search_food(self, food_name: str) -> List[int]:
        names = get_close_matches(food_name, [x.name for x in self.foods])
        ids = []
        for food in self.foods:
            if food.name in names:
                ids.append(food.id)
        return ids

    def add_food(self, food_name: str) -> Food:
        f = Food(food_name)
        self.foods.append(f)
        return f
