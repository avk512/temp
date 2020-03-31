import requests
import os
import json

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20200331T164239Z.ec4eb58b5568079e.e7d2adf2434d9f6a15c2005521187654e1f2e954'


# 1-я функция: загружает тексты из файлов
# 2-я функция: осуществляет перевод текстов
# 3-я фукнция: записывает переводы в файлы

def open_file(source):
    pass


def translate_it(text):
    params = {
        'key': 'API_KEY',
        'text': 'text',
    }


def write_file(destination):
    pass
