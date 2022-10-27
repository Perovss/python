import requests
from pprint import pprint
from datetime import datetime
from yandex_disc import YaUploader

def open_token(filename:str):
    with open(filename , "r") as token_in_file:
        token = token_in_file.read().strip()
        return token

def task1():
    token = open_token("token.txt")
    superhero_list = ["Hulk", "Captain America", "Thanos"]
    heroes_intelligence = []

    for superheho in superhero_list:
        url = (f'https://superheroapi.com/api/{token}/search/{superheho}/')
        resp = requests.get(url).json()
        for hero in resp["results"]:
            if hero["name"] == superheho:
                heroes_intelligence.append([superheho , hero["powerstats"]["intelligence"]])
    heroes_intelligence = sorted(heroes_intelligence, key=lambda x: x[0], reverse=True)
    print(heroes_intelligence[0])

def task2():
    filename = 'result.txt'
    path_disk = 'request'
    token = open_token("token_yandex.txt")
    with open(filename , "w") as file:
        file.write(f'py-54 {datetime.today().strftime("%d/%m/%y %H:%M")}')
    uploader = YaUploader(token)
    uploader.upload_file_to_disk(path_disk+'/'+filename, filename)

if __name__ == '__main__':
    print("Задание 1: Кто самый умный супергерой?")
    task1()

    print("\nЗадание 2. Передача файла на Яндекс диск")
    task2()
    