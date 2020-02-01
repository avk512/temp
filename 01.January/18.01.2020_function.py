# Лекция 6. Функции - использование встроенных и создание собственных

# def square(number):
#     """
#     это функция по возведению в квадрат
#     """
#     result = number ** 2
#     return result
#
#
# a = square(10)


# print(a)

# help(square)

# def square_2():
#     user_input = int(input("Введите число: "))
#     result = user_input ** 2
#     return result
#
# print(square_2())

# def power(number_1, number_2):
#     """Возведение числа number_1 в степень числа number_2"""
#     result = number_1 ** number_2
#     return result
#
# print(power(6, 8))

# def power2(number_1, number_2=2):
#     """Возведение числа number_1 в степень числа number_2"""
#     result = number_1 ** number_2
#     return result


# print(power2(8))  # если заранее известно, что будет возведение в квадрат, то достаточно одного аргумента в выводе


# def power3():
#     """Возведение в квадрат с проверкой ввода (обработка исключений)"""
#     user_input = input("Введите любое число: ")
#     try:
#         user_input = int(user_input)
#         result = user_input ** 2
#         return result
#
#     except ValueError:
#         print("Введите число, а не строку!")
#         return power3()
#
#
# print(power3())

# def power4(number):
#     result = number ** 2
#     print(result)
#
# print(power4(5))

# number = 5
# power = 2
#
# def square():
#     number = 6
#     # power = 3
#     some_number = 1
#     return number ** power
#
# # print(number ** power)
# # print(square())
# print(some_number)

# name = "James"
# print(name)
# def say_hy():
#     global name
#     name = "Oleg"
#     print("Hello", name)
#
# say_hy()
# print(name)

# def say_hy():
#     name = 'Oleg'
#     def get_name():
#         nonlocal name
#         name = input('Введите имя: ')
#         return name
#     get_name()
#     print('Hello', name)
#
# say_hy()

# Лямбда-функции или анонимные функции
# Анонимные функции создаются при помощи инструкции lambda и используются для более краткой записи функций с одним
# выражением. Выполняются быстрее обычных и не требуют инструкции return:
# lambda x, pow: x**pow
# func = lambda переменная 1, переменная 2: выражение
# вызов анонимной функции: print(func(переменная 1, переменная 2))

# result = lambda x, y: x+y
# print(result(5, 7))

# Примеры использования функций
# Написать функцию подсчета средних оценок по всей группе за экзамен и за Домашние задания
student_list = [
    {"name": "Василий", "surname": "Теркин", "sex": "мужчина", "program_exp": True, "grade": [8, 8, 9, 10, 9],
     "exam": 9},
    {"name": "Мария", "surname": "Павлова", "sex": "женщина", "program_exp": True, "grade": [7, 8, 9, 7, 9], "exam": 8},
    {"name": "Ирина", "surname": "Андреева", "sex": "женщина", "program_exp": False, "grade": [10, 9, 8, 10, 10],
     "exam": 10},
    {"name": "Татьяна", "surname": "Сидорова", "sex": "женщина", "program_exp": False, "grade": [7, 8, 8, 9, 8],
     "exam": 8},
    {"name": "Иван", "surname": "Васильев", "sex": "мужчина", "program_exp": True, "grade": [9, 8, 9, 6, 9],
     "exam": 10},
    {"name": "Роман", "surname": "Золотарев", "sex": "мужчина", "program_exp": False, "grade": [8, 9, 9, 6, 9],
     "exam": 10}
]


def get_average_grade(students):
    # Создаем переменные для сумм оценок экзмена и оценок домашних заданий
    sum_average_ex = 0
    sum_average_hw = 0
    for student in students:
        # print(number)
        sum_average_ex += student['exam']
        sum_average_hw += sum(student['grade']) / len(student['grade'])
    # print(sum_average_ex)
    # print(sum_average_hw)
    print(f"Средняя оценка за ДЗ равна: {round(sum_average_hw / len(students), 2)}")
    print(f"Средняя оценка за экзамен равна: {round(sum_average_ex / len(students), 2)}")


# get_average_grade(student_list)

def get_average_grade_by_gender(students, gender):
    # Создаем переменные для сумм оценок экзмена и оценок домашних заданий
    sum_average_ex = 0
    sum_average_hw = 0
    student_counter = 0
    for student in students:
        if student['sex'] == gender:
            sum_average_ex += student['exam']
            sum_average_hw += sum(student['grade']) / len(student['grade'])
            student_counter += 1
    # print(sum_average_ex)
    # print(sum_average_hw)
    print(f"Средняя оценка за ДЗ равна: {round(sum_average_hw / student_counter, 2)}")
    print(f"Средняя оценка за экзамен равна: {round(sum_average_ex / student_counter, 2)}")


# get_average_grade_by_gender(student_list, 'мужчина')
# get_average_grade_by_gender(student_list, 'женщина')

def main():
    while True:
        user_input = input(
            "Введите команду: 1 (для вывода средних оценок всех студентов), 2 (для мужчин), 3 (для женщин), q (для выхода из программы): ")
        if user_input == '1':
            get_average_grade(student_list)
        elif user_input == '2':
            get_average_grade_by_gender(student_list, 'мужчина')
        elif user_input == '3':
            get_average_grade_by_gender(student_list, 'женщина')
        elif user_input == 'q':
            print("Программа завершена. До свидания.")
            break


main()

#### Пример для себя, вопрос задавал в тостере (https://qna.habr.com/q/701600) ####
# s_list = [
#     {'one': 1, 'two': 2, 'seven': 7, 'fix': 'price', 'number': [5, 4, 2, 3, 5, 4], 'dig': 4},
#     {'one': 5, 'two': 4, 'seven': 6, 'fix': 'nix', 'number': [3, 5, 7, 2, 3, 9], 'dig': 5},
#     {'one': 8, 'two': 3, 'seven': 9, 'fix': 'pix', 'number': [3, 2, 3, 1, 8, 4], 'dig': 9}
# ]
# print(s_list[1]['number'])
# for x, y in s_list:
#     # print(x['number'])
#     print(x['number'][y])
# for i, x in enumerate(s_list):
#     print(f"List's element = {i}")
#     for key, value in x.items():
#         print(f"key = {key} and value = {value}")
