from abc import ABCMeta, abstractmethod


class FileReaderLineObserver(metaclass=ABCMeta):
    @abstractmethod
    def onReceive(self, line):
        pass

    @abstractmethod
    def onReadFinish(self):
        pass


class FileReader:
    def __init__(self, fileName):
        self.fileName = fileName
        self.observers = []

    def subscribe(self, observer: FileReaderLineObserver):
        self.observers.append(observer)

    def read(self):
        with open(self.fileName) as f:
            for line in f:
                # print(line.rstrip())
                line_cut = line.rstrip()
                for observer in self.observers:
                    observer.onReceive(line_cut)

        for observer in self.observers:
            observer.onReadFinish()


