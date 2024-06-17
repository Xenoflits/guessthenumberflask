from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)

@app.route('/')
def sample():
    return("<h1>Guess a number between 0-9 by adding your guess to the url</h1>")

@app.route('/<number>')
def check_number(number):
    number = int(number)
    if number == random_number:
        return "<h1>you have guessed correctly</h1>" 
    elif number < random_number:
        return "<h1>higher</h1>"
    elif number > random_number and number < 10:
        return "<h1>lower</h1>"
    else:
        return "<h1> needs to be between 0 and </h1>"

app.run(debug=True)
