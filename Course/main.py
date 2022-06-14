import time, api_service
from pprint import pprint
import os

def open_token(filename:str):
    with open(f'{os.getcwd()}/{filename}', "r") as token_in_file:
        token = token_in_file.read().strip()
        return token

path = 'files'
ya_path = 'course'
url = 'https://api.vk.com/method/'

os.system('cls||clear')

vk_import = api_service.VKservice(url, open_token('token.txt'))
vk_import.request_get()

YA_export = api_service.YaUploader(open_token('token_yandex.txt'))

YA_export.upload_file_to_disk(ya_path)

# api_service.write_json(photo['sizes'])