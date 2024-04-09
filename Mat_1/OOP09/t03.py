N = 4

#      f
#          g
#          D
#  5   19  65 211

f = 5
g = 19
for n in range(3, N+1):
    # D = 5 * g - 6 * f
    # f = g
    # g = D
    g, f = 5 * g - 6 * f, g

    print(g)