import requests
from pprint import pprint

URL = 'https://translate.yandex.net/api/v1/tr.json/translate'

params = {
    'lang': 'ru-en',
    'srv': 'tr-text',
    'id': '370877e7.5e7a33d7.b815dee8-1-0'
}

data = {
    'text': 'Очень сложно'
}

resp = requests.post(URL, params=params, data=data)
resp_json = resp.json()
print(resp_json)
print(resp_json['text'])
