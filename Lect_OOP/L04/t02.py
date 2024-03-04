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
        self._car = None

    def drive(self):
        print(f"Driver {self._name} is driving")

    def drive_car(self):
        if self._car is not None:
            car.drive()

    def fill_tank(self):
        print(f"Driver {self._name} is filling tank")

    def set_car(self, car):
        self._car = car

class Car:
    def __init__(self, wheel):
        self._engine = Engine()  # композиція
        self._wheel = wheel  # агрегація
        self._driver = None  # під час створення автомобіля водія туди не додають, але передбачають, що потім його можна туди посадити

    def set_driver(self, driver):
        self._driver = driver

    def drive(self):  # проста залежність класу Car від класу Driver
        if self._wheel.inflated() and self._driver is not None:
            self._engine.run()
            driver.drive()

    def fill_fuel(self):
        if self._driver is not None:
            self._driver.fill_tank()




if __name__ == '__main__':
    wheel = Wheel()
    car = Car(wheel)

    driver = Driver("Valyera")
    driver.set_car(car)

    car.set_driver(driver)  # посадили Валєру у автомобіль - тобто зберегли в об'єкті Car посилання на об'єкт Driver
    car.fill_fuel()
    # car.drive()

    driver.drive_car()

















    # car.set_driver(driver)

