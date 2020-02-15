import requests
import pprint

# points = {}
# for line in open('points.txt'):
#     line = line.split('\n')  # из строки получаем список
#     line = line[0]  # избавляемся от последнего элемента (\n)
#     line = line.split(' ')  # разделяем данные
#     line[1] = int(line[1])  # преобразуем координаты
#     line[2] = int(line[2])
#     points[line[0]] = line[1:]  # добавляем в словарь
#     # первый элемент списак - как ключ
#     # остальные - значение
# print(points)
#
# graphs = {}
# for line in open('graphs.txt'):
#     line = line.split('\n')
#     line = line[0]
#     line = line.split(' ')
#     graphs[line[0]] = line[1:]  # первый элемент - название пути
#     # остальные - точки, через которые он проходит
# print(graphs)

# with open('owner.txt') as fh:
#     d = {k.strip(): 0 for k in fh}
#
# print(d)
#
# data = []
# current = {}
# with open('Arts.txt') as f:
#     for line in f:
#         pair = line.split(': ', 1)
#         if len(pair) == 2:
#             if pair[0] == 'product/productId' and current:
#                 # start of a new block
#                 data.append(current)
#                 current = {}
#             current[pair[0]] = pair[1]
#     if current:
#         data.append(current)
#
# print(data)

# keys={}
# birds={}
# with open('birds.txt') as f:
#     for line in f:
#         k,_,v=line.partition(':')
#         k=k.capitalize()
#         v=map(float, v.split())
#         keys[k]=keys.setdefault(k, 0)+1
#         birds.setdefault('{} {}'.format(k, keys[k]), []).extend(v)
#
# print(birds)


# numbers = range(10)  # диапазон чисел от 0 до 9
# new_dict_for = {}  # создание нового словаря

# Add values to `new_dict` using for loop
# for n in numbers:  # для каждого числа из диапазона...
#     if n % 2 == 0:  # если число делится без остатка (четное число)...
#         new_dict_for[n] = n ** 2     # заносим в словарь это число в виде ключа, а его значением будет квадрат числа
#
# print(new_dict_for) # должно получиться: {2: 4, }


# new_dict_comp = {n: n ** 2 for n in numbers if n % 2 == 0}
# print(new_dict_comp)
#
# ne_d = {x: x ** 2 for x in numbers if x % 2 != 0}
# print(ne_d)

# d = {x: True for x in range(1, 11)}
# print(d)

# d = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
#
#
# def invert(d):
#     return {v: k for k, v in d.items()}
#
#
# print(invert(d))

# number = []
# for x in range(1, 11):
#     number.append(x)
# print(number)
#
# number = [x for x in range(1, 11)]
# print(number)
#
# numbers = [x for x in range(1,12) if x%2 != 0]
# print(numbers)

# data = [
#     {'id': 10, 'data': '...'},
#     {'id': 11, 'data': '...'},
#     {'id': 12, 'data': '...'},
#     {'id': 10, 'data': '...'},
#     {'id': 11, 'data': '...'},
#     {'id': 13, 'data': '...'},
#     {'id': 14, 'data': '...'},
#     {'id': 15, 'data': '...'},
#     {'id': 16, 'data': '...'},
#     {'id': 17, 'data': '...'},
#     {'id': 18, 'data': '...'},
#     {'id': 19, 'data': '...'},
# ]
#
# # Задача: составить новый список, содержащий ключи c уникальными значениями в словарях
# unique_data = []  # создаем новый список
# for d in data:  # для каждого элемента (словаря) в списке словарей ...
#     data_exists = False  # по умолчанию переменная = ложь
#     for ud in unique_data:  # для каждого элемента в новом списке...
#         if ud['id'] == d['id']:  # если значения по ключу id в обоих списках одинаковы ...
#             data_exists = True  # меняем переменную на правду...
#             break  # прекращаем проверку
#     if not data_exists:  # если переменная не равна лжи (равна правде)...
#         unique_data.append(d)  # добавляем в конец списка словарь с уникальным  значением по ключу id
# print(unique_data)
#
# ## Синтаксис ГЕНЕРАТОРА СЛОВАРЯ ###
# # { key:value for item in list if conditional }
#
# ud_list = {d['id']: d for d in data}.values()
# pprint(ud_list)

# url = 'https://randomuser.me/api/?results=1'
# users = requests.get(url).json()
#
# pprint.pprint(users)

# a = [
#     {"name": "Tom", "bag": ["black", "pink"]},
#     {"name": "Mark", "bag": ["red", "green"]},
#     {"name": "Pam", "bag": ["no"]}
# ]
#
# for elem in a:
#     for x in elem.values():
#         if x == ["no"]:
#             print(elem)
#             break
