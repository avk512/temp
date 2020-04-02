import os
import json
import requests


def files_name(dir_input):
    """Получение списка файлов в исходной папке"""
    fname = os.listdir(dir_input)  # список имен файлов в папке
    print(fname)
    return fname


def file_name_without_ext(fname):
    """Получение имени файла без расширения"""
    fnwe = os.path.splitext(fname)  # кортеж из имени файла и его расширения
    print(fnwe[0])
    return fnwe[0]


def file_open(dir_input, func_files_name):
    """Получение абсолютного пути и открытие файла на чтение"""
    full_file_name = os.path.join(os.path.abspath(dir_input), func_files_name)
    print(full_file_name)
    with open(full_file_name, encoding='UTF-8') as f:
        fopened = f.read()
    # print(fopened)
    return fopened


def translate(func_file_open):
    """Перевод файла из исходной папки"""
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20200331T164239Z.ec4eb58b5568079e.e7d2adf2434d9f6a15c2005521187654e1f2e954'
    params = {
        'key': key,
        'text': func_file_open,
        'lang': 'ru'
    }
    response = requests.get(URL, params=params)
    resp_json = response.json()
    # print(''.join(resp_json['text']))
    return ''.join(resp_json['text'])


def write_tr_text(dir_output, func_file_name_without_ext, func_translate):
    fnwe = func_file_name_without_ext
    fn = f'{fnwe}-Ru.txt'
    new_file = os.path.join(dir_output, fn)
    with open(new_file, 'w', encoding='UTF-8') as f:
        f.write(func_translate)
    print("Выполнено")


fname = files_name('texts_in')
fnwe = file_name_without_ext(fname[0])
fopen = file_open('texts_in', fname[0])
tr = translate(fopen)
write_tr_text('texts_out', fnwe, tr)
