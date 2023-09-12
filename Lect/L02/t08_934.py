a, b, c = [int(schos) for schos in input().split()]

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

ha = 2 * S / a  # висота опущена на сторону a
hb = 2 * S / b  # висота опущена на сторону b
hc = 2 * S / c  # висота опущена на сторону c

print(f"{ha:0.2f} {hb:0.2f} {hc:0.2f} ")
# print(ha, hb, hc)
