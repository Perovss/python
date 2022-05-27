import requests
from pprint import pprint
with open("token.txt" , "r") as token_in_file:
    token = token_in_file.read().strip()
print(token)
url = "http://feron.ru/"
resp = requests.get(url)
pprint(type(resp))