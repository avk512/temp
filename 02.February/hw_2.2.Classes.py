# Задача №1
# # Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с
# животными и дополнить их в дочерних классах, если потребуется.

class Animals:
    """Общий класс всех животных"""
    animalCount = 0  # количество всех животных
    animalWeight = 0  # общий вес всех животных

    # dicStats = {
    #     'animalCount': 0,
    #     'animalWeight': 0
    # }

    def __init__(self, name, weight, vid, voice):
        """Инициализация экземпляра класса с атрибутами: имя, вес, вид животного, его голос"""
        self.name = str(name).title()
        self.weight = weight
        self.vid = str(vid).title()
        self.voice = voice
        Animals.animalCount += 1  # с каждым новым экземпляром увеличиваем общее кол-во животных
        Animals.animalWeight += weight  # c каждым новым экземпляром увеличиваем общий вес всех животных
        # Animals.dicStats['animalCount'] = Animals.animalCount
        # Animals.dicStats['animalWeight'] = Animals.animalWeight

    def feed(self):  # общий метод: кормить животных
        print(f"Животное вида '{self.vid}' с именем '{self.name}' накормлено и напоено.")

    def voices(self):  # общий метод узнавания животных по их голосам
        v = input("Узнать животное по его голосу (кря, му, бее) - введите звучание из предложенного списка: >> ")
        if v == self.voice:
            print(f"По голосу это животное относится к виду '{self.vid}'")
        else:
            print("По данному звучанию сложно определить вид животного.")


class Birds(Animals):
    """Класс птиц (наследование от общего класса животных)"""
    birdsCount = 0

    def eggs(self):  # метод для птиц: сбор яиц
        pass


class Mammals(Animals):
    """Класс млекопитающих (наследование от общего класса животных"""
    mammalsCount = 0

    def milk(self):  # метод для млекопитающих: доение
        pass

    def shearing(self):  # метод для млекопитающих: стрижка
        pass


anim1 = Animals('Серый', 6, 'гусь', 'кря')
anim2 = Animals('Манька', 643, 'корова', 'му')

anim2.feed()
print(f"{anim2.vid} с именем '{anim2.name}' весит {anim2.weight} кг.")

anim1.voice()
