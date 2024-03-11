class Animal:
    def __init__(self, name):
        self.name = name

    def get_animal_type(self):
        return None

    def move(self):
        print(f'Тварина: "{self.get_animal_type()}" {self.name} рухається')


class Dog(Animal):
    def get_animal_type(self):
        return "Dog"

class Cat(Animal):
    def get_animal_type(self):
        return "Cat"

class Lizard(Animal):
    pass

if __name__ == '__main__':
    # animal = Animal('Violetta')
    # animal.move()

    dog = Dog('Romeo')
    dog.move()

    cat = Cat('Vasya')
    cat.move()

    liz = Lizard('Gosha')
    liz.move()



