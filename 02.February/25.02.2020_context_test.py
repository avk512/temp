import pprint
import datetime
import time
from contextlib import contextmanager


class open_file:
    """"""

    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


#   Домашнее задание к лекции 2.4 "Открытие и чтение файла, запись в файл"
#   Задача №1 - создание словаря кулинарной книги
#
def cookbook(filename):
    cook_book = {}  # итоговый словарь
    with open(filename, encoding='UTF-8') as f:
        while True:
            i = 0  # счетчик
            stroka = f.readline().strip()  # читаем файл построчно
            ing = []  # промежуточный список для ингредиентов
            if not stroka:
                # print("Рецепты закончились.")
                break
            dish_name = stroka  # сохраняем наименование блюда
            cnt = int(f.readline().strip())  # сохраняем количество ингредиентов
            while i < cnt:
                ingred = f.readline().strip().replace(" | ", ",").split(",")  # читаем строки с ингредиентами
                ing.append({'ingredient_name': ingred[0], 'quantity': int(ingred[1]), 'measure': ingred[2]})
                i += 1
                cook_book[dish_name] = ing  # заносим в словарь
            f.readline().strip()  # пустая строка
    return pprint.pprint(cook_book)


cookbook("recipes.txt")
