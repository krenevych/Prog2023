from QuadraticEquation import QuadraticEquation


class EqReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        equations = []
        with open(self.file_name) as f:
            for line in f:
                # print(line)
                a, b, c = [float(el) for el in line.split()]
                eq = QuadraticEquation(a, b, c)
                equations.append(eq)
        return equations
