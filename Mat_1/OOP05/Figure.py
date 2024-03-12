class Figure:

    def __init__(self):
        self._position = (0, 0)
        self._color = "black"

    def translate(self, dx, dy):
        self._position = (self._position[0] + dx,
                          self._position[1] + dy)

    def set_position(self, x, y):
        self._position = (x, y)

    def set_color(self, color):
        self._color = color

    def calc_absolute_position(self, vertex):
        x = self._position[0] + vertex[0]
        y = self._position[1] + vertex[1]
        return x, y

    def draw(self):
        pass


