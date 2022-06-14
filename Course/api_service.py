import requests, json, os, time
from pprint import pprint
from datetime import datetime
dict_photo = {}
photo_list = []

def write_json(data):
    with open('photos.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_lagest(size_dict):
    weight = {'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 'm' : 10, 'x' : 20, 'y' : 30, 'z' : 40, 'w' : 50}
    size_dict['type'] = weight[size_dict['type']]
    return size_dict['type']
    # if size_dict['width'] >= size_dict['height']:
    #     return size_dict['width']
    # else:
    #     return size_dict['height']      


class VKservice:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def request_get(self):
        url_photos = self.url + 'photos.get'
        params = {
            'owner_id': '4321910',
            'access_token': self.token,
            'v': '5.131',
            'album_id': 'profile',
            'count': 100,
            'extended': '1'
        }
        res = requests.get(url_photos, params=params).json()
        photos = res['response']['items']
        for photo in photos:
            # write_json(photo['sizes'])
            sizes = (photo['sizes'])
            link_photo = max(sizes, key = get_lagest)['url']
            likes = (photo['likes'])['count']
            photo_list.append(likes)
            # print(link_photo)

            print(photo_list)
            # for qwert in sizes:
            #     if qwert['type'] == 'z':
            #         qwerty = {qwert['url']: likes['count']}
            #         dict_photo.update(qwerty)

            if likes in photo_list and photo_list.count(likes) >1:
                
                likes = str(likes) +'_' +str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


            download_photo(link_photo, 'Files', likes)

def download_photo(url, disk_file_path, name):
    """
    Функция скачивания файла по интернет ссылке url в папку disk_file_path
    @param url: url скачиваемого файла
    @param disk_file_path: локальная папка, куда будет скачан файл
    @return: полное имя файла, результат скачивания
    """
    # Скачивание файла
    res = requests.get(url, stream=True, allow_redirects=True)
 
    # Вычленение навзания файла
    # url = res.url.split('/')[-1].split('?')[0]
    url = str(name) +'.jpg'

    # Вычисление полного пути
    filepath = os.path.join(disk_file_path, url)

    # Сохраение файла в локальную папку disk_file_path
    with open(filepath, 'wb') as image:
        if res.ok:
            for content in res.iter_content(1024):
                if content:
                    image.write(content)
