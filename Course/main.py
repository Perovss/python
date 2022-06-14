import time, api_service
from pprint import pprint
import os
with open('token.txt' , "r") as token_in_file:
    token = token_in_file.read().strip()
path="files"
url = "https://api.vk.com/method/"

os.system('cls||clear')

hello = api_service.VKservice(url, token)
hello.request_get()
# api_service.download_photo(hello.request_get(), path)

# api_service.download_photo(url, path)