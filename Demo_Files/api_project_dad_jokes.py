# Colored Text

import termcolor
from pyfiglet import Figlet
f = Figlet(font='5lineoblique')
x = f.renderText("Dad Joke 3000")
print(termcolor.colored(x, "magenta"))

# API request
import requests

import requests


def get_input():
    print("Let me tell you a joke! Give me a topic: ")
    topic = input()
    return topic

topic = get_input()

# Get API

url = 'https://icanhazdadjoke.com/search'
response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': topic}
)

data = response.json()

if data['total_jokes']>1:
    print(f"I've got {data['total_jokes']} jokes, here's one: {data['results'][0]['joke']}")
elif data['total_jokes']==1:
    print(f"Here's one: {data['results'][0]['joke']}")
else:
    print("Sorry no jokes")
