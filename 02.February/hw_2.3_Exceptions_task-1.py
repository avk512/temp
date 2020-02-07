### Задача №1: Реализовать польскую нотацию

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
