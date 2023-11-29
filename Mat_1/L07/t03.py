# Описати підпрограму, яка утворює текстовий файл
# із 9 рядків, у першому з яких одна літера '1',
# у другому – дві літери '2', ... , у дев’ятому – дев’ять літер '9'.

# 1
# 22
# 333
# 4444
def createDigitalTriangle(n):
    with open("out03.txt", "w") as f:
        for i in range(1, n+1):
            print(str(i) * i, file=f)

if __name__ == '__main__':
    createDigitalTriangle(4)