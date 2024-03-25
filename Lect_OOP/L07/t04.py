# Клас словник елементів, де ключами можуть бути лише рядки з 4 символів
# d = Dictionary4()
# d["sdfe"] = 12
# d["sdfeasdfwe"] = 12 - креш, заборонена операція, бо len("sdfeasdfwe") != 4
# d[34] = 12 - креш, заборонена операція, бо 34 не рядок

class Dictionary4:
    """ Користувацький словник

    Клас словник елементів, де ключами можуть бути лише рядки з 4 символів
    Клас Dictionary4 - обгортка навкол стандартного словника
    """
    def __init__(self):
        self.__my_dict = {}

    def __str__(self):
        return f"Dictionary4: {self.__my_dict}"

    def __setitem__(self, key, value):
        "Спеціальний метод, який реалізує оператор [] для додавання або заміни елементів"
        assert type(key) is str and len(key) == 4, "key must be str and 4 characters"
        self.__my_dict[key] = value

    def __getitem__(self, key):
        if key not in self.__my_dict:
            return None
        return self.__my_dict[key]

    def __len__(self):
        # Спеціальний метод, який дозволяє використовувати вбудовану функцію len для нашого словника
        return len(self.__my_dict)

    def __contains__(self, key):
        return key in self.__my_dict

    def __delitem__(self, key):
        del self.__my_dict[key]

if __name__ == '__main__':
    d = Dictionary4()
    print(d)
    d["asdf"] = 12 # d.__setitem__("asdf", 12)
    print(d)
    d["23__"] = 12
    print(d)
    print(len(d))
    print(d["23__"])  # d.__getitem__("23__")
    print(d["23"])



