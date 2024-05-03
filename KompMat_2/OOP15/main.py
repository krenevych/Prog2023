from KompMat_2.OOP15.FileReader import FileReaderLineObserver, FileReader


class ShowLines(FileReaderLineObserver):
    def onReceive(self, line):
        print(line)

    def onReadFinish(self):
        print("file read finish!!!")

class WordCounter(FileReaderLineObserver):
    def __init__(self):
        self.counter = 0

    def onReceive(self, line: str):
        words = line.split()
        self.counter += len(words)

    def onReadFinish(self):
        print(f"Кількість слів у файлі {self.counter}")


if __name__ == '__main__':
    file_reader = FileReader("input.txt")
    # showLines = ShowLines()
    # file_reader.subscribe(showLines)

    file_reader.subscribe(WordCounter())

    # wc = WordCounter()
    # file_reader.subscribe(wc)

    file_reader.read()
    # print(wc.counter)