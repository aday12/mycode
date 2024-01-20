# !usr/bin/env python3
# same code
import requests
from flask import Flask
from flask import render_template

# This project is mostly to work with API's. As such a stretch goal is to incorperate dynamic age calculation based on date of user input
# another stretch goal is to incorperate Pandas and cookies
# stretch goal: dynamically calculate age with birth year

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/<name>", methods = ["POST", "GET"])
# def name(name):
#    return render_template("name.html", name = name)

# @app.route("/gen/<age>", methods =  ["POST", "GET"])
# def generation(age):
#    return render_template("age.html", user_age=age)

@app.route("/year/<bday>", methods = ["POST", "GET"])
def year(bday):
    api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}'.format(bday)
    response = requests.get(api_url, headers={'X-Api-Key': 'QNYrADBFchwxcIyRQShmlA==JfMRdFvbWhHc5GFz'})
    if response.status_code == requests.codes.ok:
        return render_template("gen.html", year = response.text)

# this is the main function
def main():
    # fires the generation function from above
    name()
    generation()
    year()
    # main only works if the user is inside of the main funciton
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 2224)
