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


def get_recipes(dictionary, dish):
    """Функция получения рецепта для конкретного блюда"""
    a = dictionary.get(dish)  # список со словарями из ингредиентов
    return a

def get_dicts(list):
    """Функция получения словарей с рецептом"""
    d = {}
    newDict = {}
    lst = []
    persons = int(input("Введите число едоков: >>> "))
    for elem in list:
        name = elem.get("ingredient_name")
        kol = int(elem.get("quantity"))
        kol = int(elem.get("quantity"))
        for k, v in elem.items():
            if (k == 'measure') or (k == 'quantity'):
                d['quantity'] = kol * persons
                d[k] = v
        # print(d)
        print(elem)


def result(dicts):
    """Функция получения итогового словаря"""

    # print(dicts)


def main():
    """Главная функция - пользовательское меню"""
    pass


one = get_recipes(cook_book, 'Омлет')
two = get_dicts(one)
three = result(two)
