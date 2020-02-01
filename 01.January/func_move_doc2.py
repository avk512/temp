directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


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
        print("Такого документа нет.")


move_doc(directories)
