b = [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
     {'ingredient_name': 'Яйцо', 'quantity': 4, 'measure': 'шт'},
     {'ingredient_name': 'Молоко', 'quantity': 200, 'measure': 'мл'},
     {'ingredient_name': 'Помидор', 'quantity': 4, 'measure': 'шт'},
     ]

resultdict2 = {}  # результирующий словарь

for dictionary in b:  # пробегаем по списку словарей
    l = len(b)
    i = 0
    person = 2
    # print(l)
    while i < l:
        name = dictionary['ingredient_name']
        quantity = dictionary['quantity']
        dictionary['quantity'] = quantity * person  # перемножаем едоков на количество ингредиентов
        # dictionary.pop('ingredient_name')
        if name in resultdict2:
            # resultdict2[name][quantity] += dictionary['quantity']
            print(resultdict2[name][1])
        else:
            resultdict2[name] = b
        i += 1

print(resultdict2)
