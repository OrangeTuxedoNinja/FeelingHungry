from flask import Flask, render_template, redirect, jsonify
from food import Food
from foodProducer import FoodProducer

app = Flask(__name__, template_folder="../FrontEnd")
foodset = FoodProducer()

path = "http://127.0.0.1:5000/"

@app.route('/main')
def hello_world():
    return 'test!'

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route("/")
def main_page():
    return redirect("http://127.0.0.1:5000/index")

@app.route("/api/search/<string:food>")
def search_food(food):
    return foodset.search_food(food).toJson()

@app.route("/api/food/<string:id>")
def get_food(food_id: str):

    return foodset.get_food(int(food_id)).toJson()


if __name__ == '__main__':
    app.run(host='35.203.43.136', debug=True, port=80)
