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


class Mammals(Animals):
    """Класс млекопитающих (наследование от общего класса животных"""

    def milk(self):  # метод для млекопитающих: доение
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' подоено.")

    def shearing(self):  # метод для млекопитающих: стрижка
        print(f"Живое существо вида '{self.vid}' с именем '{self.name}' подстрижено.")


bird1 = Birds('ко-ко', 3, 'курица', 'ко-ко-ко')
ko = bird1.voice
bird2 = Birds('кукареку', 4, 'петух', 'ку-ка-ре-ку')
ku = bird2.voice
bird3 = Birds('кряква', 5, 'утка', 'кря-кря')
u = bird3.voice
bird4 = Birds('серый', 6, 'гусь', 'га-га-га')
g = bird4.voice
bird5 = Birds('белый', 7, 'гусь', 'га-га-га')
mlk1 = Mammals('манька', 643, 'корова', 'му-у-у')
m = mlk1.voice
mlk2 = Mammals('барашек', 23, 'баран', 'бе-е-е')
ob = mlk2.voice
mlk3 = Mammals('кудрявая', 25, 'овца', 'бе-е-е')
mlk4 = Mammals('рога', 24, 'коза', 'ме-е-е')
kz = mlk4.voice
mlk5 = Mammals('копыта', 27, 'коза', 'ме-е-е')


def main():
    """Пользовательский выбор"""
    print("*** ФЕРМА ДЯДЮШКИ ДЖО *** \n")
    select_input = input(
        "Если хотите покормить животных, нажмите клавишу 1; Если хотите подстричь животных, нажмите клавишу 2; Если "
        "хотите собрать яйца у птиц, нажмите клавишу 3; Если хотите подоить животных, нажмите клавишу 4; Если хотите "
        "узнать, какое животное на ферме имеем максимальный вес, нажмите клавишу 5, а какое минимальный вес - 6; Если"
        " хотите узнать общую статистику по ферме, нажмите клавишу 7; Если хотите услышать голоса животных, нажмите"
        " клавишу 8; Для выхода нажмите любую иную клавишу. >>> \n")
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
        print(f"У гуся голос такой: {g}")
        print(f"У курицы голос такой: {ko}")
        print(f"У петуха голос такой: {ku}")
        print(f"У утки голос такой: {u}")
        print(f"У коровы голос такой: {m}")
        print(f"У барана и овцы голос такой: {ob}")
        print(f"У коз голос такой: {kz}")
    else:
        print("Программа завершена. До свидания.")


main()