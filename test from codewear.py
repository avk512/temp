# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
# Создайте функцию, которая вернет новые списки без строк
# Example#
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
#
from typing import List, Union
#
# a = [1, 2, 'a', 'b']
# b = [1, 'a', 'b', 0, 15]
# c = [1, 2, 'aasf', '1', '123', 123]
#
#
# def list_only_digit(lst):
#     """function that takes a list of non-negative integers and strings and returns a new list with the strings
#     filtered out
#     Функция, которая возращает новый список, состоящий только из цифр
#     """
#     dig_list = []
#     for elem in lst:
#         if type(elem) == int:
#             dig_list.append(elem)
#     return print(dig_list)
#
#
# list_only_digit(c)
