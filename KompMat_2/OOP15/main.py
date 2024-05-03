from KompMat_2.OOP15.FileReader import FileReaderLineObserver, FileReader


class ShowLines(FileReaderLineObserver):
    def onReceive(self, line):
        print(line)


if __name__ == '__main__':
    file_reader = FileReader("input.txt")
    showLines = ShowLines()
    file_reader.subscribe(showLines)

    file_reader.read()