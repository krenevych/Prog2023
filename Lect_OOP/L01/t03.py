class CastomClass:
    def __init__(self, par1):
        self.par2 = None
        self.par1 = par1

    def mymethod(self):
        self.par2 = 10

instance = CastomClass(10)
print(instance.par1)
# instance.mymethod()
print(instance.par2)