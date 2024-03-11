class BaseCar:
    def __init__(self):
        self.make = 'Volvo'
        self.model = "CX-90"
        self.wheel = "18"
        self.engine = "245"

    def describe_car(self):
        print("Car:", self.make, self.model, self.wheel, self.engine)

class LuxuryCar(BaseCar):

    def __init__(self):
        super().__init__()
        self.audio = "JBL"
        self.seats = "Lather"
        self.color = "Crimson"

    def describe_car(self):
        print("Car:", self.make, self.model, self.wheel)
        print("Luxury:", self.audio, self.seats, self.color)

if __name__ == '__main__':
    # car = BaseCar()
    # car.describe_car()

    luxury_car = LuxuryCar()
    luxury_car.describe_car()



