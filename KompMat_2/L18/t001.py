a = input()
try:
    # a = int(input())

    a = int(a)
except ValueError:
    print(f"'{a}' не є цілим, тому його не вдалося конвертувати")

# try:
#     # відкриваємо файл
# except FileNotFoundError:
