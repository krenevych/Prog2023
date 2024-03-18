class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.lastName = last_name
        self.age = age
    def __str__(self):
        return f'name: {self.name}, lastName: {self.lastName}, age: {self.age}'

p = Person("Volodymyr", "Avakumov", 18)
print(p)
