#####       Структура класса          ###
# class ИмяКласса:
#   ПеременнаяКласса = Значение
#   ...
#   def ИмяМетода(self, аргументы):
#       self.ПеременнаяКласса = Значение
#       ...
# ...
#########################################

# class Second:
#     color = 'red'
#     form = 'circle'
#
#     def change_color(self, newcolor):
#         self.color = newcolor
#
#     def change_form(self, newform):
#         self.form = newform
#
#
# ob1 = Second()
# ob2 = Second()
#
# print(ob1.color, ob1.form)
# print(ob2.color, ob2.form)
#
# ob1.change_color('green')
# ob2.change_color('blue')
# ob1.change_form('oval')
# ob2.change_form('kvadrat')
#
# print(ob1.color, ob1.form)
# print(ob2.color, ob2.form)


# class YesInit:
#     def __init__(self, one, two):
#         self.fname = one
#         self.sname = two
#
# ob1 = YesInit("Peter", "Ok")
# print(ob1.fname,ob1.sname)
#
# class NoInit:
#     def names(self, one, two):
#         self.fname = one
#         self.sname = two
#
# ob2 = NoInit()
# ob2.names("Peter", "Ok")
# print(ob2.fname, ob2.sname)

# class Employee:
#     """Создаем класс служащего (работника)"""
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def display_employee(self):
#         print(f"Имя: {self.name}, зарплата: {self.salary} руб.")
#
#
# emp1 = Employee("Зара", 2000)
# emp2 = Employee("Петр", 2500)
# emp3 = Employee("Николай", 2200)
# all = Employee.empCount
#
# emp1.display_employee()
# emp2.display_employee()
# emp3.display_employee()
# print(f"Всего служащих (работников): {all}")


# class User:
#     """Класс для всех покупателей"""
#     user_count = 0  # переменная-счетчик всех покупателей в самом начале
#     user_status = 0
#
#     def __init__(self, name, age, address, bonus, loyalty):  # инициализируем класс со свойствами всех покупателей: имя, возраст, адрес,
#         # бонусные баллы, уровень лояльности (от 0 до 3)
#         self.name = name
#         self.age = age
#         self.address = address
#         self.bonus = bonus
#         self.loyalty = loyalty
#         User.user_count += 1    # увеличиваем количество покупателей на единицу при создании каждого нового покупателя
#
#     def add_bonus(self, bonus_count):
#         """Определяем метод начисления бонусных баллов"""
#         self.bonus += bonus_count   # Количество бонусных баллов
#         self.loyalty = self.bonus // 10000   # подсчет уровня лоялности (целая часть от деления)
#         if self.loyalty > 3:
#             self.loyalty = 3
#         print(f"Бонусный уровень покупателя {self.name}: {self.loyalty}.")
#
# # Создаем покупателей, опираясь на класс (создаем экземпляр покупателя):
# user1 = User('Николай', 24, 'Чебоксары', 0, 0)
# user1.add_bonus(15000)
# user2 = User('Елена', 20, 'Москва', 3000, 0)
# user2.add_bonus(5000)
# user3 = User('Марина Владимировна', 35, 'Санкт-Петербург', 0, 1)
# user4 = User('Петр', 40, 'Мурманск', 5000, 2)
# user5 = User('Сергей', 27, 'Вологда', 8000, 1)
# user5.add_bonus(10000)


# Задачи по ролику "Классы, ООП" ######################
#
# class Restaurant:
#     """Класс Ресторан"""
#
#     def __init__(self, name, cuisine_type):
#         """инициализация класса с двумя аргументами-атрибутами"""
#         self.name = name  # имя ресторана
#         self.cuisine = cuisine_type  # тип кухни
#
#     def describe_r(self):
#         """Функция вывода атрибутов ресторана: название ресторана и тип кухни"""
#         print(f"Ресторан '{self.name}': {self.cuisine} кухня")
#
#     def open_r(self):
#         """Функция вывода сообщения о том, что ресторан открыт"""
#         print(f"Ресторан '{self.name}' открыт для гостей!")

# rs1 = Restaurant('Плакучая Ива', 'русская')
# rs2 = Restaurant('Темная ночь', 'средиземноморская')
# rs3 = Restaurant('Шанталь', 'кавказская')
#
# rs1.describe_r()
# rs1.open_r()
# rs2.describe_r()
# rs2.open_r()
# rs3.describe_r()
# rs3.open_r()
#
# class User:
#     """Класс пользователей"""
#     user_count = 0
#
#     def __init__(self, first_name, last_name, age, address):
#         """Создание экземпляря пользователя с общими атрибутами (профиль пользователя)"""
#         self.f_name = str(first_name).title()
#         self.l_name = str(last_name).title()
#         self.age = age
#         self.address = address
#         User.user_count += 1
#
#     def describe(self):
#         """Вывод сводки по пользователю"""
#         print(f"Пользователь: {self.f_name} {self.l_name}: возраст - {self.age}, адрес - {self.address}.")
#
#     def greeting(self):
#         """Вывод персонального приветствия пользователя"""
#         print(f"Приветствуем тебя, {self.f_name} {self.l_name}!")
#
#
# user1 = User('иннокентий', 'Петров', 35, 'Москва')
# user2 = User('Николай', 'иванов', 22, 'Вологда')
# user3 = User('снежана', 'батагова', 18, 'Симферополь')
# user4 = User('юлия', 'жмулия', 23, 'Киев')
#
# user1.describe()
# user2.describe()
# user3.describe()
# user4.describe()
#
# user1.greeting()
# user2.greeting()
# user3.greeting()
# user4.greeting()
