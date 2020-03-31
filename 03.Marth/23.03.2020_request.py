import requests
from pprint import pprint
import os

resp = requests.get("https://google.com")
print(resp.status_code)
print(resp.text)

# Поиск в каталоге ITunes песни исполнителя Монеточки и обложки ее альбома
# Нас могут интересовать следующие параметры для запроса
# - term (текстовая строка, которую нужно найти, обязательный параметр)
# - country (выбор страны RU, обязательный параметр)
# - media (тип контента, музыка music в данной ситуации)
# - limit (ограничение запроса, максимально 200)

# запрос URL-а для поиска
ITUNES_URL = 'https://itunes.apple.com/search'
#
# задание параметров для строки запроса (в виде словаря)
params = {
    'term': 'Монеточка',
    'country': 'RU',
    'media': 'music',
    'limit': 200
}

headers = {
    'User-Agent': 'Python Netology'
}

# передача запроса
resp = requests.get(ITUNES_URL, params=params, headers=headers)

resp_json = resp.json()

for track in resp_json['results']:
    print('*' * 30)
    pprint(track)

    track_id, track_name, artist = track['trackId'], track['trackName'], \
                                   track['artistName']
    file_name = f'{track_id}-{track_name}-{artist}.jpg'
    full_file_name = os.path.join('covers', file_name)
    # f_movie_name = f'{track_name}-{track_name}-{artist}.m4v'
    # full_movie_name = os.path.join('movies', f_movie_name)
    print("Filename image: ", full_file_name)
    # print("Filename movie: ", full_movie_name)

    with open(full_file_name, 'wb') as f:
        img_url = track['artworkUrl100']
        img_file_resp = requests.get(img_url)
        img = img_file_resp.content
        f.write(img)

    # with open(full_movie_name, 'wb') as f:
    #     mv_url = track['previewUrl']
    #     mv_file_resp = requests.get(mv_url)
    #     mv = mv_file_resp.content
    #     f.write(mv)
#
### ВТОРОЙ ПРИМЕР ИЗ ВЕБИНАРА в файле translate-it.py ###
