import requests, json, os, time
from pprint import pprint
from datetime import datetime
from progress.bar import IncrementalBar
dict_photo = {}
photo_list = []
file_list = []

def write_json(data):
    with open('photos.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_lagest(size_dict):
    weight = {'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 'm' : 10, 'x' : 20, 'y' : 30, 'z' : 40, 'w' : 50}
    size_dict['type'] = weight[size_dict['type']]
    return size_dict['type']

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
        bar = IncrementalBar('Выгрузка фото из VK', max = len(photos))
        for photo in photos:
            bar.next()
            time.sleep(1)
            write_json(photo['sizes'])
            sizes = (photo['sizes'])
            link_photo = max(sizes, key = get_lagest)['url']
            likes = (photo['likes'])['count']
            photo_list.append(likes)
            if likes in photo_list and photo_list.count(likes) >1:               
                likes = str(likes) +'_' +str(datetime.now().strftime("%Y-%m-%d %H-%M"))
            download_photo(link_photo, os.getcwd() + '/Files', likes)
        bar.finish()

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
    extension = res.url.split('.')[-1].split('?')[0]
    url = str(name) +'.'+str(extension)
    file_list.append(url)
    # Вычисление полного пути
    filepath = os.path.join(disk_file_path, url)

    # Сохраение файла в локальную папку disk_file_path
    with open(filepath, 'wb') as image:
        if res.ok:
            for content in res.iter_content(1024):
                if content:
                    image.write(content)

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)

        return response.json()

    def upload_file_to_disk(self,path, filename = file_list):
        bar = IncrementalBar('Загрузка фото из Yandex.Disc', max = len(file_list), )
        for filename in file_list:
            bar.next()
            time.sleep(1)
            disk_file_path = (f'{path}/{filename}')
            href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
            response = requests.put(href, data=open(f"{os.getcwd()}/Files/{filename}", 'rb'), timeout=10)
        bar.finish()
            # response.raise_for_status()
            # if response.status_code == 201:
            #     print(f"файл - {disk_file_path} загрузка выполнена.")
        
