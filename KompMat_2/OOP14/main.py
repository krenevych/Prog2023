from KompMat_2.OOP14.MilitaryObject import GeneralStaff, MilitaryBase
from KompMat_2.OOP14.Spy import Spy


class SecretAgent(Spy):
    def __init__(self, name):
        super().__init__(name)
        self.pen_drive = ""

    def visit_general_staff(self, staff : GeneralStaff):
        self.pen_drive = f"GeneralStaff: У генеральному штабі є {staff.generals} геренералів та {staff.secretPaper} секретних паперів."

    def visit_military_base(self, base: MilitaryBase):
        self.pen_drive = f"MilitaryBase: На військовій базі є {base.officers} офіцерів, {base.soldiers} солдатів, {base.jeeps} джипів та {base.tanks} танків."

    def give_info(self):
        print(f"Agent='{self.name}': info = '{self.pen_drive}'")


class Saboteur(Spy):

    def visit_general_staff(self, staff : GeneralStaff):
        print(f"Привіт від {self.name}!!!")
        staff.generals = 0
        staff.secretPaper = 0

    def visit_military_base(self, base: MilitaryBase):
        print(f"Привіт від {self.name}!!!")
        base.jeeps -= 2
        base.tanks -= 1
        base.officers -= 3
        base.soldiers -= 10


if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100, "Kremlin")
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20, "BNR")
    print(militaryBase)

    james = SecretAgent("James Bond")
    kirya = Saboteur("Kyrylo Budanov")

    generalStaff.accept(james)
    james.give_info()

    militaryBase.accept(james)
    james.give_info()

    generalStaff.accept(kirya)
    militaryBase.accept(kirya)

    generalStaff.accept(james)
    james.give_info()

    militaryBase.accept(james)
    james.give_info()
