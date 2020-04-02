import os
import json
import requests


def files_name(dir_input):
    """Получение списка файлов в исходной папке"""
    fname = os.listdir(dir_input)  # список имен файлов в папке
    print(fname)  # ['DE.txt', 'ES.txt', 'FR.txt']
    return fname


def file_name_without_ext(func_files_name):
    """Получение списка имен файлов без расширений"""
    fnwe = []  # список для имен файлов без расширений
    for file in func_files_name:
        fn = os.path.splitext(file)  # кортеж из имени файла и его расширения
        fnwe.append(fn[0])
    print(fnwe)  # ['DE', 'ES', 'FR']
    return fnwe


def file_open(dir_input, func_files_name):
    """Получение абсолютного пути и открытие файла на чтение"""
    full_file_name = os.path.join(os.path.abspath(dir_input), func_files_name)
    # print(full_file_name)
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


def write_tr_text(dir_output, func_fnwe, func_translate):
    fnwe = func_fnwe
    for ff in func_fnwe:
        fn = f'{ff}-Ru.txt'
        new_file = os.path.join(dir_output, fn)
        with open(new_file, 'w', encoding='UTF-8') as f:
            f.write(func_translate)
            # print("Записано")


fname = files_name('texts_in')  # ['DE.txt', 'ES.txt', 'FR.txt']
fnwe = file_name_without_ext(fname)  # ['DE', 'ES', 'FR']


def main():
    """Основная функция программы"""

    for file in fname:
        fopen = file_open('texts_in', file)
        # print(fopen)
        tr = translate(fopen)
        print("Переведен текст")
        # print(tr)

        # сбойный фрагмент кода !!!!
        for ff in fnwe:
            fn = f'{ff}-Ru.txt'
            # print(fn)
            new_file = os.path.join('texts_out', fn)
            with open(new_file, 'w', encoding='UTF-8') as f:
                f.write(tr)
                print("Записано в файл")

    print("Выполнено")


# fopen = file_open('texts_in', fname[0])
# tr = translate(fopen)
# write_tr_text('texts_out', fnwe, tr)

if __name__ == '__main__':
    main()
