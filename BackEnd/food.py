import jsonpickle
import requests
import json
from typing import Optional
import urllib.parse
import re

class Food:
    _id_counter = 0

    def __init__(self, name: str, image_url: Optional[str], recipe_url: str, recipe_html: str, fat_level: str, salt_level: str,
                 saturates_level: str, sugars_level: str):
        self.id = Food._id_counter
        Food._id_counter += 1
        self.name = str.join(" ", [word for word in name.split(" ") if not re.search(r'[\d,#]', word.strip())])
        self.image_url = image_url
        self.recipe_url = recipe_url
        self.recipe_html = recipe_html
        self.fat_level = fat_level
        self.salt_level = salt_level
        self.saturates_level = saturates_level
        self.sugars_level = sugars_level

    def toJson(self):
        return jsonpickle.encode(self)

    def findImage(self, type: str) -> None:
        """Finds a image of this food using pixabay api. If it cant find an image it uses type"""
        url = "https://pixabay.com/api/?key=14958320-84c9a72858b2f32099b33d787&q=" + urllib.parse.quote(self.name) + "&image_type=photo"
        print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        if len(data["hits"]) != 0:
            url = data["hits"][0]["previewURL"]
            self.image_url = url
            return
        url = "https://pixabay.com/api/?key=14958320-84c9a72858b2f32099b33d787&q=" + urllib.parse.quote(type) + "&image_type=photo"
        print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        if len(data["hits"]) != 0:
            url = data["hits"][0]["previewURL"]
            self.image_url = url
            return

