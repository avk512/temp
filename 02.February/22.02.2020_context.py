# class Person:   # отражает сущностьь человека
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#         self.asks = 0
#
#     def say_name(self):
#         print('My name is ' + self.name)
#         self.asks += 1

# import datetime
#
#
# class Myopen:
#     def __init__(self, path, method):
#         self.path = path
#         self.method = method
#
#     def __enter__(self):
#         self.file = open(self.path, self.method, encoding='UTF-8')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.method == 'w':
#             now = datetime.datetime.now()
#             self.file.write(f'\n{now}\n')
#             if exc_type:
#                 self.file.write(f"{exc_val}\n")
#                 self.file.write(f"{exc_tb.tb_frame}\n")
#         self.file.close()
#         # print(exc_type)
#         # print(exc_val)
#         # print(exc_tb.tb_frame)
#
# if __name__ == '__main__':
#     with Myopen('testfile.txt', 'w') as test_file:
#         test_file.write('Первая строка')
#     # print(test_file.closed)
#         1/0


import datetime
# import contextlib
from contextlib import contextmanager
import sys


# @contextlib.contextmanager
@contextmanager
def my_open(path, method):
    try:
        file = open(path, method, encoding='UTF-8')
        yield file
    finally:
        if method == 'w':
            now = datetime.datetime.now()
            file.write(f'\n{now}\n')
        exc_ex, exc_info, exc_tb = sys.exc_info()
        file.write(f'\n{exc_tb.tb_frame}\n')
        file.close()

if __name__ == '__main__':
    with my_open('testfile.txt', 'w') as file:
        file.write('И это первая строка')
        file.read()