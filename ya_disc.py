
import requests

with open('ya_token.txt', 'r') as file_object_ya:
    token_ya = file_object_ya.read().strip()


def upload_path(new_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    parametrs = {'path': new_path}
    headers = {'Authorization': f'OAuth {token_ya}'}
    response = requests.put(url, params=parametrs, headers=headers)
    return response


def delete_folder(new_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token_ya}'}
    parametrs = {'path': new_path}
    response = requests.delete(url, headers=headers, params=parametrs)
    return response


def last_uploaded(new_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token_ya}'}
    parametrs = {'path': f'disk:/{new_path}'}
    response = requests.get(url, headers=headers, params=parametrs)
    return response


if __name__ == "__main__":
    pass
