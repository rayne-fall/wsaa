# assignment 2 - card draw
# author: Sylvia Chapman Kent
# deals five cards from a deck and prints the value and suit of each card

import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/draw/?count=5"
response = requests.get(url)
data = response.json()
#print(response.json())
cards = data["cards"]
result = cards["value"]["suit"]
print(result)