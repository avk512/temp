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


def shop_list_one_dish(list, persons):
    """Функция получения словаря для одного выбранного блюда"""
    newDict = {}  # словарь с одним выбранным блюдом по количеству едоков
    for elem in list:
        name = elem['ingredient_name']  # сохраняем имя продукта (ингредиента)
        quant = elem['quantity']  # сохраняем начальное значение количества продукта
        del elem['ingredient_name']  # удаляем из словаря элемент ингредиента (ключ и значение)
        newDict[name] = elem  # заносим в новый словарь сохраненное имя продукта (ингредиента) в качестве ключа, а в
        # качестве значения словарь с количеством продукта и мерой веса (без наименования продукта, т.к. он удален)
        elem['quantity'] = quant * persons  # перезаписываем новое значение количества продукта

    return newDict


def shop_list_multy_dishes(d1, d2):
    """Функция получения итогового словаря в зависимости от количества блюд и едоков"""
    pass


def check_number():
    """Функция ввода количества едоков и проверки корректности ввода"""
    while True:
        select_persons = input("Укажите количество едоков: >>> ")
        if not select_persons.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        else:
            print(f"Число едоков: {select_persons}.")
            break
    return select_persons


def main():
    """Главная функция - пользовательское меню"""
    i = 1  # счетчик
    dishes = {}  # словарь доступных блюд
    numbers = []  # список из порядковых номеров доступных блюд
    print("Вам доступны на выбор следующие блюда:")
    for key in cook_book:
        dishes[i] = key
        i += 1
    for k, v in dishes.items():
        print(k, '=>', v)
        numbers.append(k)  # заносим в список порядковые номера доступных блюд
    print("")

    select_dish = input("Введите через пробел цифры нужных блюд: >> ")
    s_d_list = select_dish.replace(',', ' ').split()  # разбиваем введенные пользователем данные на элементы списка
    intgr = []  # список только для цифр
    for x in s_d_list:
        try:
            x = int(x)
            intgr.append(x)
        except ValueError:
            pass
    if len(intgr) > len(dishes) or len(intgr) < 1:
        print(F"Пожалуйста, выберите от 1 до {len(dishes)} блюд.")
        exit()

    for n in intgr:
        if n in dishes.keys():
            func1 = get_recipes(cook_book, dishes[n])
            print(f"Для выбранного блюда '{dishes[n]}:")
            print(shop_list_one_dish(func1, int(check_number())))


main()
