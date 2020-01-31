# import random
#
# greetings = ["Чем я могу помочь вам?", "...", "Следующий!"]     # список приветствий
# MOODS = ('bad', 'average', 'good')      # кортеж с настроениями служащих
# RANKS = ('low', 'medium', 'high')       # кортеж с рангами служащих
#
# class Bureaucrat:       # создаем класс государственных служащих
#     """A government employee who works in the insitution"""
#
#     def __init__(self):
#         self.rank = random.choice(RANKS)
#         self.mood = random.choice(MOODS)
#
#     def greet(self):
#         """Функция выдает случайное приветствие служащего"""
#
#         print(random.choice(greetings))
#         print("The Bureaucrat is of a {} rank.".format(bureaucrat.rank))
#         print("The bureaucrat's mood seems to be {}.".format(bureaucrat.mood))
#
# bureaucrat = Bureaucrat()
# bureaucrat.greet()

# class Dog:
#     """простая модель собаки"""
#
#     def __init__(self, name, age):
#         """инициализируем атрибуты: имя и возраст"""
#         self.name = name
#         self.age = age
#         print('Собака создана/инициализирована.')
#
#     def sit(self):
#         """собака будет садиться по команде"""
#         print(self.name.title() + ' сел')
#
#     def jamp(self):
#         """Собака будет прыгать"""
#         print(self.name.title() + ' прыгнула')
#
#     def gav(self):
#         """Собака будет лаять"""
#         print('Гав-гав')
#
#
# my_dog = Dog('Лайка', 4)
# my_dog2 = Dog('Байкал', 2)
# poppy = Dog('Поппи', 1)
#
# poppy.gav()

# class Car:
#     """класс по созданию автомобиля"""
#
#     def __init__(self, firm, model, year):
#         """инициализация атрибутов автомобиля"""
#         self.firm = firm
#         self.model = model
#         self.year = year
#         self.odometer = 0
#
#     def description(self):
#         """возвращаем описание автомобиля"""
#         desc = str(self.firm) + ' ' + str(self.year)
#         return desc.title()
#
#     def read_odometer(self):
#         """Вывод пробега автомобиля"""
#         print(f"Пробег моего автомобиля составляет: {self.odometer} км.")
#
#     def update_odometer(self, km):
#         """устанавливаем значение на одометре"""
#         if km >= self.odometer:
#             self.odometer = km
#         else:
#             print("Не стоит баловаться со счетчиком пробега!")
#
#     def increment_odometer(self, km):
#         """увеличиваем пробег одометра на заданную величину"""
#         if km >= 0:
#             self.odometer += km
#         else:
#             print("Нельзя установить отрицательное значение пробега.")
#
#
# my_auto = Car('Audi', 'A4', 2017)
# my_car = Car('Renault Duster', '', 2016)
#
# print(my_auto.description())
# print(my_car.description())
# my_car.update_odometer(65000)
# my_car.increment_odometer(1000)
# my_car.read_odometer()
