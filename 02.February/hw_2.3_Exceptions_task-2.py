### Задача 2 по исключениям - проверять через assert и ловить ошибки через try/except

operator_list = ['+', '-', '*', '/']  # список операторов
try:
    oper1 = int(input("Введите первое число: >>> "))
    oper2 = int(input("Введите второе число: >>> "))
    action = input("Вам доступны четыре операции (оператора): сложение (+), вычитание (-), умножение () и деление (). "
                   "Введите нужный вам оператор: >>> ")
    try:
        assert (action in operator_list)
    except AssertionError:
        print(f"Введенный символ '{action}' не является доступным оператором.")


    def operations(operand1, operand2, operator):
        if action == '+':
            result = operand1 + operand2
            return result
        elif action == '-':
            result = operand1 - operand2
            return result
        elif action == '*':
            result = operand1 * operand2
            return result
        elif action == '/':
            try:
                result = operand1 // operand2
            except ZeroDivisionError:
                print(f"Ваш второй операнд '{operand2}, а на ноль делить нельзя!'")
            else:
                return result


    itog = operations(oper1, oper2, action)
    if itog != None:
        print(f"Результат операции: {itog}")
    else:
        print("Результат: 0")

except ValueError:
    print("Нужно ввести целое число! ")
