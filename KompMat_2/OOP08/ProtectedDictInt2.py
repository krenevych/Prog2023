class ProtectedDictInt(dict):
    def __setitem__(self, key, value):
        assert type(key) == int, "Ключі мають бути цілими"
        assert key not in self,  "Заборонена операція зміни значення за ключем"

        # self[key] = value - неможемо робити, бо буде рекурсія
        # self.__setitem__(key, value) - неможемо робити, бо буде рекурсія
        super().__setitem__(key, value) # викикаємо квадратні дужки з батьківського класу



if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = "world"
    # d[23] = "world"
    # d["hello"] = "world"
    # d["hello"] = "WORLD" # заборонено
    print(d)
    print(23 in d)
    print(2332 in d)
    d.update({"Hell": "World"}) # - хакнули систему, тому такий спосіб розвʼязання задачі у нашому випидку не дуже підходить
    print(d)
