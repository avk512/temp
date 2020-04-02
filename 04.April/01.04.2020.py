import os
import json
import requests


def files_name(dir_input):
    """Получение списка файлов в исходной папке"""
    fname = os.listdir(dir_input)  # список имен файлов в папке
    print(
        f"Готовятся к переводу файлы: {fname}\n")  # ['DE.txt', 'ES.txt', 'FR.txt']
    return fname


def file_name_without_ext(file_name):
    """Получение списка имен файлов без расширений"""
    fn = os.path.splitext(file_name)  # кортеж из имени файла и его расширения
    return fn[0]


def file_open(dir_input, func_files_name):
    """Получение абсолютного пути и открытие файла на чтение"""
    full_file_name = os.path.join(os.path.abspath(dir_input), func_files_name)
    with open(full_file_name, encoding='UTF-8') as f:
        fopened = f.read()
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
    return ''.join(resp_json['text'])


def main():
    """Основная функция программы"""
    fname = files_name('texts_in')  # ['DE.txt', 'ES.txt', 'FR.txt']
    for file in fname:
        # print(file)
        fns = file_name_without_ext(file)
        # print(fns)
        fn = f'{fns}-Ru.txt'
        # print(fn)
        new_file = os.path.join('texts_out', fn)
        # print(new_file)
        with open(new_file, 'w', encoding='UTF-8') as f:
            fopen = file_open('texts_in', file)
            # print(fopen)
            tr = translate(fopen)
            # print(tr)
            print(f"Переведен текст из файла {file}")
            f.write(tr)
            print(f"Записано в файл {fn}")

    print("\nЗадача №1 выполнена!")


if __name__ == '__main__':
    main()