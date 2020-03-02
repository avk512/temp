import pprint
import datetime
import time
from contextlib import contextmanager


class OpenTimer:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, encoding='UTF-8')
        self.dt_now = datetime.datetime.now()  # дата и время начала выполнения кода блока
        self.t_now = time.time()  # время начала выполнения кода блока
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        now = datetime.datetime.now()  # текущие дата и время
        dt = self.dt_now - now  # расчетное время выполнения блока кода с датой
        timing = self.t_now - time.time()  # расчетное время выполнения блока кода без даты (только время)
        # print("Время выполнения: {:.3f} sec".format(time.time() - self._startTime))


if __name__ == '__main__':
    cook_book = {}  # итоговый словарь
    with OpenTimer('recipes.txt') as file:
        pass


@contextmanager
def open_timer(filename):
    try:
        dt_start = datetime.datetime.now()  # дата и время начала выполнения кода блока
        # t_start = time.time()  # время начала выполнения кода блока
        t_start = time.monotonic()
        file = open(filename, encoding='UTF-8')
        yield file
    finally:
        now_time = time.monotonic()
        timing = now_time - t_start  # расчетное время выполнения блока кода без даты (только время)
        print(f"Дата и время начала выполнения кода: {dt_start}.")
        print(f'Время выполнения кода (полный формат): {timing} секунд.')
        # print(f"Время выполнения: {format(timing, ':>.3f')} секунд\n")
        print(f"Время выполнения кода (округленный формат): {timing:>.3f} секунд.\n")


if __name__ == '__main__':
    cook_book = {}
    with open_timer('recipes.txt') as file:
        while True:
            time.sleep(0.1)  # задержка выполнения кода, иначе мгновенно выполняется
            i = 0  # счетчик
            stroka = file.readline().strip()  # читаем файл построчно
            ing = []  # промежуточный список для ингредиентов
            if not stroka:
                # print("Рецепты закончились.")
                break
            dish_name = stroka  # сохраняем наименование блюда
            cnt = int(file.readline().strip())  # сохраняем количество ингредиентов
            while i < cnt:
                ingred = file.readline().strip().replace(" | ", ",").split(",")  # читаем строки с ингредиентами
                ing.append({'ingredient_name': ingred[0], 'quantity': int(ingred[1]), 'measure': ingred[2]})
                i += 1
                cook_book[dish_name] = ing  # заносим в словарь
            file.readline().strip()  # пустая строка
    pprint.pprint(cook_book)
