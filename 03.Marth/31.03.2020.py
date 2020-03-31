import requests

url = 'https://translate.yandex.net/api/v1/tr.json/translate'

params = {
    'lang': 'ru-en',
    'srv': 'tr-text',
    'id': 'c924f578.5e831559.501041fe-2-0'
}

data = {
    'text': 'Великолепно!'
}

resp = requests.post(url, params=params, data=data)

resp_json = resp.json()
print(resp_json)
print(resp_json['text'])
