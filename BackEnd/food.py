import jsonpickle
import requests
import json
from typing import Optional
import urllib.parse
import re
from random import randint
from imageFinder import *


class Food:
    _id_counter = 0

    def __init__(self, name: str, image_url: Optional[str], recipe_url: str, recipe_html: str, fat_level: str, salt_level: str,
                 saturates_level: str, sugars_level: str):
        self.id = Food._id_counter
        Food._id_counter += 1
        self.name = str.join(" ", [word for word in name.split(" ") if not re.search(r'[\d,#:()]', word.strip())])
        self.image_url = image_url
        self.recipe_url = recipe_url
        # self.recipe_html = recipe_html
        self.fat_level = fat_level
        self.salt_level = salt_level
        self.saturates_level = saturates_level
        self.sugars_level = sugars_level
        if self.how_healthy() < 8:
            self.num_leaves = 1
        elif self.how_healthy() < 13:
            self.num_leaves = 2
        else:
            self.num_leaves = 3

    def to_json(self) -> str:
        return jsonpickle.encode(self)

    def find_image(self, type: str) -> None:
        """find_image finds an image for this food"""
        self.image_url = search(type, 1)

    def how_healthy(self) -> int:
        """Returns a numerical value of how healthy an item is between 0-12"""
        def get_level(level: str) -> int:
            """Maps the string descriptions of healthiness to numerical"""
            if level == "green":
                return 3
            elif level == "orange":
                return 2
            elif level == "red":
                return 0
            else:
                raise Exception
        return round(get_level(self.fat_level) + get_level(self.sugars_level) * 1.5 + get_level(self.salt_level) + get_level(self.saturates_level) * 1.5)
