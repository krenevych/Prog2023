# Визначити слово, яке входить до тексту найбільшу кількість разів.
s = "hello   world  hello hello   hello    hello world forever "
# s = input()
words = s.split()
d_words = {
    word: words.count(word) for word in words
}
max_word = ""
max_count = 0

for word, count in d_words.items():
    if max_count < count:
        max_word = word
        max_count = count

print(f"Слово {max_word} зустрічається найбільшу кількість разів {max_count}")
