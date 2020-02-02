# Задача №1
# # Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с
# животными и дополнить их в дочерних классах, если потребуется.

class Animals:
    """Общий класс всех животных"""
    animalCount = 0  # количество всех животных
    animalWeight = 0  # общий вес всех животных
    birdCount = 0  # количество видов птиц
    mlkCount = 0  # количество видов млекопитающих

    def __init__(self, name, weight, vid):
        """Инициализация экземпляра класса с атрибутами: имя, вес, вид животного, его голос"""
        self.name = str(name).title()
        self.weight = weight
        self.vid = str(vid).title()
        Animals.animalCount += 1  # с каждым новым экземпляром увеличиваем общее кол-во животных
        Animals.animalWeight += weight  # c каждым новым экземпляром увеличиваем общий вес всех животных

    def feed(self):  # общий метод: кормить животных
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' накормлено и напоено.")


class Birds(Animals):
    """Класс птиц (наследование от общего класса животных)"""
    Animals.birdCount += 1
    voice = ''

    def eggs(self):  # метод для птиц: сбор яиц
        pass


class Mammals(Animals):
    """Класс млекопитающих (наследование от общего класса животных"""
    Animals.mlkCount += 1

    def milk(self):  # метод для млекопитающих: доение
        pass

    def shearing(self):  # метод для млекопитающих: стрижка
        pass


bird1 = Birds('Серый', 6, 'гусь')
bird2 = Birds('Белый', 4, 'гусь')
bird3 = Birds('Зеленый', 2, 'гусь')
mlk1 = Mammals('Манька', 643, 'корова')

bird1.feed()
print(f"{bird1.vid} с именем '{bird1.name}' весит {bird1.weight} кг.")
print(f"{mlk1.vid} с именем '{mlk1.name}' весит {mlk1.weight} кг.")
print(f"Общий вес всех животных на ферме составляет: {Animals.animalWeight} кг.")
# print(f"Самое тяжелое животное на ферме: {} с весом {} кг.")
print(f"Всего животных на ферме: {Animals.animalCount}")
print(f"Всего птиц на ферме: {Animals.birdCount}")
