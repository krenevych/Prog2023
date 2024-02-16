from FigureReader import FigureReader

if __name__ == '__main__':
    reader = FigureReader("input.txt")
    figures = reader.read()
    for figure in figures:
        # print(figure.area())
        print(figure,", Arrea = ", figure.area())

    pass
