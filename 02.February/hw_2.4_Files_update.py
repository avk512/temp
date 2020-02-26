import pprint

#   Домашнее задание к лекции 2.4 "Открытие и чтение файла, запись в файл"
#   Задача №1 - создание словаря кулинарной книги
#
def cookbook(filename):
    cook_book = {}  # итоговый словарь
    with open(filename, encoding='UTF-8') as f:
        while True:
            i = 0  # счетчик
            stroka = f.readline().strip()  # читаем файл построчно
            ing = []  # промежуточный список для ингредиентов
            if not stroka:
                # print("Рецепты закончились.")
                break
            dish_name = stroka  # сохраняем наименование блюда
            cnt = int(f.readline().strip())  # сохраняем количество ингредиентов
            while i < cnt:
                ingred = f.readline().strip().replace(" | ", ",").split(",")  # читаем строки с ингредиентами
                ing.append({'ingredient_name': ingred[0], 'quantity': int(ingred[1]), 'measure': ingred[2]})
                i += 1
                cook_book[dish_name] = ing  # заносим в словарь
            f.readline().strip()  # пустая строка
    # return pprint.pprint(cook_book)
    return cook_book


#   Задача №2 - создание словаря с названием ингредиентов и его объема по количеству едоков
# 1. Сначала получаем от пользователя выбранный им список блюд
def dishes_list(dictionary):
    """Функция, возвращающая список блюд по выбору пользователя"""
    lst_dish = []  # список названий блюд
    set_dish = set()  # множество названий блюд
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
            # set_dish.add(dic_dish[x])  # заносим в множество названия блюд (исключая повторы)
            # lst_dish = list(set_dish)  # преобразуем множество в список
    print("Вы выбрали следующие блюда:")
    print(f"- {', '.join(lst_dish)}")
    # print(lst_dish)
    # print(set_dish)

    return lst_dish  # возварт блюд в виде списка: ['Омлет', 'Запеченный картофель']


# 2. Получаем список персон, для которых будем рассчитывать количество ингредиентов
def persons_count():
    """Функция получения количества едоков (персон)"""
    while True:
        persons = input("Укажите количество персон: >>> ")
        if not persons.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        else:
            return int(persons)  # возврат количества персон в виде целого числа


# 3. Получаем список рецептов для одного или нескольких блюд, которые выбрал пользователь
def get_recipes(dictionary, list_of_dishes):
    """Функция получения списка списков словарей для одного или нескольких рецептов блюд"""
    recipes = []  # список для списка словарей рецептов блюд
    for elem in list_of_dishes:
        for key, val in dictionary.items():
            if elem == key:
                recipes.append(dictionary.get(key))  # получаем список списков словарей рецептов

    return recipes


# 4. Получаем итоговый результат в виде словаря со списком ингредиентов и их количества для покупки
def shop_list(list_of_recipes, persons_count):
    resDict = {}  # итоговый словарь
    for recepts in list_of_recipes:
        for elem in recepts:
            name = elem['ingredient_name']  # сохраняем название ингредиента (продукта)
            quantity = elem['quantity']  # сохраняем количество ингредиента (продукта)
            # elem.pop('ingredient_name')  # удаляем из словаря пару с названием ингредиента
            elem['quantity'] = quantity * persons_count  # перемножаем едоков на количество ингредиентов
            if name in resDict:
                resDict[name]['quantity'] += elem['quantity']
            else:
                resDict[name] = elem
    print(f"Список продуктов для закупки с учетом {persons_count} персон:")
    return pprint.pprint(resDict)


def main():
    func0 = cookbook("recipes.txt")  # запуск функции для получения словаря с рецептами
    func1 = dishes_list(func0)  # запуск функции получения списка блюд от пользователя
    func2 = persons_count()  # запуск функции получения количество едоков (персон)
    func3 = get_recipes(func0, func1)  # запуск функции получения списка списков словарей для рецептов блюд
    shop_list(func3, func2)  # запуск функции получения итогового словаря


main()
