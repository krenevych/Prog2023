# Слова у рядку розділяються одним або декількома пропусками.
# Визначити кількість входжень кожного слова до рядка.
s = "hello   world  hello hello   hello    hello world forever "
# використаємо словник, ключами будуть окремі слова, а значеннями - кількість входжень
words = s.split()
print(words)
d_words = dict(dict.fromkeys(words, 0))
print(d_words)
for word in words:
    d_words[word] += 1
print(d_words)

for word, count in d_words.items():
    print(f"Our sentence contains word '{word}' {count} times")
