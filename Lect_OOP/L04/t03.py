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
        self._drivers = []  # список водіїв, які можуть керувати даним автомобілем

    def add_driver(self, driver):
        self._drivers.append(driver)

    def drive(self, driver_number):  # проста залежність класу Car від класу Driver
        if self._wheel.inflated() and driver_number < len(self._drivers):
            self._engine.run()
            driver = self._drivers[driver_number]
            driver.drive()



if __name__ == '__main__':
    wheel = Wheel()
    car = Car(wheel)

    driver = Driver("Valyera")
    driver1 = Driver("Anatoliy")

    car.add_driver(driver)  # посадили Валєру у автомобіль
    car.add_driver(driver1)  # посадили Анатолія у автомобіль
    car.drive(1)


















    # car.set_driver(driver)

