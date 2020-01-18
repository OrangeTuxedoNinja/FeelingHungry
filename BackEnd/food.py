import json


class Food:
    _id_counter = 0

    def __init__(self, name: str):
        self.id = Food._id_counter
        Food._id_counter += 1
        self.name = name

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys= True, indent= 4)