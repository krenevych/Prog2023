class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def growUp(self):
        self.age += 1
        age = 100
        age += 1

    def bite(self, other):
        print(f"Cat {self.name} bites {other.name}")

    def miu(self):
        print(f"Cat '{self.name}' says: Miu")


catVasya = Cat('Vasya')
catKuzia = Cat('Kuzia')
catInokentiy = Cat('Inikentiy')

print(catKuzia.age)
catKuzia.growUp()
catKuzia.growUp()
catKuzia.growUp()
print(catKuzia.age)

# catVasya.miu()
# catVasya.miu()
# catVasya.miu()
# catKuzia.miu()
# catKuzia.miu()
# catKuzia.miu()

# print(catVasya.name)
# print(catKuzia.name)
catVasya.bite(catKuzia)




