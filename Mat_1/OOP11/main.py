from Mat_1.OOP11.FileReader import FileReader, FileReaderObserver


class ShowLines(FileReaderObserver):
    def onReceive(self, line):
        print(line)

class WordCounter(FileReaderObserver):
    def __init__(self):
        self.counter = 0

    def onReceive(self, line: str):
        words = line.split()
        self.counter += len(words)

    def __str__(self):
        return f"WordCounter: count = {self.counter}"

class WordContains(FileReaderObserver):
    def __init__(self, word):
        self.exist = False
        self.word = word

    def onReceive(self, line: str):
        words = line.split()
        if self.word in words:
            self.exist = True


    def __str__(self):
        return f"WordContains: File contains {self.word} = {self.exist}"


if __name__ == '__main__':
    showLines = ShowLines()
    wordCounter = WordCounter()
    wordContains = WordContains("Навчати")
    fr = FileReader("input.txt")
    fr.subscribe(showLines)
    fr.subscribe(wordCounter)
    fr.subscribe(wordContains)
    fr.read()

    print(wordCounter)
    print(wordContains)