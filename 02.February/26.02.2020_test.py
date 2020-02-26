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


# 1. Сначала получаем от пользователя выбранный им список блюд
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
    print("Вы выбрали следующие блюда:")
    print(f"- {', '.join(lst_dish)}")

    return lst_dish  # возварт блюд в виде списка: ['Омлет', 'Запеченный картофель']


# 2. Получаем список персон, для которых будем рассчитывать количество ингредиентов
def persons():
    """Функция получения количества едоков (персон)"""
    while True:
        persons = input("Укажите количество персон: >>> ")
        if not persons.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        else:
            pprint.pprint(f"Количество персон: {persons}")
            return int(persons)  # возврат количества персон в виде целого числа


# 3. Получаем итоговый результат в виде словаря со списком ингредиентов и их количества для покупки
def shop_list(lst_dish, persons):
    pass


def main():
    dl = dishes_list(cook_book)  # функция получения от пользователя списка блюд
    prsn = persons()  # функция получения от пользователя количества едоков
    sl = shop_list(dl, prsn)  # функция получения итогового словаря
