# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с
# животными и дополнить их в дочерних классах, если потребуется.
class Animals:
    """Общий класс всех животных - базовый класс"""
    animalCount = 0  # количество всех животных
    animalWeight = 0  # общий вес всех животных
    animalsList = []  # список всех животных на ферме

    @staticmethod
    def stats():
        print(f"Всего на ферме {Animals.animalCount} животных.")
        print(f"Общий вес всех животных на ферме составляет: {Animals.animalWeight} кг.")

    @staticmethod
    def maxWeight():
        maxW = max(Animals.animalsList, key=lambda x: x[1])  # Находим животное с максимальным весом
        print(f"Животное с максимальным весом: {maxW[2]} по имени '{maxW[0]}' и весом {maxW[1]} кг.")

    @staticmethod
    def minWeight():
        minW = min(Animals.animalsList, key=lambda x: x[1])  # Находим животное с минимальным весом
        print(f"Животное с минимальным весом: {minW[2]} по имени '{minW[0]}' и весом {minW[1]} кг.")

    def __init__(self, name, weight, vid, voice):
        """Инициализация экземпляра класса с атрибутами: имя, вес, вид и голос животного"""
        self.name = str(name).title()
        self.weight = weight
        self.vid = str(vid).upper()
        self.voice = voice
        Animals.animalCount += 1  # с каждым новым экземпляром увеличиваем общее кол-во животных
        Animals.animalWeight += weight  # c каждым новым экземпляром увеличиваем общий вес всех животных
        Animals.animalsList.append([self.name, self.weight, self.vid, self.voice])

    def feed(self):  # общий метод: кормить животных
        print(
            f"Живое существо вида '{self.vid}' с именем '{self.name}' накормлено, напоено и в благодарность сказало '{self.voice}'.")


class Birds(Animals):
    """Класс для птиц (наследование от общего класса Animals)"""

    def eggs(self):  # метод для птиц: сбор яиц
        print(f"'{self.vid}' с именем '{self.name}' снесла яйца. Их мы и собрали.")


class Geese(Birds):
    """Расширение классов птиц - гуси"""

    def voices(self):
        print(f"У гуся голос вот такой: {getattr(bird4, 'voice')}")


class Ducks(Birds):
    """Расширение классов птиц - утки"""

    def voices(self):
        print(f"У утки голос вот такой: {getattr(bird3, 'voice')}")


class Mammals(Animals):
    """Класс млекопитающих (наследование от общего класса животных"""

    def milk(self):  # метод для млекопитающих: доение
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' подоено.")

    def shearing(self):  # метод для млекопитающих: стрижка
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' подстрижено.")


class Cows(Mammals):
    """Расширение классов млекопитающих - коровы и быки"""

    def voices(self):
        print(f"У коровы голос вот такой: {getattr(mlk1, 'voice')}")


class Sheeps(Mammals):
    """Расширение классов млекопитающих - овцы и бараны"""

    def voices(self):
        print(f"У овцы и барана голос вот такой: {getattr(mlk2, 'voice')}")


class Goats(Mammals):
    """Расширение классов млекопитающих - козы"""

    def voices(self):
        print(f"У коз голос вот такой: {getattr(mlk4, 'voice')}")


bird1 = Birds('ко-ко', 3, 'курица', 'ко-ко-ко')
bird2 = Birds('кукареку', 4, 'петух', 'ку-ка-ре-ку')
bird3 = Birds('кряква', 5, 'утка', 'кря-кря')
bird4 = Birds('серый', 6, 'гусь', 'га-га-га')
bird5 = Birds('белый', 7, 'гусь', 'га-га-га')
mlk1 = Mammals('манька', 643, 'корова', 'му-у-у')
mlk2 = Mammals('барашек', 23, 'баран', 'бе-е-е')
mlk3 = Mammals('кудрявая', 25, 'овца', 'бе-е-е')
mlk4 = Mammals('рога', 24, 'коза', 'ме-е-е')
mlk5 = Mammals('копыта', 27, 'коза', 'ме-е-е')


def main():
    """Пользовательский выбор"""
    print("*** ФЕРМА ДЯДЮШКИ ДЖО *** \n")
    select_input = input(
        "Если хотите покормить животных, нажмите клавишу 1; Если хотите подстричь животных, нажмите клавишу 2; Если "
        "хотите собрать яйца у птиц, нажмите клавишу 3; Если хотите подоить животных, нажмите клавишу 4; Если хотите "
        "узнать, какое животное на ферме имеем максимальный вес, нажмите клавишу 5, а какое минимальный вес - 6; Если"
        " хотите узнать общую статистику по ферме, нажмите клавишу 7; Для выхода нажмите любую иную клавишу. >>> \n")
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
    elif select_input == '5':
        Animals.maxWeight()
    elif select_input == '6':
        Animals.minWeight()
    elif select_input == '7':
        Animals.stats()
    elif select_input == '8':
        Geese.voices('0')
        # pass
    else:
        print("Программа завершена. До свидания.")


main()
# print(Animals.animalsList[3][-1])
