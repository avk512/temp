import time  # импорт библиотеки с функциями времени
from contextlib import contextmanager

#
#
# class timer():
#
#     def __init__(self):
#         self.start = time.time()  # переменная, в которую будет занесено время старта -
#         # текущее время (время начала отсчета)
#
#     def current_time(self):
#         return time.time() - self.start  # рассчитываем время выполнения, прошедшее от начала
#         # выполнения чего-либо в контекстном менеджере (текущее время минус время старта)
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, *args):
#         print(f"Время выполнения: {self.current_time()}")  # выведем время выполнения
#
#
# # Контекстный менеджер, который считает время, проведенное внутри него и выводит время, которое прошло с момента начала
# # внутри самого контекстного менеджера
# with timer() as t:
#     time.sleep(1)  # выводим время выполнения с задержкой в 1 секунду
#     print(f"Текущее время: {t.current_time()}")
#     time.sleep(1)

# Пример кода из книги Лутца (стр.950)
# class TraceBlock:
#     """Определяет объект менеджера контекста, который сообщает о входе и выходе из блока программного блока
#     любой инструкции with, с которой он используется"""
#     def __init__(self):
#         self.start = time.time()    # время старта (время входа в менеджер контекста)
#
#     def current_time(self):
#         return time.time() - self.start # расчет времени выполнения кода
#
#     def message(self, arg):
#         print('Выполняется', arg)
#
#     def __enter__(self):  # выполняется при входе в блок кода инструкции with. Возвращает объект, который будет
#     # использоваться в пределах данного контекста
#         print('Начало with блока')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):    # выполняется при выходе из блока with (всегда в любом случае)
#         if exc_type is None:
#             print('Выход без порождения исключения')#
#         else:
#             print('Возникло исключение!', exc_type)
#             return False    # повторное возбуждение исключения
##        print(f'Время выполнения: {self.current_time()}\n')  #вывод времени выполнения кода
#
# with TraceBlock() as action:
#     action.message('test 1')
#     print('Выполнено')
#
# with TraceBlock() as action:
#     action.message('test 2')
#     raise TypeError
#     print('Не выполнено')

# Пример кода расчета времени выполнения блока кода (из книги Python книга рецептов стр.381)
# @contextmanager
# def timethis(label):
#     start = time.time()
#     try:
#         yield
#     finally:
#         end = time.time()
#         print(f'{label}: {start - end}')
#
#
# with timethis('counting'):
#     n = 10000000
#     while n > 0:
#         n -= 1

# @contextmanager
# def list_transaction(orig_list):
#     working = list(orig_list)
#     yield working
#     orig_list[:] = working
#
#
# items = [1, 2, 3]
# with list_transaction(items) as working:
#     working.append(4)
#     working.append(5)
#
# print(items)
#
# with list_transaction(items)as working:
#     working.append(6)
#     working.append(7)
#     raise RuntimeError('oops')
#
# print(items)

# f = (x for x in range(100))
# c = [x for x in range(100)]
#
# print(f)
# print()
# print(c)
# print()
# print(f)
# print()
# print(c)
