cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
                       {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
                       {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}],
             'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
                                  {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
                                  {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
                                  {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}],
             'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
                                      {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
                                      {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}],
             'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
                         {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
                         {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
                         {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
                         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]}

# dishes = {}
# i = 1
# for key in cook_book:
#     # print(key)
#     dishes[i] = key
#     i += 1
#
# print(dishes)
# lst = [1, 4, 5, 2]
# print(lst)
#
# for x in lst:
#     if x in dishes.keys():
#         print(f"{x} есть в словаре")
#     else:
#         print(f"{x} отсутствует в словаре")

# lst = [{'update_id': 138638308,
#         'message': {'message_id': 215, 'from': {'id': 2999, 'is_bot': False, 'first_name': 'Yuri'},
#                     'chat': {'id': 77777777, 'first_name': 'Yuri'}}}]
#
# print(lst[0])
# print(lst[0]['message'])
# print(lst[0]['message']['chat'])
# print(lst[0]['message']['chat']['id'])


# a = [1, 2, 3, 4, 5, 6]
#
# s = ' '.join('@{}(.)'.format(i) for i in a)
#
# print(s)

# s = []
# for i in a:
#     s.append("".join(f'@{i}(.)'))
# print(s)
#
# a = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
# for i, item in enumerate(a):
#     a[i] = int(item)
# print(a)

inp = input('Введите через пробел номера блюд, список продуктов для которых вы хотите рассчитать: >>> ')
if inp.isspace():
    print("Есть цифры и пробелы")
else:
    print("Есть плохие символы")
