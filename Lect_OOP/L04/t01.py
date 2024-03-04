class Wheel:

    def inflated(self):
        print("Inflated")
        return True


class Engine:
    def run(self):
        print("Enigine runs...")

class Driver:
    def __init__(self, name):
        self._name = name

    def drive(self):
        print(f"Driver {self._name} is driving")

class Car:
    def __init__(self, wheel):
        self._engine = Engine()  # композиція
        self._wheel = wheel  # агрегація

    def drive(self, driver: Driver):  # проста залежність класу Car від класу Driver
        if self._wheel.inflated():
            self._engine.run()
            driver.drive()




if __name__ == '__main__':
    wheel = Wheel()
    car = Car(wheel)

    driver = Driver("Valyera")
    car.drive(driver)

















    # car.set_driver(driver)

