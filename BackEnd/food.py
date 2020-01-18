import json


class Food:
    _id_counter = 0

    def __init__(self, name: str, image_url: str, recipe_url: str, recipe_html: str):
        self.id = Food._id_counter
        Food._id_counter += 1
        self.name = name
        self.image_url = image_url
        self.recipe_url = recipe_url
        self.recipe_html = recipe_html

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys= True, indent= 4)