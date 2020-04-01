import requests
import os
import json

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20200331T164239Z.ec4eb58b5568079e.e7d2adf2434d9f6a15c2005521187654e1f2e954'


# 1-я функция: получает список абсолютных путей к файлам с текстами
# 2-я функция: загружает тексты из файлов
# 3-я функция: осуществляет перевод текстов
# 4-я фукнция: записывает переводы в файлы

def path_to_files(dir_input):
    """dir_input = 'texts_in'  # исходная директория с файлами"""
    ffn = []  # список абсолютных путей к файлам
    fls = os.listdir(dir_input)  # список имен всех файлов в директории
    print(f"В папке [{dir_input}] найдено {len(fls)} файла:")
    print('-' + '\n-'.join(fls) + '\n')
    # print("Путь к файлам (абсолютный путь):")
    for fname in fls:
        full_file_name = os.path.join(os.path.abspath(dir_input), fname)
        # print(full_file_name)
        ffn.append(full_file_name)
    return ffn


def open_file(fname):
    """Открываем файл и читаем его весь целиком"""
    with open(fname, encoding='UTF-8') as fn:
        f = fn.read()
    return f


def translate_it(func_open_files):
    """Переводим текст из считанного файла"""
    params = {
        'key': API_KEY,
        'text': func_open_files,
        'lang': 'ru',
    }
    resp = requests.get(URL, params=params)
    resp_json = resp.json()
    # print(resp_json['code'])
    # print(resp_json['lang'])
    # print(resp_json['text'])
    return ''.join(resp_json['text'])


# def write_files(func_translate_it, dir_output):
def write_files(func_translate_it):
    """Сохраняем переводы в новых файлах"""
    dir_input = 'texts_in'
    dir_output = 'texts_out'
    a = []
    fls = os.listdir(dir_input)
    print(fls)
    for name in fls:
        file_name = os.path.splitext(name)
        # print(file_name)    # кортежи из имени и расширения по-отдельности
        fn = f'{file_name[0]}-Ru.txt'
        full_file_name = os.path.join(dir_output, fn)
        # print(full_file_name)
        with open(full_file_name, 'w') as f:
            f.write(func_translate_it)


ptf = path_to_files('texts_in')  # вызов 1-й функции (список файлов с путями)
# f = open_file(ptf[0])    # вызов 2-й функции

# translate_it(open_file(ptf[0]))
