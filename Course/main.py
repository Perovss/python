import time
import requests
from pprint import pprint
with open('token.txt' , "r") as token_in_file:
    token = token_in_file.read().strip()

def request_get():
    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': '4321910',
        'access_token': token,
        'v': '5.131',
        'album_id': 'profile',
        'count': 300,
        'extended': '1'
        # 'fields': 'education,sex'
    }
    res = requests.get(URL, params=params).json()
    photos = res['response']['items']
    for photo in photos:
        file_dir = (photo['sizes'])
        likes = (photo['likes'])
        for qwert in file_dir:
            if qwert['type'] == 'z':
                print(qwert['url'])
                print(likes['count'])


request_get()
# def group_search(q, sorting=0):
#     params = {
#         'q': q,
#         'access_token': token,
#         'v': '5.131',
#         'sort': sorting,
#         'count': 300
#     }
#     req = requests.get("https://api.vk.com/method/groups.search", params).json()
#     req = req['response']['items']
#     return req
# target_group = group_search("python")
# # pprint(target_group)
# # target_group_ids = ','.join([str(group['id']) for group in target_group])
# # pprint(target_group_ids)