import pprint

#   Домашнее задание к лекции 2.4 "Открытие и чтение файла, запись в файл"
#   Задача №2 - создание словаря с названием ингредиентов и его объема по количеству едоков
#
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


def dishes_list(dictionary):
    """Функция, возвращающая список блюд по выбору пользователя"""
    lst_dish = []  # список названий блюд
    dic_dish = {}  # словарь блюд с порядковой нумерацией
    nw = []  # список цифр, отобранных из символов, введенных пользователем
    print("Вам доступны на выбор следующие блюда:")
    for n, d in enumerate(dictionary, 1):
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


def persons_count():
    """Функция получения количества едоков (персон)"""
    while True:
        persons = input("Укажите количество персон: >>> ")
        if not persons.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        else:
            return int(persons)  # возврат в виде целого числа количества персон


def get_recipes(dictionary, list_of_dishes):
    """Функция получения списка списков словарей для одного или нескольких рецептов блюд"""
    data = []  # список для списка словарей рецептов блюд
    for elem in list_of_dishes:
        for key, val in dictionary.items():
            if elem == key:
                data.append(dictionary.get(key))  # получаем список списка словарей для нескольких блюд
    return data


func1 = dishes_list(cook_book)  # запуск функции получения списка блюд от пользователя
# pprint.pprint(func1)
func2 = persons_count()  # запуск функции получения количество едоков (персон)
func3 = get_recipes(cook_book, func1)  # запуск функции получения списка списков словарей для рецептов блюд
# pprint.pprint(func3)
