import jsonpickle


class Food:
    _id_counter = 0

    def __init__(self, name: str, image_url: str, recipe_url: str, recipe_html: str, fat_level: str, salt_level: str,
                 saturates_level: str, sugars_level: str):
        self.id = Food._id_counter
        Food._id_counter += 1
        self.name = name
        self.image_url = image_url
        self.recipe_url = recipe_url
        self.recipe_html = recipe_html
        self.fat_level = fat_level
        self.salt_level = salt_level
        self.saturates_level = saturates_level
        self.sugars_level = sugars_level

    def toJson(self):
        return jsonpickle.encode(self)