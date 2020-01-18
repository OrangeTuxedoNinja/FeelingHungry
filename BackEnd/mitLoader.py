import json
from typing import List
from food import Food

class MitLoader:
    def __init__(self):
        pass

    def load(self) -> List[Food]:
        food = []
        #Load the mit data set with nutritional data
        with open('recipes_with_nutritional_info.json', 'r') as fp:
            recipes = json.loads(fp.read())
        for recipe in recipes:
            instructions = "<p>INGREDIENTS: </p>"
            for ingred in recipe["ingredients"]:
                instructions += "<p>" + ingred["text"] + "</p>"
            instructions += "<p> INSTRUCTIONS: </p>"
            for instruct in recipe["instructions"]:
                instructions += "<p>" + instruct["text"] + "<\p>"
            food.append(Food(recipe["title"], "www.google.com", recipe["url"], instructions, recipe["fsa_lights_per100g"]["fat"],
                             recipe["fsa_lights_per100g"]["salt"], recipe["fsa_lights_per100g"]["saturates"], recipe["fsa_lights_per100g"]["sugars"]))

        return food
