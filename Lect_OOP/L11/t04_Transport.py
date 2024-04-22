class Transport:
    def __init__(self):
        self.current_mileage = 0
        self.resource = 100_000 # раз на 100_000 треба робити капітальний ремонт

    def driving(self):
        self.current_mileage += 10_000

