import requests
from pprint import pprint

# resp = requests.get("https://google.com")
# print(resp.status_code)
# print(resp.text)

# Поиск в каталоге ITunes песни исполнителя Монеточки и обложку ее альбома
# Нас могут интересовать следующие параметры для запроса
# - term (текстовая строка, которую нужно найти, обязательный параметр)
# - country (выбор страны RU, обязательный параметр)
# - media (тип контента, музыка music в данной ситуации)
# - limit (ограничение запроса, максимально 200)

# запрос URL-а для поиска
ITUNES_URL = 'https://itunes.apple.com/search'

# задание нескольких параметров для строки запроса (в виде словаря)
params = {
    'term': 'Монеточка',
    'country': 'RU',
    'media': 'music',
    'limit': 200
}

resp = requests.get(ITUNES_URL, params=params)

resp_json = resp.json()
