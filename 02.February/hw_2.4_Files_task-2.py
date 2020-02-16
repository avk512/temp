#   Домашнее задание к лекции 2.4 "Открытие и чтение файла, запись в файл"
#   Задача №2 - создание словаря с названием ингредиентов и его объема по количеству едоков
#
cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'},
                       {'ingredient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'},
                       {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}],
             'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': '1', 'measure': 'шт'},
                                  {'ingredient_name': 'Вода', 'quantity': '2', 'measure': 'л'},
                                  {'ingredient_name': 'Мед', 'quantity': '3', 'measure': 'ст.л'},
                                  {'ingredient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}],
             'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'},
                                      {'ingredient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч'},
                                      {'ingredient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}],
             'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': '500', 'measure': 'г'},
                         {'ingredient_name': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'},
                         {'ingredient_name': 'Лаваш', 'quantity': '2', 'measure': 'шт'},
                         {'ingredient_name': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'},
                         {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}]}


def get_shop_list():
    pass


def get_recipes(dictionary, dish):
    newDict = {}
    d = {}
    if dish not in dictionary.keys():
        return print("Такого блюда нет.")
    else:
        # print(dictionary.get(dish))
        # return dictionary.get(dish)
        a = dictionary.get(dish)
        # print(a)
        for x in a:
            name = x.get("ingredient_name")
            # print(name)
            kol = int(x.get("quantity"))
            # print(kol, type(kol))
            for a, b in x.items():
                if (a == 'measure') or (a == 'quantity'):
                    d['quantity'] = kol * 2
                    d[a] = b
            # print(d['quantity'])
            print(d)
            newDict[name] = d
    print(newDict)


get_recipes(cook_book, 'Омлет')


def main():
    i = 0
    print("Вам доступны для заказа следующие блюда:")
    for k in cook_book.keys():
        i += 1
        print(f"{i}.{k}")
    print("")
    inp = input("Выберите нужное блюдо (блюда) через запятую, и введите число гостей: >> ")

# main()
