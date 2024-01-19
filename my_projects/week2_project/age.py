# !usr/bin/env python3
# same code
import requests
from pprint import pprint
from flask import Flask
from flask import render_template

# This project is mostly to work with API's. As such a stretch goal is to incorperate dynamic age calculation based on date of user input
# another stretch goal is to incorperate Pandas and cookies

app = Flask(__name__)


@app.route("/")
def name():
    while True:
        try:
            user_name=input("Hi! What's your name?\n>").strip().title()
            return(f"\nHi, {user_name}!")
            break
        except TypeError:
            return("\nPlease only input a valid name. For example: Aaron, Hutch, Michael Jordan, ajlkdjhfklajsdf")

def generation():
    while True:
        try:
            user_age=int(input("\nHow old are you? (As of December 31 2023)\n>"))
    # this line sets user_age to the int of what the user inputs with blank spaces stripped from either side
            if user_age >= 123:
                return("\nYou're a member of the Lost Generation. That doesn't sound fun D:\n")
            elif user_age >= 96 and  user_age <= 122:
                return("\nYou're a member of the Greatest Generation, I salute you :D\n")
            elif user_age >= 77 and user_age <= 95:
                return("\nShhhhhhhhh, you're a member of the Silent Generation\n")
            elif user_age >= 59 and user_age <= 76:
                return("\nYOU'RE A BOOMER!!!!!!\n")
            elif user_age >= 43 and user_age <= 58:
                return("\nYou're a member of Gen X. AKA the Siltent Generation Part 2\n")
            elif user_age >= 27 and user_age <= 42:
                return("\nYou're a Millennial. Where were you for Y2K?\n")
            elif user_age >= 11 and user_age <= 26:
                return("\nWHAT'S UP ZOOMER?!?!?!\n")
            elif user_age > 0 and 11 > user_age: # this line is an example of an 
                # alterative way to write similar logic to the other if/elif statements
                return("\nThe future is yours Gen Alpha!\n")
            else:
                return("\nHmmm seems like maybe you hadn't arrived yet\n")
            break
        except TypeError:
            return("\nPlease enter a number. For example: 42, 58, 15 etc.")

def year():
    while True:
        text=int(input("\nWhat year were you born?\n>"))
        try:
            return(f"Here are some imortant things that happened in {text}:\n")
            api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}'.format(text)
            response = requests.get(api_url, headers={'X-Api-Key': 'QNYrADBFchwxcIyRQShmlA==JfMRdFvbWhHc5GFz'})
            if response.status_code == requests.codes.ok:
                pprint(response.text)
                break
        except TypeError:
            return("\nPlease enter a number. For example: 2002, 1996, 1843")

# this is the main function
def main():
    # fires the generation function from above
    name()
    generation()
    year()
    # main only works if the user is inside of the main funciton
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 2224, debug = True) # runs the app in debug mode
