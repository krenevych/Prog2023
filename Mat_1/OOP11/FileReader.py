from abc import ABCMeta, abstractmethod

# абстрактний клас, навіть інтерфейс
class FileReaderObserver(metaclass=ABCMeta):
    @abstractmethod
    def onReceive(self, line):
        pass

class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.observers = [] # список спостерігачів - всі вони будуть отримувати прочитаний рядок з файлу.

    def subscribe(self, observer): # підписування на отримання рядків з файлу
        self.observers.append(observer)

    def read(self):
        with open(self.file_name) as f:
            for line in f:
                for observer in self.observers:
                    observer.onReceive(line.rstrip()) # відправка прочитаного рядока кожному зі спостерігачів


if __name__ == '__main__':
    fr = FileReader("input.txt")
    fr.read()