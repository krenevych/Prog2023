class Copier:
    def copy(self):
        print("Copier is coping")

class Xerox(Copier):
    pass

class Scanner:
    def copy(self):
        print("Scanner is coping")

    def send(self):
        print("Scanner is sending file via email")


class MFD(Xerox, Scanner):
    pass

mfd = MFD()
mfd.copy()
mfd.send()

print(MFD.__mro__)