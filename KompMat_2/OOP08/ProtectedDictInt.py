class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}

    def __setitem__(self, key, value):
        assert type(key) == int, "Ключі мають бути цілими"
        assert key not in self.__dict, "Заборонена операція зміни значення за ключем"
        self.__dict[key] = value


if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = "Hello"
    print(d)
