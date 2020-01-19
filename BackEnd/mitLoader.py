import json
from typing import List
from food import Food
import foodProducer


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
            allow = True
            for namew in recipe["title"].split(" "):
                if namew.strip().lower() in foodProducer.banned:
                    allow = False
                    break
            if allow:
                name = recipe["title"]
                if len(name) < 26 and (len(name) <= 2 or (name[-1] == "s" and name[-2] != "s")):
                    if name[-3:] == "ies":
                        name = name[:-3] + "y"
                    name = name[:-1]
                    food.append(Food(name, None, recipe["url"], instructions, recipe["fsa_lights_per100g"]["fat"],
                                     recipe["fsa_lights_per100g"]["salt"], recipe["fsa_lights_per100g"]["saturates"], recipe["fsa_lights_per100g"]["sugars"]))

        return food
