# Слова у рядку розділяються одним або декількома пропусками.
# Визначити кількість входжень кожного слова до рядка.
s = "hello   world  hello hello   hello    hello world forever "
# s = input()
words = s.split()
d_words = {
    word: words.count(word) for word in words
}
# print(d_words)
for word, count in d_words.items():
    print(f"Our sentence contains word '{word}' {count} times")
