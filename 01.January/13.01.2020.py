import csv

flats_list = list()
with open("output.csv", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    flats_list = list(reader)

header = flats_list.pop(0)  # удаляем заголовок (поля данных) и сохраняем его в переменной на всякий случай

# Создание переменных:
subway_dict = dict()  # создаем пустой словарь для станций метро (ключ) и списка квартир на этой станции (значения)
flatinfo_dict = dict()  # создаем пустой словарь для описания квартиры (для TODO 2.1)

# Основной цикл программы:
for flat in flats_list:
    f_id = flat[0]
    f_rooms = flat[1]
    f_type = flat[2]
    f_price = flat[11]

    flatinfo_dict = {"id": f_id, "rooms": f_rooms, "type": f_type, "price": f_price}

    subway = flat[3].replace("м.", "")  # убираем буквы "м." у станций метро

    subway_dict.setdefault(subway,
                           [])  # проверяет наличие ключа в словаре, если отсутствует, то создает пару с ключем и значением по умолчанию (None),
    # если такой ключ в словаре есть, то возвращает значение по этому ключу
    subway_dict[subway].append(flatinfo_dict)
print(subway_dict)
