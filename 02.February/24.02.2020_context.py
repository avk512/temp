import pprint
import datetime
import time
import contextlib


class date_timer:
    """Вариант решения задачи с использованием класса"""

    def __init__(self, path, encoding):
        self.path = path
        self.encoding = encoding
        self.d_now = datetime.datetime.now()  # дата и время начала выполнения программы
        self.t_start = time.time()  # начало выполнения программы

    def __enter__(self):
        self.file = open(self.path, encoding='UTF-8')
        return self.file

    def current_date_time(self):
        return time.time() - self.t_start  # рассчитываем время выполнения, прошедшее от начала

    #         # выполнения блока кода в контекстном менеджере (текущее время минус время старта)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.d_end = datetime.datetime.now()  # дата и время окончания программы
        print(f'Время выполнения: {self.current_date_time()}\n')  # вывод времени выполнения кода


#
def cookbook(filename):
    cook_book = {}  # итоговый словарь
    with date_timer(filename, encoding='UTF-8') as f:
        f.
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
        print(date_timer.d_end)
    return pprint.pprint(cook_book)


cookbook("recipes.txt")
