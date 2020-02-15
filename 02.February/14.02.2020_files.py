import requests
import pprint

# i_list = []  #
# ingr_dic = {}  #
# cook_book = {}  #
# with open('recipes2.txt', encoding='UTF-8') as f:
#     while True:
#         cnt = True
#         dn = f.readline().strip()  #
#         if not dn:
#             print("Рецепты закончились.")
#             cnt = False
#             break
#
#         colin = f.readline().strip()  #
#
#         for x in range(int(colin)):
#             ingr = f.readline().strip().replace(' | ', ',')  #
#             ingr_lst = ingr.split(',')  #
#             for elem in ingr_lst:
#                 ingr_dic['ingredient_name'] = ingr_lst[0]  #
#                 ingr_dic['quantity'] = int(ingr_lst[1])  #
#                 ingr_dic['measure'] = ingr_lst[2]  #
#             # print(ingr_dic)
#             y = ingr_dic
#             # print(cook_book)
#         f.readline().strip()  # пустая строка
#         cook_book[dn] = y
#         print(cook_book)


# with open('recipes.txt', encoding='utf-8-sig') as f:
#     cook_book = {}
#     while True:
#         cook = f.readline().strip()
#         cook_book[cook] = []
#         count = f.readline().strip()
#         i = 0
#         while i < int(count):
#             a = f.readline().strip().split()
#             cook_book[cook].append({'ingredient_name': a[0], 'quantity': a[2],'measure': a[4]})
#             i += 1
#         if f.readline() == '\n':
#             continue
#         else:
#             break
#
# print(cook_book)

cook_book = {}  # итоговый словарь
with open('recipes2.txt', encoding='UTF-8') as f:
    while True:
        i = 0  # счетчик
        stroka = f.readline().strip()  # читаем файл построчно
        ing = []  # список для ингредиентов
        if not stroka:
            print("Рецепты закончились.")
            break
        dish_name = stroka  # сохраняем наименование блюда
        cnt = int(f.readline().strip())  # сохраняем количество ингредиентов
        while i < cnt:
            ingred = f.readline().strip().replace(" | ", ",").split(",")  # читаем строки с ингредиентами
            ing.append({'ingredient_name': ingred[0], 'quantity': ingred[1], 'measure': ingred[2]})
            i += 1
            cook_book[dish_name] = ing  # заносим в словарь
        f.readline().strip()  # пустая строка

print(cook_book)
# pprint.pprint(cook_book)
