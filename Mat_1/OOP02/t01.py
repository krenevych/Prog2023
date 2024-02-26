class Auto:

    def __init__(self, mark, color, speed):
        self.mark = mark
        self.color = color
        self.speed = speed

    def go(self):
        print(f"{self.mark}: go... ")

    def showColor(self):
        print(f"Color = {self.color}")

if __name__ == '__main__':
    mercedes = Auto("Mercedes", "White", 250)
    mazda = Auto("Mazda", "Grey", 200)
    print(mercedes.mark)
    print(mazda.mark)
    mercedes.go()
    mazda.go()
    mazda.showColor()


