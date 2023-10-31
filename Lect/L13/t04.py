# sin
# 0     - 0
# pi/6  - 0.5
# pi/4  - корінь з двох на два
# pi/3  - корінь з трох на два
# pi/2  - 1



def table(points, f):
    for x in points:
        print(f"{x:6.2f} - {f(x)}")

# pts = [math.pi / i for i in range(11)]
# pts = [math.pi / 2 * i / 4 for i in range(5)]
from math import pi, sin, cos, tan
pts = [0, pi/6, pi/4, pi/3, pi/2]
table(pts, tan)


