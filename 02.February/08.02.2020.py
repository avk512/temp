# s = 0
# for k in range(5, 11):
#     s = s + 2 * k
#     print(s)

# s = 1
# for k in range(1, 30):
#     s = (k -5) *s
# print(s)

# temp = -1
# assert (temp > 20), "Лето еще не наступлило"

operator_list = ['+', '-', '*', '/']  # список операторов
oper1 = input("Введите первое число: >>> ")
oper2 = input("Введите второе число: >>> ")
action = input("Вам доступны четыре математические операции: сложение '+', вычитание '-', умножение '*' и деление '/'. "
               "Введите нужный вам оператор: >>> ")
try:
    assert (action in operator_list)
except AssertionError:
    print(f"Введенный символ '{action}' не является доступным оператором.")
else:
    print(f"Введенный символ '{action}' является надлежащим оператором.")
finally:
    print("Можете запустить программу заново, если вдруг не наигрались :)")
