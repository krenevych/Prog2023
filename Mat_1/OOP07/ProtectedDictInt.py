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



if __name__ == '__main__':
    d = ProtectedDictInt()
    # d = {}
    d[23] = "hello"
    d[234] = "hello_234"
    # d[23] = "32" # заборонена за умовою задачі, бо неможна змінювати
    # d["Hello"] = "world" # заборонена, бо ключами мають бути лише числа
    print(d)
    print("d[23]=", d[23])  # d.__getitem__(23)
    # d.show()
    print(23 in d)
    print(23223 in d)
    print(len(d))
    d2 = d + (34, 65, 77, "hello77") # 1 - додавання кортежу
    # d2 = d2 + {88: 34}   # 2 - додавання словника
    # d_tmp = ProtectedDictInt()
    # d_tmp[99] = 99
    # d2 = d + d_tmp # - додавання словника ProtectedDictInt
    print("d2", d2)
    d3 = d2 - 34
    # del d2[34]
    print("d2", d2)


