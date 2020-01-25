directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

numbers_list = []


def dir_dic(x):
    number = input("Введите номер документа: >>> ")
    type = input("Укажите тип документа (паспорт, счет, СНИЛС): >>> ")
    name = input("Укажите имя и фамилию владельца документа: >>> ")
    numbers_list.append(number)
    q = input("Если хотите добавить еще один номер, нажмите клавишу 1, если не хотите - нажмите любую клавишу: >>> ")
    if q == 1:
        dir_dic(directories)
    for i in range(3, 6):
        i = str(i)
        if q != 1:
            directories[i] = directories.setdefault(i, numbers_list)


dir_dic(directories)
print(directories)
