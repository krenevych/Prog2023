from t06 import Complex

z1 = Complex(1, 2)
z1 += 3 # z1 = z1 + 3
print(z1)
z1 += complex(3 + 4j)
print(z1)
z1 += Complex(1, 1)
print(z1)