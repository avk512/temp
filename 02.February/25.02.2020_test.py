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


def get_recipes(dictionary, list_of_dishes):
    """Функция получения списка списков словарей для одного или нескольких рецептов блюд"""
    recipes = []  # список для списка словарей рецептов блюд
    for elem in list_of_dishes:
        for key, val in dictionary.items():
            if elem == key:
                recipes.append(dictionary.get(key))  # получаем список списков словарей рецептов
    # pprint.pprint(recipes)
    # print()
    return recipes


# 4. Получаем итоговый результат в виде словаря со списком ингредиентов и их количества для покупки
def shop_list(list_of_recipes, persons_count):
    resDict = {}  # итоговый словарь
    for recepts in list_of_recipes:
        for elem in recepts:
            name = elem['ingredient_name']  # сохраняем название ингредиента (продукта)
            quantity = elem['quantity']  # сохраняем количество ингредиента (продукта)
            # elem.pop('ingredient_name')  # удаляем из словаря пару с названием ингредиента
            # elem['quantity'] = quantity * persons_count  # перемножаем едоков на количество ингредиентов
            if name in resDict:
                resDict[name]['quantity'] += elem['quantity']
                resDict[name]['quantity'] *= persons_count
            else:
                resDict[name] = elem
                elem['quantity'] = quantity * persons_count  # перемножаем едоков на количество ингредиентов
    print(f"Список продуктов для закупки с учетом {persons_count} персон:")
    return pprint.pprint(resDict)


recipes = get_recipes(cook_book, ['Омлет', 'Омлет', 'Омлет', 'Фахитос'])
shop_list(recipes, 2)
