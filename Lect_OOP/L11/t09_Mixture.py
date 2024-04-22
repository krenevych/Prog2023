from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):  # metaclass=ABCMeta -  означає, що Pet може бути абстрактним класом
    def __init__(self, name, limbs, fleas):
        self.name = name
        self.limbs = limbs
        self.fleas = fleas

    @abstractmethod
    def voice(self):
        pass

class Cat(Pet):
    def __init__(self, name, flies):
        super().__init__(name, 4, flies)

    def voice(self):
        print("Міу-міу")

class Dog(Pet):
    def __init__(self, name, flies):
        super().__init__(name, 4, flies)

    def voice(self):
        print("I'm just a dog: Bau-Bau!")

class Logged:
    def log(self):
        print("========= Клас:", self.__class__.__name__)
        print("Кличка тварини:", self.name)
        print("Кількість лап: ", self.limbs)
        print("Кількість бліх:", self.fleas)


class LoggedDog(Dog, Logged):
    pass

class LoggedCat(Cat, Logged):
    pass


if __name__ == '__main__':
    cat = LoggedCat("Кузя", 0)
    dog = LoggedDog("Бобік", 5)

    cat.log()