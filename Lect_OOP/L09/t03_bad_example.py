from math import factorial

N = int(input("Enter N: "))
x = float(input("Enter x: "))

a = x**N / factorial(N)
print(x**N)
print(factorial(N))

print(a)

# Enter N: 20
# Enter x: 20
# 43099804.12182177

# Enter N: 20
# Enter x: 20
# 43099804.12182178
# /////////////////////

# Enter N: 30
# Enter x: 30
# 776207020879.7281

# Enter N: 30
# Enter x: 30
# 776207020879.7279

#######
# Enter N: 30
# Enter x: 1
# 3.7699876288159054e-33

# Enter N: 30
# Enter x: 1
# 3.769987628815905e-33

