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
            # dic_ing[cook_book[dish][]] =0

            for elem in cook_book[dish]:
                # print(elem)
                name = elem['ingredient_name']  # сохраняем название ингредиента (продукта)
                # print(name)
                if name in dic_ing:
                    dic_ing[name]['quantity'] = dic_ing[name]['quantity'] + elem['quantity']
                else:
                    dic_ing[name] = {'quantity': elem['quantity'], 'measure': elem['measure']}

    for v in dic_ing.values():
        # print(v)
        v['quantity'] *= persons
    pprint.pprint(dic_ing)
    print()


shop_list(['Омлет', 'Омлет', 'Омлет'], 2)  # яйцо - 12, молоко - 600, помидор - 12
shop_list(['Омлет', 'Омлет'], 2)  # яйцо - 8, молоко - 400, помидор - 8
shop_list(['Омлет', 'Омлет', 'Омлет', 'Омлет'], 2)  # яйцо - 16, молоко - 800, помидор - 16
shop_list(['Омлет', 'Омлет', 'Омлет'], 3)  # яйцо - 18, молоко - 900, помидор - 18
shop_list(['Омлет', 'Фахитос', 'Омлет'], 2)  # яйцо - 8, молоко - 400, помидор - 12
