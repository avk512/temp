import pprint

recipes = [[{'ingredient_name': 'Яйцо', 'measure': 'шт', 'quantity': 2},
            {'ingredient_name': 'Молоко', 'measure': 'мл', 'quantity': 100},
            {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': 2}],
           [{'ingredient_name': 'Яйцо', 'measure': 'шт', 'quantity': 2},
            {'ingredient_name': 'Молоко', 'measure': 'мл', 'quantity': 100},
            {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': 2}]]


# 4. Получаем итоговый результат в виде словаря со списком ингредиентов и их количества для покупки
def shop_list(list_of_recipes, persons_count):
    resDict = {}  # итоговый словарь
    for recepts in list_of_recipes:
        for elem in recepts:
            name = elem['ingredient_name']  # сохраняем название ингредиента (продукта)
            quantity = elem['quantity']  # сохраняем количество ингредиента (продукта)
            # elem.pop('ingredient_name')  # удаляем из словаря пару с названием ингредиента
            elem['quantity'] = quantity * persons_count  # перемножаем едоков на количество ингредиентов
            if name in resDict:
                resDict[name]['quantity'] += elem['quantity']
            else:
                resDict[name] = elem
    print(f"Список продуктов для закупки с учетом {persons_count} персон:")
    return pprint.pprint(resDict)


shop_list(recipes, 2)
