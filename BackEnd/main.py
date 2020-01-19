from flask import Flask, render_template, redirect, jsonify
from food import Food
from foodProducer import FoodProducer
from flask_cors import CORS
import requests

app = Flask(__name__,static_url_path='',  template_folder="../FrontEnd", static_folder="../FrontEnd")
foodset = FoodProducer()
CORS(app)

# path = "35.203.43.136"
# local = "127.0.0.1"


@app.route('/main')
def hello_world():
    return 'test!'


# @app.route('/<string:page_name>/')
# def render_static(page_name):
#     print("Getting: " + page_name)
#     return render_template('%s' % page_name)


@app.route("/")
def main_page():
    return render_template('index.html')


@app.route("/api/search/<string:food>")
def search_food(food):
    result = foodset.search_food(food)
    print("Foodset search: " + str(result))
    return jsonify(result)


@app.route("/api/food/<string:id>")
def get_food(id: str):
    food = foodset.get_food(int(id))
    if food is None:
        return {}
    return food.toJson()


@app.route("/api/link/<string:id>")
def does_site_load(id: str):
    f = foodset.get_food(int(id))
    req = requests.get(f.recipe_url)
    if "X-Frame-Options" not in req.headers:
        return "True"
    elif req.headers["X-Frame-Options"].strip().lower() in ["deny", "sameorigin"]:
        return "False"
    return "True"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
