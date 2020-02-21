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
for recept in lst:
    for elem in recept:
        name = elem['ingredient_name']
        quantity = elem['quantity']
        elem.pop('ingredient_name')
        elem['quantity'] = quantity * person
        if name in newDict:
            newDict[name]['quantity'] += elem['quantity']
        else:
            newDict[name] = elem

pprint.pprint(newDict)
