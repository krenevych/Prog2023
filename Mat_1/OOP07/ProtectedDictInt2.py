class ProtectedDictInt(dict):
    def __setitem__(self, key, value):
        assert type(key) == int, "за умовою ключ має бути цілий"
        assert key not in self, "за умовою задачі значення, що відповідає ключу, що є в словнику змінювати вже не можна"
        # self[key] = value # self.__setitem__(key, value)
        super().__setitem__(key, value)

if __name__ == '__main__':
    d = ProtectedDictInt()
    # d = {}
    d[23] = "hello" # d.__setitem__(23, "hello")
    d[232] = "hello3" # d.__setitem__(23, "hello")
    # d[23] = "32" # заборонена за умовою задачі, бо неможна змінювати
    # d["Hello"] = "world" # заборонена, бо ключами мають бути лише числа
    print(d)
    d.update({23: 643, "Hello": "world"}) # хакнули систему, тому такий підхід не дуже хороший
    print(d)

