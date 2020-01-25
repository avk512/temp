directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def dir_dic(x):
    for i in range(3, 100):
        number = input("Введите номер документа: >>> ")
        type = input("Укажите тип документа (паспорт, счет, СНИЛС): >>> ")
        name = input("Укажите имя и фамилию владельца документа: >>> ")
        dir_dic = {}
        directories[i] = [number]
        return directories


dir_dic(directories)
# print(directories)
