from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):  # metaclass=ABCMeta -  означає, що Pet може бути абстрактним класом
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def voice(self):
        pass

class Cat(Pet):
    # def __init__(self, name):  - створення конструктора у нашому випадку є зайвий код
    #     super().__init__(name)

    def voice(self):
        print("Міу-міу")

class Dog(Pet):
    def voice(self):
        print("I'm just a dog: Bau-Bau!")

class HunterDog(Dog):
    def voice(self):
        print("HunterDog: WHERE ARE FOXES!!!!!!!")


if __name__ == '__main__':
    cat = Cat("Кузя")
    cat.voice()

    dog = Dog("Бобік")
    dog.voice()

    hunterDog = HunterDog("Rex")
    hunterDog.voice()

    # pet = Pet("Hello") # не иможна створювати, бо Pet абстрактний і спроба створити викличе креш.
