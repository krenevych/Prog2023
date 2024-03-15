from math import sin, cos, radians
import turtle

class Figure:
    default_color = "DeepPink3"

    def __init__(self):
        self.color = Figure.default_color
        self.position = (0, 0)
        self.rotation = 0
        self.scale = (1, 1)

    def set_position(self, x, y):
        self.position = (x, y)

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_rotation_degree(self, degree):
        self.rotation = radians(degree)

    def rotationMatrix(self):
        fi = self.rotation
        fiMatrix = [
            [cos(fi), -sin(fi)],
            [sin(fi), cos(fi)]
        ]
        return fiMatrix

    @staticmethod
    def multMatrixVector(M, v):
        turnedVertex1 = [0, 0]
        turnedVertex1[0] = M[0][0] * v[0] + M[0][1] * v[1]
        turnedVertex1[1] = M[1][0] * v[0] + M[1][1] * v[1]
        return turnedVertex1

    @staticmethod
    def scaleVertex(vertex, scale):
        return (scale[0] * vertex[0],
                scale[1] * vertex[1])

    def calc_abs_pos(self, vertex):
        scaledVertex1 = Figure.scaleVertex(vertex, self.scale)
        M = self.rotationMatrix()
        turnedVertex1 = Figure.multMatrixVector(M, scaledVertex1)

        v1 = (self.position[0] + turnedVertex1[0],
              self.position[1] + turnedVertex1[1])
        return v1

    def draw(self):
        pass

