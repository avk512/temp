operator_list = ['+', '-', '*', '/']  # список операторов
print("Вам доступны четыре операции (оператора): сложение (+), вычитание (-), умножение () и деление (). ")
s = input(
    "Введите выражение в префиксной (польской) нотации, например: + 2 2, добавляя пробелы между оператором и цифрами: >>> ")
inp_list = s.split()
print(f"Вы ввели: {inp_list}")
try:
    assert (inp_list[0] in operator_list)
except AssertionError:
    print(f"Введенный символ '{inp_list[0]}' не является доступным оператором.")

try:
    assert int(inp_list[1]) == True and int(inp_list[2]) == True
except (ValueError, AssertionError):
    print("Это не цифры2")


# def isint(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return print("Это не цифра")


def operations(operand1, operand2, operator):
    if operator == '+':
        result = operand1 + operand2
        return result
    elif operator == '-':
        result = operand1 - operand2
        return result
    elif operator == '*':
        result = operand1 * operand2
        return result
    elif operator == '/':
        try:
            result = operand1 // operand2
        except ZeroDivisionError:
            print(f"Ваш второй операнд '{operand2}, а на ноль делить нельзя!'")
        else:
            return result


itog = operations(int(inp_list[1]), int(inp_list[2]), inp_list[0])
print(itog)
