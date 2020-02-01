import csv

flats_list = list()
with open("output.csv", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    flats_list = list(reader)

header = flats_list.pop(0)  # удаляем заголовок (поля данных) и сохраняем его в переменной на всякий случай

# Создание переменных:
id_newbuild_list = list()  # создаем пустые списки для ID новостроек и ID вторичного жилья
id_oldbuild_list = list()
# print(type(id_newbuild_list))   # проверяем тип объекта
subway_newbuild_list = list()  # создаем пустые списки для станций метро для новостроек и вторички
subway_oldbuild_list = list()
subway_dict = dict()  # создаем пустой словарь для станций метро (ключ) и списка квартир на этой станции (значения)
flatinfo_dict = dict()  # создаем пустой словарь для описания квартиры с избранными полями-значениями (для TODO 2.1)

# TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки и их порядковые номера в файле.
# Подсказка - вам нужно изменить этот код:
# for flat in flats_list:
#   if "новостройка" in flat:
#     print("{}".format(flat))
# 2) добавьте в код подсчет количества новостроек

######################################################################
# РЕШЕНИЕ TODO 1 #

id_newbuild_list = list()  # создаем пустые списки для ID новостроек и ID вторичного жилья
id_oldbuild_list = list()
# print(type(id_newbuild_list))   # проверяем тип объекта
subway_newbuild_list = list()  # создаем пустые списки для станций метро для новостроек и вторички
subway_oldbuild_list = list()
for flat in flats_list:
    subway = flat[3].replace("м.", "")  # убираем буквы "м." у станций метро
    if "новостройка" in flat:
        id_newbuild_list.append(flat[0])
        subway_newbuild_list.append(subway)
    elif "вторичка" in flat:
        id_oldbuild_list.append(flat[0])
        subway_oldbuild_list.append(subway)
    subway_dict.setdefault(subway,
                           [])  # проверяет наличие ключа в словаре, если отсутствует, то создает пару с ключем и значением по умолчанию (None),
    # если такой ключ в словаре есть, то возвращает значение по этому ключу
    subway_dict[subway].append(flat[0])  # наполняем словарь значениями (ID квартир)

# Исключаем повторяющиеся станции метро для новостроек и вторички (используем множества)
subway_new_set = set(subway_newbuild_list)
subway_old_set = set(subway_oldbuild_list)
# print(type(subway_new_set))   # проверяем тип объекта

# # Итоговый вывод по новостройкам и вторичному жилью
# print(f"Всего квартир: {len(flats_list)}")
# print(f"Из них новостроек: {len(id_newbuild_list)}, вторичного жилья: {len(id_oldbuild_list)}")

# print("Список ID новостроек:")
# for elem in id_newbuild_list:
#   print(elem, end="; ")
# print()
# print("Список ID вторичного жилья:")
# for elem in id_oldbuild_list:
#   print(elem, end="; ")

######################################################################

# TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
# flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1
# subway_dict = {}
# for flat in flats_list:
#   subway = flat[3].replace("м.", "")
#   if subway not in subway_dict.keys():
#     subway_dict[subway] = list()
#   subway_dict[subway].append(flat[0])
# print(subway_dict)

# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.

######################################################################
# РЕШЕНИЕ TODO 2 #
# 1)
print("*****************************************************************************************")
print("Описание квартиры в виде словаря с определенными полями:")
for flat in flats_list:
    f_id = flat[0]
    f_rooms = flat[1]
    f_type = flat[2]
    f_price = flat[11]

    flatinfo_dict = {"id": f_id, "rooms": f_rooms, "type": f_type, "price": f_price}
    print(flatinfo_dict)
print()

################################################################################################
# 2)
print("*****************************************************************************************")
# Словарь со значениями из todo 2.1:
print()
for flat in flats_list:
    f_id = flat[0]
    f_rooms = flat[1]
    f_type = flat[2]
    f_price = flat[11]

    flatinfo_dict = {"id": f_id, "rooms": f_rooms, "type": f_type, "price": f_price}

    subway = flat[3].replace("м.", "")  # убираем буквы "м." у станций метро

    subway_dict.setdefault(subway, [])
    subway_dict[subway].append(flatinfo_dict)
    print(subway_dict)

#################################################################################################
# 3)
print("*****************************************************************************************")
# Количество квартир по каждой станции метро (TODO 2.3):
for sub, i in subway_dict.items():
    if sub != '':
        print(f"Количество квартир на станции метро {sub} составляет: {len(i)}")
for sub, i in subway_dict.items():
    if sub == '':
        print()
        print(f"Количество квартир без указания станции метро составляет: {len(i)}")
