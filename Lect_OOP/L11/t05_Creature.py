class Creature:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attend_party(self):
        self.health -= 10
        if self.health < 0:
            self.health = 0