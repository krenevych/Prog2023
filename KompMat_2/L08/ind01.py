counter = 0
# for i in range(100, 1000):
#     od = i % 10
#     de = (i // 10) % 10
#     so = i // 100
for so in range(1, 10):
    for de in range(10):
        for od in range(10):
            suma = od + de + so
            od = suma % 10
            de = suma // 10
            if od == 7 or de == 7:
                counter += 1

print(counter)
