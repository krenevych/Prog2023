from abc import ABCMeta, abstractmethod

from KompMat_2.OOP14.Spy import Spy


class MilitaryObject(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def accept(self, spy: Spy):
        pass

class GeneralStaff(MilitaryObject):
    def __init__(self, generals, secretPaper, name):
        super().__init__(name)
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        return f"GeneralStaff: У генеральному штабі є {self.generals} геренералів та {self.secretPaper} секретних паперів."

    def accept(self, spy: Spy):
        spy.visit_general_staff(self)

class MilitaryBase(MilitaryObject):
    def __init__(self, officers, soldiers, jeeps, tanks, name):
        super().__init__(name)
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        return f"MilitaryBase: На військовій базі є {self.officers} офіцерів, {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."

    def accept(self, spy: Spy):
        spy.visit_military_base(self)

if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    print(militaryBase)




