documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

print("***** ", "Программа перемещения документа с одной полки на другую", "*****")
print()
isnum = None
dir_keys = list(directories.keys())  # список ключей (перечисление названий всех полок)
num_doc = input("Введите номер документа, который вы хотите переместить: >>> ")
for k, v in directories.items():
    if num_doc in v:
        isnum = True
        print(f"Документ с номером {num_doc} находится на полке №{k}.")
        print(f"Всего полок: {len(directories)}, их номера:  {', '.join(dir_keys)}.")
        sh = input("Выберите номер полки, куда вы хотите переместить документ: >>> ")
        if sh not in directories:
            print("Такой полки нет.")
        elif sh == k:
            print("Документ уже находится на этой полке. Укажите другой номер полки.")
        elif sh != k:
            v.remove(num_doc)
            directories[sh].append(num_doc)
            # break
    for k, v in directories.items():
        if num_doc in v:
            print(f"Документ с номером {num_doc} перемещен на полку №{k}.")
            print(directories)
    break
