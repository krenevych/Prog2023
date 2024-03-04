class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print(f'Тварина {self.name} рухається')

class Dog(Animal):
    def speak(self):
        print(f"Собака {self.name} гавкає...")

    def move(self):
        print(f'Собака {self.name} бігає')


class Cat(Animal):
    def speak(self):
        print(f"Кіт {self.name} нявкає...")

    def move(self):
        print(f'Кіт {self.name} лазить по столу')

class Lizard(Animal):
    def speak(self):
        print(f"Ящірка {self.name} шипить...")

    def move(self):
        print(f'Ящірка {self.name} плазує')



if __name__ == '__main__':
    animal = Animal('Violetta')
    animal.move()

    dog = Dog("Барбос")
    dog.move()
    dog.speak()

    cat = Cat("Васька")
    cat.speak()
    cat.move()

    lizard = Lizard("Артемій")
    lizard.move()
    lizard.speak()

