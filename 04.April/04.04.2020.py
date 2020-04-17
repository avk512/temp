import os
import json
import requests
from pprint import pprint

URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {
    'Authorization': 'OAuth AgAAAAAB9fBVAAZDy-BQ8R0t00G8jf5Kq6G9RNE',
    'Content-Type': 'application/json',
}


def files_name(dir_input):
    """Получение списка файлов в исходной папке"""
    fname = os.listdir(dir_input)  # список имен файлов в папке
    print(
        f"Готовятся к загрузке файлы: \n{fname}\n")  # ['DE-Ru.txt', 'ES-Ru.txt', 'FR-Ru.txt']
    return fname


def fls(func_files_name):
    for file in func_files_name:
        return file


params = {
    # 'path': 'test.txt',
    'path': fls(files_name('texts_out')),
    'overwrite': 'true',
}


# def fls(func_files_name):
#     fname = func_files_name()  # ['DE-Ru.txt', 'ES-Ru.txt', 'FR-Ru.txt']


# resp = requests.get(URL, headers=headers, params=params)
# resp_json = resp.json()
# print(resp_json['href'])  # ссылка для загрузки файла


def main():
    fname = files_name('texts_out')  # ['DE-Ru.txt', 'ES-Ru.txt', 'FR-Ru.txt']
    resp = requests.get(URL, headers=headers, params=params)
    resp_json = resp.json()
    for file in fname:
        print(resp_json['href'])  # ссылка для загрузки файла
        # print(file)
        resp_upload = requests.put(resp_json['href'], file)


if __name__ == '__main__':
    main()
