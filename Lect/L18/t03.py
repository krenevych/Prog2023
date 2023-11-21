
try:
    lst = [1, 2, 3]
    print(lst[5])
    # d = {"first": 1, "second": 2}
    # print(d["third"])
# except IndexError:
#     print("Помилка ключа або індексу")
# except KeyError:
#     print("Помилка ключа або індексу")
except LookupError:
    print("Помилка ключа або індексу")
# except BaseException :  ===== except: НЕ МОЖНА, БО РУКИ ВІДІБ'Є КЕРІВНИК ПРОЕКТУ!
#     print("Помилка ключа або індексу")

