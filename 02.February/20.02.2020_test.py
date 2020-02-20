import pprint

lst = [[{'ingredient_name': 'Яйцо', 'measure': 'шт', 'quantity': 2},
        {'ingredient_name': 'Молоко', 'measure': 'мл', 'quantity': 100},
        {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': 2}],
       [{'ingredient_name': 'Говядина', 'measure': 'г', 'quantity': 500},
        {'ingredient_name': 'Перец сладкий', 'measure': 'шт', 'quantity': 1},
        {'ingredient_name': 'Лаваш', 'measure': 'шт', 'quantity': 2},
        {'ingredient_name': 'Винный уксус', 'measure': 'ст.л', 'quantity': 1},
        {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': 3}]]

person = 3
newDict = {}  # словарь ингредиентов
#
# for recept in lst:
#     for elem in recept:
#         name = elem['ingredient_name']
#         quantity = elem['quantity']
#         elem.pop('ingredient_name')
#         newDict[name] = elem
#         elem['quantity'] = quantity * person
#
# pprint.pprint(newDict)

for recept in lst:
    for elem in recept:
        pprint.pprint(elem)  # получаем отдельные словари для каждого ингредиента
        for key, val in elem.items():

pprint.pprint(newDict)

#
# a = (
#     {'Петя': 6, 'Вася': 8, 'Дима': 11, 'Юля': 3},
#     {'Петя': 5, 'Вася': 36, 'Дима': 4, 'Юля': 8},
#     {'Петя': 54, 'Вася': 21, 'Дима': 22, 'Юля': 39},
#     {'Петя': 61, 'Вася': 48, 'Дима': 71, 'Юля': 73}
# )
#
# resultdict = {}  # результирующий словарь
#
# for dictionary in a:  # пробегаем по списку словарей
#     for key in dictionary:  # пробегаем по ключам словаря
#         try:
#             resultdict[key] += dictionary[key]  # складываем значения
#         except KeyError:  # если ключа еще нет - создаем
#             resultdict[key] = dictionary[key]
#
# print(resultdict)
