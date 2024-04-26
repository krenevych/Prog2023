from KompMat_2.OOP14.MilitaryObject import GeneralStaff, MilitaryBase
from KompMat_2.OOP14.Spy import Spy


class JamesBond(Spy):
    def __init__(self, name):
        super().__init__(name)

    def visit_general_staff(self, staff : GeneralStaff):
        print(self.name, staff.name)

    def visit_military_base(self, base: MilitaryBase):
        print(self.name, base.name)



if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100, "Kremlin")
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20, "BNR")
    print(militaryBase)

    james = JamesBond("James Bond")
    generalStaff.accept(james)
    militaryBase.accept(james)