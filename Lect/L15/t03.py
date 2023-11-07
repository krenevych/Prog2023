ordinary_set = {1, 2, 3, 4}
frozen_set = frozenset({4, 5, 6})

print(ordinary_set)
print(frozen_set)

new_set = ordinary_set | frozen_set
print(new_set)
new_set2 = frozen_set | ordinary_set
print(new_set2)
unfrozen_set = set(frozen_set)
print(unfrozen_set)


