import jsonpickle
import requests
import json
from typing import Optional
import urllib.parse
import re
from random import randint

class Food:
    _id_counter = 0

    def __init__(self, name: str, image_url: Optional[str], recipe_url: str, recipe_html: str, fat_level: str, salt_level: str,
                 saturates_level: str, sugars_level: str):
        self.id = Food._id_counter
        Food._id_counter += 1
        self.name = str.join(" ", [word for word in name.split(" ") if not re.search(r'[\d,#:()]', word.strip())])
        self.image_url = image_url
        self.recipe_url = recipe_url
        self.recipe_html = recipe_html
        self.fat_level = fat_level
        self.salt_level = salt_level
        self.saturates_level = saturates_level
        self.sugars_level = sugars_level
        self.num_leaves = (self.how_healthy() + 1) // 3

    def toJson(self):
        return jsonpickle.encode(self)

    def findImage(self, type: str) -> None:
        """Finds a image of this food using pixabay api. If it cant find an image it uses type"""
        url = "https://pixabay.com/api/?key=14958320-84c9a72858b2f32099b33d787&q=" + urllib.parse.quote(self.name) + "&image_type=photo"
        response = requests.get(url)
        data = json.loads(response.text)
        if len(data["hits"]) != 0:
            url = data["hits"][0]["previewURL"]
            self.image_url = url
            return
        url = "https://pixabay.com/api/?key=14958320-84c9a72858b2f32099b33d787&q=" + urllib.parse.quote(type) + "&image_type=photo"
        response = requests.get(url)
        data = json.loads(response.text)
        if len(data["hits"]) != 0:
            url = data["hits"][min(randint(0, len(data["hits"]) / 2 + 1), len(data["hits"]) - 1)]["previewURL"]
            self.image_url = url
            print("Setting url to : " + url)
            return

    def how_healthy(self) -> int:
        """Returns a numerical value of how healthy an item is between 0-8"""
        def get_level(level: str) -> int:
            """Maps the string descriptions of healthiness to numerical"""
            if level == "green":
                return 0
            elif level == "orange":
                return 1
            elif level == "red":
                return 2
            else:
                raise Exception
        return get_level(self.fat_level) + get_level(self.sugars_level) + get_level(self.salt_level) + get_level(self.saturates_level)