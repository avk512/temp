import csv
from pprint import pprint

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

# создание файла и запись в файл данных (списка)
with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)  # создаем объект для записи в файл
    writer.writerows(users)  # запись в файл списка

# добавление в файл csv новой одной записи (из списка)
with open("users.csv", "a", newline="") as f:
    user = ["Sam", 41]
    writer = csv.writer(f)
    writer.writerow(user)  # запись в файл только одной строки

# чтение из файла csv
with open("users.csv", newline="") as f:
    reader = csv.reader(f)  # создаем объект для чтения из файла
    for row in reader:
        pprint(row)
        print(row[0], "->", row[1])

users2 = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]
# создание файла и запись в файл данных (из словаря)
with open("users2.csv", "w", newline="") as f:
    columns = ["name", "age"]  # данные для заголовка
    writer = csv.DictWriter(f,
                            fieldnames=columns)  # создаем объект для записи в файл с заголовком
    writer.writeheader()  # запись в файл заголовка

    writer.writerows(users2)  # запись в файл данных из словаря

    user2 = {"name": "Sam", "age": 41}
    writer.writerow(user2)  # запись в файл одиночных данных из словаря

# чтение файла
with open("users2.csv", newline="") as f:
    reader = csv.DictReader(f)  # создаем объект для чтения из файла
    for row in reader:
        print(f"{row['name']} => {row['age']} ")
