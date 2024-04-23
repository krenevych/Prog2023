from Mat_1.OOP11.FileReader import FileReader, FileReaderObserver


class ShowLines(FileReaderObserver):
    def onReceive(self, line):
        print(line)


if __name__ == '__main__':
    showLines = ShowLines()
    fr = FileReader("input.txt")
    fr.subscribe(showLines)
    fr.read()