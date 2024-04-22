from abc import ABC

from Lect_OOP.L11.t03_Diagnosable import Diagnosable
from Lect_OOP.L11.t05_Creature import Creature


class Human(Creature, Diagnosable): # клас Людина є нащадком класу Створіння та реалізовує інтерфейс Дігностований

    def diagnose(self):
        if self.health <= 0:
            print("Треба терміново зайнятися здоров'ям!")
        else:
            print(f"{self.name}, Health = {self.health}")


if __name__ == '__main__':
    human = Human("Anatolii")
    for i in range(10):
        human.attend_party()
        
    human.diagnose()
