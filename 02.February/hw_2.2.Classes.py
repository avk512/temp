# Задача №1
# # Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с
# животными и дополнить их в дочерних классах, если потребуется.
from pprint import pprint


class Animals:
    """Общий класс всех животных - базовый класс"""
    animalCount = 0  # количество всех животных
    animalWeight = 0  # общий вес всех животных
    animalDic = {}

    @staticmethod
    def statistics():
        print(f"Всего на ферме {Animals.animalCount} животных.")
        print(f"Общий вес всех животных на ферме составляет: {Animals.animalWeight} кг.")
        # print(f"Самое тяжелое животное на ферме - {} с весом {}.")
        # print(f"Самое легкое животное на ферме - {} с весом {}.")

    def __init__(self, name, weight, vid):
        """Инициализация экземпляра класса с атрибутами: имя, вес, вид животного"""
        self.name = str(name).title()
        self.weight = weight
        self.vid = str(vid).upper()
        Animals.animalCount += 1  # с каждым новым экземпляром увеличиваем общее кол-во животных
        Animals.animalWeight += weight  # c каждым новым экземпляром увеличиваем общий вес всех животных
        self.animalDic[self.name] = [self.vid, self.weight]

    def __str__(self):
        """Возврат строки, которая содержит значение атрибута (name) - образец для вывода: print(mlk3)"""
        rep = "\nОбъект класса Animals \n"
        rep += "имя: " + self.name + "\n"
        return rep

    def feed(self):  # общий метод: кормить животных
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' накормлено, напоено и довольно жизнью.")


class Birds(Animals):
    """Класс для куриц (наследование от общего класса Animals)"""

    def eggs(self):  # метод для птиц: сбор яиц
        print(f"'{self.vid}' с именем '{self.name}' снесла яйца. Их мы и собрали.")


class Mammals(Animals):
    """Класс млекопитающих (наследование от общего класса животных"""

    def milk(self):  # метод для млекопитающих: доение
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' подоено.")

    def shearing(self):  # метод для млекопитающих: стрижка
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' подстрижено.")


# print("*** ФЕРМА ДЯДЮШКИ ДЖО *** \n")
# Animals.statistics()
# print()
bird1 = Birds('ко-ко', 3, 'курица')
bird2 = Birds('кукареку', 4, 'петух')
bird3 = Birds('кряква', 5, 'утка')
bird4 = Birds('серый', 6, 'гусь')
bird5 = Birds('белый', 7, 'гусь')
mlk1 = Mammals('манька', 643, 'корова')
mlk2 = Mammals('барашек', 23, 'баран')
mlk3 = Mammals('кудрявая', 25, 'овца')
mlk4 = Mammals('рога', 24, 'коза')
mlk5 = Mammals('копыта', 27, 'коза')


# print(
#     f"На ферме дядюшки Джо есть: {bird1.vid} по имени '{bird1.name}' весом {bird1.weight} кг, {bird2.vid} по имени '{bird2.name}' весом {bird2.weight} кг,")
# Animals.statistics()


def main():
    """Пользовательский выбор"""
    select_input = input(
        "Если хотите покормить животных, нажмите клавишу 1; Если хотите подстричь животных, нажмите клавишу 2; Если "
        "хотите собрать яйца у птиц, нажмите клавишу 3; Если хотите подоить животных, нажмите клавишу 4; Для выхода "
        "нажмите любую иную клавишу. >>> \n")
    if select_input == '1':
        bird1.feed()
        bird2.feed()
        bird3.feed()
        bird4.feed()
        bird5.feed()
        mlk1.feed()
        mlk2.feed()
        mlk3.feed()
        mlk4.feed()
        mlk5.feed()
    elif select_input == '2':
        mlk2.shearing()
        mlk3.shearing()
        mlk4.shearing()
        mlk5.shearing()
    elif select_input == '3':
        bird1.eggs()
        bird3.eggs()
    elif select_input == '4':
        mlk1.milk()
    else:
        print("Программа завершена. До свидания.")


# main()
pprint(Animals.animalDic)
