
try:
    lst = [1, 2, 3]
    print(lst[5])
    # d = {"first": 1, "second": 2}
    # print(d["third"])

except LookupError as error: # змінна error містить всю детальну інформацію про виключну ситуацію, що сталася
    print("Помилка ключа або індексу:")
    if type(error) == IndexError:
        print("IndexError error")
    elif type(error) == KeyError:
        print("KeyError")

