import requests
from pprint import pprint

superhero_list = ["Hulk", "Captain America", "Thanos"]
heroes_intelligence = []

def open_token(filename:str):
    with open(filename , "r") as token_in_file:
        token = token_in_file.read().strip()
        return token

open_token("token.txt")

for superheho in superhero_list:
    url = (f'https://superheroapi.com/api/{open_token("token.txt")}/search/{superheho}/')
    resp = requests.get(url).json()
    for hero in resp["results"]:
        if hero["name"] == superheho:
            heroes_intelligence.append([superheho , hero["powerstats"]["intelligence"]])
heroes_intelligence = sorted(heroes_intelligence, key=lambda x: x[0], reverse=True)
print(heroes_intelligence[0])

