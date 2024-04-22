class Pet:
    def __init__(self, name):
        self.name = name

    def voice(self):
        print("Я базовий клас, я не знаю що сказати :)")

class Cat(Pet):

    def voice(self):
        print("Міу-міу")

class Dog(Pet):
    def voice(self):
        print("Бау-бау")


if __name__ == '__main__':
    cat = Cat("Кузя")
    dog = Dog("Бобік")

    cat.voice()
    dog.voice()

    pet = Pet("Хто-зна-що")  # Повинно бути заборонено!!!
    pet.voice()