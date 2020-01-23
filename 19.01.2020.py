# Задача 1
# l = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50]


# Из списка а необходимо создать словарь, где ключ это строка, а его значением являются цифры, слеюдущие за строкой в списке, например: {'first': 1, 2, 3}
# def key_value():
#     d = {}
#     s = None
#     for element in l:
#         if type(element) == str:
#             d[element] = []
#             s = element
#         else:
#             d[s].append(element)
#     return d


# print(key_value())

# Задача 2
# Необходимо подсчитать количество слов (без пробелов, без знаков препинания) в предложенном тексте
# my_text = "Я недаром вздрогнул, не загробный вздор, в порт, горящий как расплавленное лето, разворачивался и входил товарищ Теодор Нетте"
# my_text = input('Введите фразу для расчета количества слов, содержащихся в ней: ')
#
#
# def words_count():
#     txt = my_text.replace(', ', ' ')  # убираем из фразы пробелы и запятые
#     words = txt.split()
#     print(words)
#     return print(f'В указанной фразе содержится {len(words)} слов.')
#
#
# words_count()

# Задача 3
# my_text = "привет арбуз пока привет сколько Привет нисколько велосипед стол как пока слон да дела привет"
# Необходимо подсчитать сколько раз в исходной строке встречается каждое слово и вывести эту статистику в виде словаря
# Певрвый вариант решения задачи:
# d = {}
# l = list(my_text.split())
# for element in l:
#     if element in d:
#         d[element] = d[element] + 1
#     else:
#         d[element] = 1
# print(d)
# Второй вариант решения задачи:
# d = {}
# l = list(my_text.split())
# for element in l:
#     d[element] = d.get(element, 0) + 1
# print(d)


l = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50]


# Функция создания словаря из списка, где ключи строки, а значения цифры
def key_value():
    d = {}
    s = None
    for element in l:
        if type(element) == str:
            d[element] = []
            s = element
        else:
            d[s].append(element)
    return d


# print(key_value())
# Вывод ключей и значений одновременно через оператор индексации []
d = key_value()
# for key in d:
#     print(key, '-->', d[key])

# Вывод элементов словаря (ключей и значений) итерацией по .items()
d_items = d.items()
# print(d_items)

# Вывод элементов словаря в цикле for (перебор словаря с выдачей пар Ключ-Значение по одной) в виде кортежей
# for elem in d_items:
#     print(elem)
#     print(type(elem))
# Распаковка словаря (кортежей) для перебора ключей и значений словаря - в две разные переменные
# for k, v in d.items():
# print(k, '=>', v)


# Итерация через .key(), вывод только ключей
# keys = d.keys() # просто получаем ключи в новом виде
# print(keys)

# for key in d.keys():    # перебираем ключи в цикле
#     print(key)

# for key in d.keys():    # перебираем и получаем доступ к значениям через оператор индексации []
# print(key, '=>', d[key])
# print(key)
# print(d[key])

# Итерация через .values(), вывод только значений
# values = d.values()
# print(values)

# for value in d.values():    # перебираем в цикле значения и выводим
#     print(value)

# Проверяем, есть ли определенный элемент в словаре или нет (в ключах или в значениях)
# if 'five' in d.keys():
#     print(True)
# else:
#     print("Такого ключа нет в словаре")

# print(d_items)
# # for v in d_items:
# # if -50 in d_items:
# #     print('Ok')
# # else:
# #     print('No')
