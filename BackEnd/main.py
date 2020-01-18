from flask import Flask, render_template, redirect
app = Flask(__name__, template_folder="../FrontEnd")

path = "http://35.203.43.136:5000/"

@app.route('/main')
def hello_world():
    return 'test!'

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route("/")
def main_page():
    return redirect("http://127.0.0.1:5000/index")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
