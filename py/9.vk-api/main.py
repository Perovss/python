import time
import requests
from pprint import pprint
with open('token.txt' , "r") as token_in_file:
    token = token_in_file.read().strip()

def request_get():
    URL = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': '1,2,3,4,5,6,7,8,9,10',
        'access_token': token,
        'v': '5.131',
        'fields': 'education,sex'
    }
    res = requests.get(URL, params=params)
    pprint(res.json())

def group_search(q, sorting=0):
    params = {
        'q': q,
        'access_token': token,
        'v': '5.131',
        'sort': sorting,
        'count': 300
    }
    req = requests.get("https://api.vk.com/method/groups.search", params).json()
    req = req['response']['items']
    return req
target_group = group_search("python")
# pprint(target_group)
target_group_ids = ','.join([str(group['id']) for group in target_group])
pprint(target_group_ids)