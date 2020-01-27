# Каталог документов хранится в следующем виде:
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Перечень полок, на которых находятся документы, хранится в следующем виде:
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

# Перечень сообщений для пользователя
print_list = [
    'Гражданина с таким номером документа в базе нет. Проверьте корректность ввода номера.',
    'Полки, на которой находится документ с указанным номером, в базе нет. Проверьте правильность ввода номера.',
    'Введенный вами номер документа уже существует в базе. Проверьте корректность ввода номера.',
    'Документ с указанным номером в базе отсутствует. Проверьте корректность ввода номера.',
    'Из базы данных удалены все записи, содержащие указанный номер документа'
]


# Функция получения ключа по значению из словаря полок (directories)
def get_key(val):
    for key, value in directories.items():
        if val in value:
            return key


# def get_number_doc(dic):
#     isnum = None
#     number = input("Введите номер документа: >>> ")
#     for elem in documents:
#         if number in elem.values():
#             isnum = True
#             return print(elem)
#     if isnum != True:
#         return print(print_list[3])
#
# get_number_doc(documents)

# def get_num_dir(dic):
#     isnum = None
#     number = input("Введите номер документа: >>> ")
#     for key, val in directories.items():
#         if number in val:
#             isnum = True
#             return key, number
#     if isnum != True:
#         return print(print_list[3])

# get_num_dir(directories)


# Функция: перемещения документа - m (move)

isnum = None
number = input("Введите номер документа: ")
for val in directories.values():
    if number in val:
        isnum = True
        val.remove(number)
if isnum != True:
    print(print_list[3])

print(directories)
# move_doc(directories)

# Функция получения списка полок и преобразование их в строковый вид
# def lst(d):
#     sh_list = list(d.keys())
#     sh_str = ', '.join(sh_list)
#     return sh_list, sh_str

# Функция создания новой полки - as (add shelf)
# a, b = lst(directories)
# print(f"Количество полок в базе: {len(directories)} (под номерами: {b}).")
# new_shelf = input("Укажите номер новой полки, которую планируете добавить в базу: >>> ")
# if new_shelf in a:
#     print("Такая полка уже есть. Проверьте корректность ввода данных.")
# else:
#     directories[new_shelf] = []
#     c, n = lst(directories)
#     print(f"Вы успешно создали новую полку под номером {new_shelf}.")
#     print(f"Список имеющихся полок с номерами: {n}")
