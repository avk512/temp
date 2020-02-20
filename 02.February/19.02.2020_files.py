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


def dishes_list(dict):
    """Функция, возвращающая список блюд по выбору пользователя"""
    lst_dish = []  # список названий блюд
    dic_dish = {}  # словарь блюд с порядковой нумерацией
    nw = []  # список цифр, отобранных из символов, введенных пользователем
    print("Вам доступны на выбор следующие блюда:")
    for n, d in enumerate(dict, 1):
        print(n, '=>', d)
        dic_dish[n] = d
    inp = input('Введите через пробел номера блюд, список продуктов для которых вы хотите рассчитать: >>> ').split()
    for n in inp:
        if n.isnumeric():
            nw.append(n)
    result = [int(item) for item in nw]  # преобразуем строки в списке в числа
    for x in result:
        if x in dic_dish.keys():
            lst_dish.append(dic_dish[x])  # заносим в список названия блюд, выбранных пользователем
    # print("Вы выбрали следующие блюда:")
    # print(f"- {', '.join(lst_dish)}")
    # print(lst_dish)
    return lst_dish  # возварт блюд в виде списка: ['Омлет', 'Запеченный картофель']


def get_recipes(dict, dishes_list):
    """Функция получения рецепта для конкретного блюда"""
    # dic_ingred = {}  # словарь с ингредиентами для каждого блюда
    dlst = []
    for elem in dishes_list:
        dlst.append(dict.get(elem))  # вернет список списков со словарями из ингредиентов вида:
        # [[{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        # {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        # {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]]
        return dlst


def persons_count():
    """Функция получения количества персон"""
    while True:
        persons = input("Укажите количество едоков: >>> ")
        if not persons.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        else:
            return int(persons)


def shop_list(dishes_list, persons):
    """Функция получает на вход список блюд и количество едоков, а на выходе формируется словарь
        с названием ингредиентов и его количества для блюд"""
    newDict = {}  # словарь с одним выбранным блюдом по количеству едоков
    for elem in dishes_list:
        name = elem['ingredient_name']  # сохраняем имя продукта (ингредиента)
        quant = elem['quantity']  # сохраняем начальное значение количества продукта
        del elem['ingredient_name']  # удаляем из словаря элемент ингредиента (ключ и значение)
        newDict[name] = elem  # заносим в новый словарь сохраненное имя продукта (ингредиента) в качестве ключа, а в
        # качестве значения словарь с количеством продукта и мерой веса (без наименования продукта, т.к. он удален)
        elem['quantity'] = quant * persons  # перезаписываем новое значение количества продукта

    return newDict


func1 = dishes_list(cook_book)  # запуск функции получения списка блюд от пользователя
func2 = get_recipes(cook_book, func1)  # запуск функции получения рецептов для конкретных блюд в виде списка словарей
func3 = persons_count()  # запуск функции получения количества персон для расчета
func4 = shop_list(func1, func3)
# print(func3)
