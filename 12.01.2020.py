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

# Основной цикл программы:
for flat in flats_list:
    subway = flat[3].replace("м.", "")  # убираем буквы "м." у станций метро
    if "новостройка" in flat:
        id_newbuild_list.append(flat[0])  # заносим в список новостройки (ID новостроек)
        subway_newbuild_list.append(subway)  # заносим в список станции метро с новостройками
    elif "вторичка" in flat:
        id_oldbuild_list.append(flat[0])  # заносим в список вторичное жилье (ID вторичек)
        subway_oldbuild_list.append(subway)  # заносим в список станции метро с вторичкой

    subway_dict.setdefault(subway,
                           [])  # проверяет наличие ключа в словаре, если отсутствует, то создает пару с ключем и значением по умолчанию (None),
    # если такой ключ в словаре есть, то возвращает значение по этому ключу
    subway_dict[subway].append(flat[0])  # наполняем словарь значениями (ID квартир)

    flatinfo_dict.setdefault(flat[0], [])
    flatinfo_dict[flat[0]].append(flat[1])

# Исключаем повторяющиеся станции метро для новостроек и вторички (используем множества)
subway_new_set = set(subway_newbuild_list)
subway_old_set = set(subway_oldbuild_list)
# # print(type(subway_new_set))   # проверяем тип объекта
################################################################################################
# Итоговый вывод по новостройкам и вторичному жилью (TODO 1.1, 1.2)
print(f"Всего квартир: {len(flats_list)}")
print(f"Из них новостроек: {len(id_newbuild_list)}, вторичного жилья: {len(id_oldbuild_list)}")
print("Список ID новостроек:")
for elem in id_newbuild_list:
    print(elem, end="; ")
print()
print("Список ID вторичного жилья:")
for elem in id_oldbuild_list:
    print(elem, end="; ")
print()
print()
print("*****************************************************************************************")
################################################################################################
# Описание квартиры в виде словаря, а не списка (TODO 2.1):
print()
print("*****************************************************************************************")
print("Описание квартиры в виде словаря с определенными полями:")
for flat in flats_list:
    f_id = flat[0]
    f_rooms = flat[1]
    f_type = flat[2]
    f_price = flat[11]

    flatinfo_dict = {"id": f_id, "rooms": f_rooms, "type": f_type, "price": f_price}
    print(flatinfo_dict)
################################################################################################
# Количество квартир по каждой станции метро (TODO 2.3):
for sub, i in subway_dict.items():
    if sub != '':
        print(f"Количество квартир на станции метро {sub} составляет: {len(i)}")
for sub, i in subway_dict.items():
    if sub == '':
        print()
        print(f"Количество квартир без указания станции метро составляет: {len(i)}")
################################################################################################
