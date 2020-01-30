from pprint import pprint


class Car:
    # color = 'black'  # цвет автомобиля
    number_plate = 'x001y77ru'  # гос.номер
    speed = 0  # km/h скорость движения
    fuel = 0  # l вместимость топлива
    state = 'stopped'  # состояние авто - стоит на месте
    position = 0

    def __init__(self, color='black'):
        self.color = color

    def start(self):
        self.state = 'started'

    def fill(self, fuel):
        if fuel < 0:
            print("Go away, thief")
        self.fuel += fuel

    def accelerate(self, value):
        self.speed += value

    def drive(self, hours):
        self.position = self.speed * hours
        self.fuel -= 10 * hours

    def stop(self):
        self.state = 'stopped'


class Cabrio(Car):
    roof_state = 'folded'

    def fold_roof(self):
        self.roof_state = 'folded'

    def open_roof(self):
        self.roof_state = 'opened'


cabrio0 = Cabrio()
print(cabrio0.color)
cabrio0.open_roof()
print(cabrio0.roof_state)

# car0 = Car()
# car1 = Car('red')
# print(car0.color)
# print(car1.color)
