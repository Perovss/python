import requests

class YaUploader:
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'), timeout=10)
        response.raise_for_status()
        if response.status_code == 201:
            print(f"файл - {disk_file_path} загрузка выполнена.")

