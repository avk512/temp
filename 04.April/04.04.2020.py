import os
import json
import requests
from pprint import pprint

URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {
    'Authorization': 'OAuth AgAAAAAB9fBVAAZDy-BQ8R0t00G8jf5Kq6G9RNE',
    'Content-Type': 'application/json',
}
params = {
    'path': 'test.txt',
    'overwrite': 'true',
}

# def open_file(dir_input):
#     fname = os.listdir(dir_input)  # список имен файлов в папке
#     full_fname = os.path.join(os.path.abspath(dir_input), fname)
#     with open(full_fname, 'rb', encoding='UTF-8') as fn:
#         fopened = fn.read()
#     return fopened
#
#
# one = open_file('texts_out')

resp = requests.get(URL, headers=headers, params=params)
resp_json = resp.json()
print(resp_json['href'])

resp_upload = requests.put(resp_json['href'], 'text_out/FR-Ru.txt')

# resp_two = requests.put()
# resp = requests.get(URL, headers=headers, params=params)
# resp_json = resp.json()
# pprint(resp_json)


# pprint(resp_json['items'])
# fil = resp_json['items']
# pprint(fil)
# for item in fil:
#     pprint(item['name'])
# list_a = resp_json['_embedded']['items']
# # pprint(list_a)
# for item in list_a:
#     print(f"Объект '{item['name']}' создан {item['created']}")
# used_space = resp_json['used_space']
# total_space = resp_json['total_space']
# print(f"Занято: {used_space} байт")
# print(f"Использовано: {total_space} байт")
# print(f"Свободно {round((total_space - used_space) * (0.0009765625 ** 3), 1)} Гб")
# print((b))
# kb = b * 0.0009765625
# mb = kb * 0.0009765625
# gb = mb * 0.0009765625
# print(f"{round(kb, 2)} Kb")
# print(f"{round(mb, 2)} Mb")
# print(f"{round(gb, 2)} Gb")
