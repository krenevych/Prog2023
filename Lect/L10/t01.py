s = "Hello world"
#    012345678910

# print(s)

# for ch in s:
#     print(ch)

for i in range(len(s)):
    print(i, ":", s[i])

# s[3] = "L" # недопустима бо рядок належить
             # до незмінюваних (immutable)
             # тобто рядок це кортеж, символів

s1 = s * 3
print(s1)

p1 = "Hello"
p2 = 'World'
p3 = p1 + ", " + p2 + "!"
print(p3)

p_with_apostrophe = "В'ячеслав"
print(p_with_apostrophe)
p_with_quotes = 'Hotel "California"'
print(p_with_quotes)

single_line_string = ("RSA (абревіатура від прізвищ Rivest, Shamir та Adleman) "
                     "— криптографічний алгоритм з відкритим ключем, що "
                     "базується на обчислювальній складності задачі факторизації "
                     "великих цілих чисел.")
print(single_line_string)

multi_line_string = '''RSA (абревіатура від прізвищ Rivest, Shamir та Adleman) 
— криптографічний алгоритм з відкритим ключем,
 що базується на обчислювальній складності задачі 
 факторизації великих цілих чисел.
'''
print(multi_line_string)
