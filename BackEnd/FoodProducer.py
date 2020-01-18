from BackEnd.food import Food


class FoodProducer:
    def __init__(self):
        self.foods = []
        self.load()

    def load(self):
        pass

    def get_food(self, food_name: str) -> Food:
        for food in self.foods:
            if food.name == food_name:
                return food

        # now we just create a new food for now. in reality we would have to scrape at this point
        return self.add_food(food_name)

    def add_food(self, food_name: str) -> Food:
        f = Food(food_name)
        self.foods.append(f)
        return f
