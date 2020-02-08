# Домашнее задание по лекции 2.3: Исключения - Задача №3

# Каталог документов хранится в следующем виде:
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

documents_out = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "snils", "number": "012345"}
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
    'Из базы данных удалены все записи, содержащие указанный номер документа.'
]


# Блок вспомогательных функций ##########################

# Функция получения ключа по значению из словаря полок (directories)
def get_key(val):
    for key, value in directories.items():
        if val in value:
            return key


# Функция поиска документа по его номеру (в списке документов - documents)
def get_number_doc(doc):
    isnumber = None
    number = input("Введите номер документа: >>> ")
    for elem in doc:
        if number in elem.values():
            isnumber = True
            return elem  # возвращает словарь, содержащий значение с искомым номером документа
    if isnumber != True:
        return print(print_list[3])


# Функция получения списка полок и преобразование их в строковый вид
def lst(dir):
    sh_list = list(dir.keys())
    sh_str = ', '.join(sh_list)
    return sh_list, sh_str


# Конец блока вспомогательных функций ####################


### Задача №1 ###

# 1 функция: выбор пользователя = p (people)
def number_name(doc):
    isnumber = None
    number = input("Введите номер документа: >>> ")
    for elem in doc:
        if number in elem.values():
            isnumber = True
            return print(f"Этот документ принадлежит гражданину с именем: {elem['name']}")
        else:
            isnumber = False
    if isnumber != True:
        print(print_list[0])


# 2 функция: вывод списка всех документов = l (list)
def list_of_docs(doc):
    print("Список всех документов:")
    for elem in doc:
        print(f"{elem['type']} \"{elem['number']}\" \"{elem['name']}\"")


# 3 функция: вывод номера полки = s(shelf)
def number_shelf(dir):
    isnumber = None
    number = input("Введите номер документа: >>> ")
    for key, value in dir.items():
        if number in value:
            isnumber = True
            print(f"Документ №{number} находится на полке №{key}")
    if isnumber != True:
        print(print_list[3])


# 4 функция: добавление документа на полку - a(add)
def add_doc_shelf(doc, dir):
    isnumber = None
    number = input("Введите номер документа: >>> ")
    for value in dir.values():
        if number in value:
            isnumber = True
            print(print_list[2])
            break
    if isnumber != True:
        type = input("Укажите тип документа (паспорт, счет, СНИЛС): >>> ")
        name = input("Укажите имя и фамилию владельца документа: >>> ")
        shelf = input("Укажите номер полки, где будет храниться документ (1, 2, 3): >>> ")
        new_docs = {'type': type, 'number': number, 'name': name}
        if shelf not in dir.keys():
            print("Такой полки не существует. Проверьте корректность ввода данных.")
        else:
            doc.append(new_docs)
            dir[shelf].append(number)
            print(f"Документ под №{number} добавлен в базу и сохранен на полке №{get_key(number)}")


### Задача №2  (дополнительная) ###
# Функция: удаление документа - d (delete)
def del_doc(doc, dir):
    isnumber = None
    number = input("Введите номер документа для его удаления: >>> ")
    for ind, val in enumerate(doc):
        if number in val.values():
            isnumber = True
            doc.pop(ind)  # удаляем словарь из списка словарей по его индексу
    if isnumber != True:
        print(print_list[3])
    for value in dir.values():
        if number in value:
            isnumber = True
            value.remove(number)  # удаляем элемент из списка документов по его значению
            print(print_list[4])
            break
    # print(directories)
    # print(documents)


# Функция: перемещение документа - m (move)
def move_doc(dir):
    print("***** ", "Программа перемещения документа с одной полки на другую", "*****")
    print()
    isnum = None
    dir_keys = list(dir.keys())  # список ключей (перечисление названий всех полок)
    num_doc = input("Введите номер документа, который вы хотите переместить: >>> ")
    for k, v in dir.items():
        if num_doc in v:
            isnum = True
            print(f"Документ с номером {num_doc} находится на полке №{k}.")
            print(f"Всего полок: {len(dir)}, их номера:  {', '.join(dir_keys)}.")
            sh = input("Выберите номер полки, куда вы хотите переместить документ: >>> ")
            if sh not in dir:
                print("Такой полки нет.")
            elif sh == k:
                print("Документ уже находится на этой полке. Укажите другой номер полки.")
                break
            elif sh != k:
                v.remove(num_doc)
                dir[sh].append(num_doc)
                print(f"Документ с номером {num_doc} перемещен на полку №{sh}.")
                print(dir)
                break
    if isnum != True:
        print(print_list[3])


# Функция создания новой полки - as (add shelf)
def create_new_shelf(dir):
    a, b = lst(dir)
    print(f"Всего полок в базе: {len(dir)}, их номера: {b}.")
    new_shelf = input("Укажите номер новой полки, которую планируете добавить в базу: >>> ")
    if new_shelf in a:
        print("Такая полка уже есть. Проверьте корректность ввода данных.")
    else:
        dir[new_shelf] = []
        c, n = lst(dir)
        print(f"Вы успешно создали новую полку под номером {new_shelf}.")
        print(f"Список имеющихся полок с номерами: {n}")


# Функция вывода имен всех владельцев документов
def output_of_names(doc):
    print(f"\nВывод имен всех владельцев документов в базе:")
    for elem in doc:
        try:
            print(f"№{elem['number']} - {elem['name']}")
        except KeyError:
            print(f"№{elem['number']} - ФИО владельца документа отсутствует в базе. Уведомите программистов!")


# Функция запуска программы
def main():
    # while True:
    user_input = input(
        "Нажмите клавишу 1 (если хотите узнать, кому принадлежит документ), клавишу 2 (для вывода списка всех "
        "документов), клавишу 3 (для вывода номера полки, на которой находится документ), клавишу 4 (для "
        "добавления нового документа), клавишу 5 (для удаления документа), клавишу 6 (для перемещения документа с "
        "одной полки на другую), клавишу 7 (для создания новой полки), клавишу 8 для вывода имен всех владельцев"
        " документов или клавишу 9 для выхода из программы: >>> ")
    if user_input == '1':
        number_name(documents)
    elif user_input == '2':
        list_of_docs(documents)
    elif user_input == '3':
        number_shelf(directories)
    elif user_input == '4':
        add_doc_shelf(documents, directories)
    elif user_input == '5':
        del_doc(documents, directories)
    elif user_input == '6':
        move_doc(directories)
    elif user_input == '7':
        create_new_shelf(directories)
    elif user_input == '8':
        output_of_names(documents_out)
    elif user_input == '9':
        print("Программа завершена. До свидания.")


main()