from ProtectedDictIntIterator import ProtectedDictIntIterator
class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}  # клас ProtectedDictInt - є обготкою над вбудованим словником

    def __setitem__(self, key, value):
        assert type(key) == int, "за умовою ключ має бути цілий"
        assert key not in self, "за умовою задачі значення, що відповідає ключу, що є в словнику змінювати вже не можна"
        self.__dict[key] = value

    def __getitem__(self, item):
        return self.__dict[item]

    def __str__(self):
        # return str(self.__dict)
        return f"ProtectedDictInt: {self.__dict}"

    def __contains__(self, item):
        return item in self.__dict

    def __len__(self):
        return len(self.__dict)

    def __add__(self, other):
        new_dict = ProtectedDictInt()
        for k, v in self.__dict.items():
            new_dict[k] = v

        if type(other) == tuple or type(other) == list: #    кортеж/список
            assert len(other) % 2 == 0
            for i in range(0, len(other), 2):
                new_dict[other[i]] = other[i+1]

        return new_dict

    def __delitem__(self, key):
        del self.__dict[key]

    def __sub__(self, other):
        new_dict = ProtectedDictInt()
        for k, v in self.__dict.items():
            if other != k:
                new_dict[k] = v

        return new_dict

    def __iter__(self):
        return ProtectedDictIntIterator(self)

    def keys(self):
        return self.__dict.keys()


if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = "hello"
    d[234] = "hello_234"
    d[54] = "34"

    for el in d:
        print(el)


