import requests

class YaUploader:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.token = 'Yandex_token'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self):
        href = 'https://cloud-api.yandex.net/v1/disk/resources?' + f'path={self.folder_name}'
        headers = self.get_headers()
        response = requests.put(href, headers=headers)
        return response.status_code

    def remove_folder(self):
        href = 'https://cloud-api.yandex.net/v1/disk/resources?' + f'path={self.folder_name}'
        headers = self.get_headers()
        response = requests.delete(href, headers=headers)
        return response.status_code

    def check_folder(self):
        href = 'https://cloud-api.yandex.net/v1/disk/resources?' + f'path={self.folder_name}'
        headers = self.get_headers()
        response = requests.get(href, headers=headers)
        return response.status_code


