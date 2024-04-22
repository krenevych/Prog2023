from abc import ABC

from Lect_OOP.L11.t03_Diagnosable import Diagnosable
from Lect_OOP.L11.t04_Transport import Transport
from Lect_OOP.L11.t05_Creature import Creature


class Car(Transport, Diagnosable): # клас Автомобіль є нащадком класу Транспорт та реалізовує інтерфейс Дігностований

    def diagnose(self):
        proc = (1 - self.current_mileage / self.resource) * 100
        if proc <= 0:
            print("Ресурс вичерпано, терміново прямуйте на капітальний ремонт")
        else:
            print(f"Лишилося {proc}% ресурсу")


if __name__ == '__main__':
    car = Car()
    for i in range(10):
        car.driving()
    car.diagnose()
