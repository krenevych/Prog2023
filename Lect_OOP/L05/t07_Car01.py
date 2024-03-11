class BaseModel:
    def __init__(self):
        self.make = 'Volvo'
        self.model = "CX-90"
        self.wheel = "18"
        self.engine = "245"

    def describe_car(self):
        print("Car:", self.make, self.model, self.wheel, self.engine)

class LuxuryCar(BaseModel):

    def __init__(self):
        BaseModel.__init__(self)
        self.audio = "JBL"
        self.seats = "Lather"
        self.color = "Crimson"

    def describe_car(self):
        # super().describe_car()
        BaseModel.describe_car(self)
        print("Luxury:", self.audio, self.seats, self.color)

if __name__ == '__main__':
    # car = BaseCar()
    # car.describe_car()

    luxury_car = LuxuryCar()
    luxury_car.describe_car()



