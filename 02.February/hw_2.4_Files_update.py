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
    return cook_book


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
def shop_list(dictionary, lst_dish, persons):
    dic_ing = {}  # словарь с названием ингредиентов
    for dish in lst_dish:
        if dish in dictionary:
            for elem in dictionary[dish]:
                name = elem['ingredient_name']  # сохраняем название ингредиента (продукта)
                if name in dic_ing:
                    dic_ing[name]['quantity'] = dic_ing[name]['quantity'] + elem['quantity']
                else:
                    dic_ing[name] = {'quantity': elem['quantity'], 'measure': elem['measure']}
    for v in dic_ing.values():
        v['quantity'] *= persons
    print(f'\n'"Список продуктов для закупки с учетом {persons} персон:")
    return pprint.pprint(dic_ing)


def main():
    cb = cookbook('recipes.txt')  # функция получения из файла словаря с рецептами
    dl = dishes_list(cb)  # функция получения от пользователя списка блюд
    prsn = persons()  # функция получения от пользователя количества едоков
    shop_list(cb, dl, prsn)  # функция получения итогового словаря


main()
