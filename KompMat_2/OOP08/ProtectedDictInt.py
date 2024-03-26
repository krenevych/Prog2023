class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}

    def __setitem__(self, key, value):
        assert type(key) == int, "Ключі мають бути цілими"
        # assert key not in self.__dict, "Заборонена операція зміни значення за ключем"
        assert key not in self, "Заборонена операція зміни значення за ключем"
        self.__dict[key] = value

    def __getitem__(self, item):
        return self.__dict[item]

    def __contains__(self, item):
        return item in self.__dict

    def __str__(self):
        return f"ProtectedDictInt: {self.__dict}"

    def __len__(self):
        return len(self.__dict)

    def __delitem__(self, key):
        del self.__dict[key]

if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = "Hello"
    # d[23] = "Hello"
    print(d)
    print(d[23])
    print(23 in d)
    print(2323 in d)
    print(len(d))

    d2 = ProtectedDictInt()
    d2[45] = "333"

    print("d2 = ", d2)
    del d2[45]  # magic method __delitem__
    print("d2 = ", d2)
    # TODO: implement corresponding magic methods
    # d3 = d + d2
    # d4 = d3 + (234, "123")
    # d5 = d4 - 23
