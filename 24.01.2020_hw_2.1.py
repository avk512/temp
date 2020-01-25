# Тестирование примеров по функциям для домашнего задания по лекции 2.1
# Домашнее задание по лекции 2.1 по функциям: https://github.com/netology-code/py-homework-basic/tree/master/2.1.functions
# 1:36:36 - разъяснение по домашнему заданию

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
print_list = [
    'Гражданина с таким номером документа в базе нет. Проверьте корректность ввода номера.',
    'Полки, на которой находится документ с указанным номером, в базе нет. Проверьте правильность ввода номера.',
    'Введенный вами номер документа уже существует в базе. Проверьте корректность ввода номера.'
]

# 1 функция: выбор пользователя = p (people)
# def number_name(number):
#     """
#     Функция определения имени гражданина по номеру его документа
#     :param number: номер документа
#     :return: имя гражданина с таким номером документа
#     """
#     isnumber = None
#     number = input("Введите номер документа: >>> ")
#     for elem in documents:
#         if number in elem.values():
#             isnumber = True
#             return print(f"Этот документ принадлежит гражданину с именем: {elem['name']}")
#         else:
#             isnumber = False
#     if isnumber == False:
#         print(print_list[0])
#         choice = input(
#             "Если хотите продолжить, нажмите клавишу 1, если хотите выйти из программы, нажмите любую иную клавишу:>>> ")
#         if choice == '1':
#             number_name(documents)
#         else:
#             print("Программа завершена. До свидания.")
# number_name(documents)

# 2 функция: вывод списка всех документов = l (list)
# def list_of_docs(dic):
#     """
#     Функция вывода списка всех документов
#     :param dic: словарь с документами
#     :return: вывод по заданному формату
#     """
#     print("Список всех документов:")
#     for elem in documents:
#         print(f"{elem['type']} \"{elem['number']}\" \"{elem['name']}\"")
# list_of_docs(documents)

# 3 функция: вывод номера полки = s (shelf)
# def number_shelf(dic):
#     """
#     Функция вывода номера полки, на которой находитс документ с указанным номером
#     :param dic: словарь полок
#     :return: вывод номера полки
#     """
#     isnumber = None
#     number = input("Введите номер документа: >>> ")
#     for key, value in directories.items():
#         if number in value:
#             isnumber = True
#             print(f"Документ №{number} находится на полке с номером {key}")
#     if isnumber != True:
#         print(print_list[1])
#         choice = input(
#         "Если хотите продолжить, нажмите клавишу 1, если хотите выйти из программы, нажмите любую иную клавишу:>>> ")
#         if choice == '1':
#             number_shelf(directories)
#         else:
#             print("Программа завершена. До свидания.")
# number_shelf(directories)

# 4 функция: добавление документа на полку - a(add)
# def add_doc_shelf():
#     pass

# Логика работы фунукции:
# 1. У пользователя спрашивают данные для добавления в базы:
#     - номер документа
#     - тип документа
#     - имя владельца
# 2. Проверка наличия номера документа в базе:
#     - если такой номер есть в базе, то добавление не происходит (предполагается, что номер уникален)
#     - если номер уникальный, то будет происходить добавление
# 3. Добавление документа (типа, номера, владельца) в список документов
# 4. Добавление документа (номера документа) в словарь полок: ключ - номер полки, значение - номер документа
isnumber = None
new_dic = dict()
number = input("Введите номер документа: >>> ")
for value in directories.values():
    if number in value:
        isnumber = True
        print(print_list[2])
        print(f"isnumber is {isnumber}")
        break

# print(isnumber)
# print(number)
if isnumber != True:
    type = input("Укажите тип документа (паспорт, счет, СНИЛС): >>> ")
    name = input("Укажите имя и фамилию владельца документа: >>> ")
    new_dic = {'type': type, 'number': number, 'name': name}
    documents.append(new_dic)
    directories['3'] = [number]

print(documents)
print(directories)
