# import sys

# try:
#     value = int(input("Введите число от 1 до 10: >>> "))
# except ValueError:
#     print("Нужно ввести число от 1 до 10!")
# else:
#     if (value > 0) and (value <=10):
#         print(f"Вы ввели число '{value}'")
#     else:
#         print("Введенное значение некорректно!")

# try:
#     value = int(input("Введите число от 1 до 10: >>> "))
# except ValueError:
#     print("Нужно ввести число от 1 до 10!")
# except:
#     print("Обобщенная ошибка!")
# else:
#     if (value > 0) and (value <= 10):
#         print("Вы ввели число '{value}'")
#     else:
#         print("Введенное значение некорректно!")


# try:
#     File = open('mytext.txt')
# except IOError as e:
#     for entry in dir(e):
#         if (not entry.startswith("_")):
#             try:
#                 print(entry, " = ", e.__getattribute__(entry))
#             except AttributeError:
#                 print(f"Атрибут {entry} недоступен.")
#     # for arg in e.args:
#     #     print(arg)
#     # print(f"Ошибка при открытии файла.\r\nНомер ошибки: {e.errno}\r\nТекст ошибки: {e.strerror}")
# else:
#     print("Файл открыт, как ожидалось.")
#     File.close()

# try:
#     value = int(input("Введите число от 1 до 10: >>> "))
# except (ValueError, KeyboardInterrupt):
#     print("Нужно ввести число от 1 до 10!")
# else:
#     if (value > 0) and (value <=10):
#         print(f"Вы ввели число '{value}'")
#     else:
#         print("Введенное значение некорректно!")


def action(operator):
    """Функция вычислений"""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        try:
            return a // b
        except ZeroDivisionError:
            print("Деление на ноль невозможно. Повторите попытку, следуя предложенному шаблону.")
    else:
        return print("Первый знак не является оператором. Повторите попытку, следуя предложенному шаблону.")


s = input(
    "Введите выражение в префиксной (польской) нотации, например: + 2 2, добавляя пробелы между оператором и цифрами: >>> ")
cols = s.split()
print(f"Вы ввели: {cols}")
try:
    a = int(cols[1])
    b = int(cols[2])
    oper = (cols[0])
except:
    print(f"Введены неверные данные. Повторите попытку, следуя предложенному шаблону.")
else:
    result = action(oper)
    if result != None:
        print(f"Результат вычисления: {result}")
