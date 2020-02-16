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
    # print(a)
    return a


def quantity(persons):
    """Функция расчета количества продуктов по количеству едоков"""
    z = []
    a = get_recipes(dictionary, dish)
    for x in a:
        # print(x)
        k = int(x.get('quantity')) * persons
        z.append(k)
    return z  # список из цифр


def newDict(func1, func2):
    d = {}

    for x, y in func1:
        if (x == 'measure') or (x == 'quantity'):
            d[x] = y
    # print(d)


def result(func1, func2):
    """Функция получения итогового словаря"""
    pass


def main():
    """Главная функция - пользовательское меню"""
    pass


# get_recipes(cook_book, 'Омлет')
quantity(get_recipes(cook_book, 'Омлет'), 3)
# newDict(get_recipes(cook_book, 'Омлет'), quantity(get_recipes(cook_book, 'Омлет'), 3))
