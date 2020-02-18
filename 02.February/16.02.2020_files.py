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
    """Функция получения словарей с рецептом
    нужно сделать словарь ключи которого ингредиенты, а значение ключей словарь - единица измерения и кол-во.
    Я бы написал класс, но если так нельзя по условию или вы их не знаете можно обойтись функциями.
    1) создаём пустой словарь - итоговые данные
    2) итерируемся по полученному списку ингредиентов при этом поверяем есть ли ключ в итоговом словаре
        — если нет дописываем ключ и значение в итоговый словарь
        — если есть то из полученного значения ( метод get для проверки)  берём  и обновляем значение словаря с ключом
        quantity - полученного значение это тоже словарь
        dict[‘q’] = dict[‘q’] + value * кол-во гостей
    """
    newDict = {}  # словарь итоговый
    persons = int(input("Введите число едоков: >>> "))
    for elem in list:
        name = elem['ingredient_name']
        del elem['ingredient_name']
        newDict[name] = elem

    # newDict = {row['ingredient_name']: {k: v for k, v in row.items() if k != 'ingredient_name'} for row in list}
    # for elem in list:
    #     for k, v in elem.items():
    #         if k != 'ingredient_name':
    #             newDict = elem['ingredient_name'] = {k: v}

    # newDict = {item.pop('ingredient_name'): item for item in list}

    print(newDict)

    # # проверяем, есть ли ключ в словаре
    # if elem.get('ingredient_name') not in newDict:
    #     newDict[elem.get('ingredient_name')] = {}
    # else:
    #     newDict[elem.get('ingredient_name')] = {elem.get('measure') = }
    # print(newDict)


def result(dicts):
    """Функция получения итогового словаря"""

    # print(dicts)


def main():
    """Главная функция - пользовательское меню"""
    pass


one = get_recipes(cook_book, 'Омлет')
two = get_dicts(one)
three = result(two)
