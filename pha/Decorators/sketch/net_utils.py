from cache_tools import cached
from test_tools import make_trace
import datetime
import requests

HOST = 'https://swapi.dev/api/'

@cached(2)
def get_people(character_id):

    return requests.get(f'{HOST}people/{character_id}').json()

@make_trace
@cached(2)
def get_starship(starship_id):

    return requests.get(f'{HOST}starships/{starship_id}').json()


# start = datetime.datetime.now()
# get_people(1)

# print(datetime.datetime.now() - start)

# print('*' * 20)

# start = datetime.datetime.now()
# get_people(1)
# get_starship(2)
# print(datetime.datetime.now() - start)

get_starship(9)