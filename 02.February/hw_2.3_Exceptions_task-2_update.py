# Задача №2 после доработки

operator_list = ['+', '-', '*', '/']  # список операторов
op = print("Вам доступны четыре операции (оператора): сложение (+), вычитание (-), умножение () и деление (). ")
s = input(
    "Введите выражение в префиксной (польской) нотации, например: + 2 2, добавляя пробелы между оператором и цифрами: >>> ")
inp_list = s.split()
if len(inp_list) > 3 or len(inp_list) < 3:
    print("Количество символов для расчета меньше или больше ожидаемого (должен быть 1 оператор и 2 операнда)!")
    exit()

print(f"Вы ввели: {inp_list}")

try:
    assert (inp_list[0] in operator_list)
except AssertionError:
    print(f"Введенный символ '{inp_list[0]}' не является доступным оператором.")


# Проверка ввода целочисленного значения
def isint(elem):
    try:
        if type(int(elem)) == int:
            elem = int(elem)
            return elem
    except ValueError:
        print(f"Вместо '{elem}' нужно ввести целое число!")
        exit()


def op_add(isint1, isint2, operator):
    result = isint1 + isint2
    return result


def op_sub(isint1, isint2, operator):
    result = isint1 - isint2
    return result


def op_multi(isint1, isint2, operator):
    result = isint1 * isint2
    return result


def op_divis(isint1, isint2, operator):
    try:
        result = isint1 // isint2
    except ZeroDivisionError:
        print(f"Ваш второй операнд '{isint2}', а на ноль делить нельзя!")
        exit()
    else:
        return result


a = isint(inp_list[1])
b = isint(inp_list[2])

if inp_list[0] == '+':
    print(f"Итог расчета: {op_add(a, b, inp_list[0])}")
elif inp_list[0] == '-':
    print(f"Итог расчета: {op_sub(a, b, inp_list[0])}")
elif inp_list[0] == '*':
    print(f"Итог расчета: {op_multi(a, b, inp_list[0])}")
elif inp_list[0] == '/':
    print(f"Итог расчета: {op_divis(a, b, inp_list[0])}")
