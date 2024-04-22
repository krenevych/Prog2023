from abc import ABCMeta, abstractmethod


class Diagnosable(metaclass=ABCMeta):  # Інтерфейс Діагностований

    @abstractmethod
    def diagnose(self):
        pass