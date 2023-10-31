def table(points, f):
    for x in points:
        print(f"{x:6.2f} - {f(x)}")

# def square(x):
#     return x ** 2
# table([0, 1, 2, 3, 4, 5], square)


table([0, 1, 2, 3, 4, 5], lambda x: x ** 2)
# square = lambda x: x ** 2
# table([0, 1, 2, 3, 4, 5], square)
