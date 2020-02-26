import pprint

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


# 3. Получаем итоговый результат в виде словаря со списком ингредиентов и их количества для покупки
def shop_list(lst_dish, persons):
    dic_ing = {}  # словарь с названием ингредиентов
    i = 0
    for dish in lst_dish:
        if dish in cook_book:
            # print(cook_book[dish])
            dic_ing[cook_book[dish]['ingredient_name']] =

            #  for elem in cook_book[dish]:
            #      # print(elem)
            #      name = elem['ingredient_name']  # сохраняем название ингредиента (продукта)
            #      # print(name)
            #      if name in dic_ing:
            #          dic_ing[name]['quantity'] = dic_ing[name]['quantity'] + elem['quantity']
            #      else:
            #          dic_ing[name] = {'quantity': elem['quantity'], 'measure': elem['measure']}
            #      print(dic_ing[name]['quantity'])

    # pprint.pprint(dic_ing)


shop_list(['Омлет', 'Омлет', 'Омлет'], 2)
