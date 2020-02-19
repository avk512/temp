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


def get_recipes(dictionary, dish):
    """Функция получения рецепта для конкретного блюда"""
    a = dictionary.get(dish, "Такого блюда нет!")  # список со словарями из ингредиентов
    return a


def dishes_list(dict):
    """Функция, возвращающая список блюд по выбору пользователя"""
    lst_dish = []  # список названий блюд
    dic_dish = {}  # словарь блюд с порядковой нумерацией
    print("Вам доступны на выбор следующие блюда:")
    for n, d in enumerate(dict, 1):
        print(n, '=>', d)
        dic_dish[n] = d
    inp = input('Введите через пробел номера блюд, список продуктов для которых вы хотите рассчитать: >>> ').split()
    result = [int(item) for item in inp]  # преобразуем строки в списке в числа
    for x in result:
        if x in dic_dish.keys():
            lst_dish.append(dic_dish[x])  # заносим в список названия блюд, выбранных пользователем
    print("Вы выбрали следующие блюда:")
    print(f"- {', '.join(lst_dish)}")
    return lst_dish


def persons_count():
    """Функция получения количества персон"""
    pass


def shop_list(dishes_list, persons):
    """Функция, получает на вход список блюд и количество едоков, а на выходе формируется словарь
        с названием ингредиентов и его количества для блюд"""
    pass


func1 = dishes_list(cook_book)  # запуск функции получения списка блюд от пользователя
