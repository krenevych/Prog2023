class Collection:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

class Iterator:
    def __init__(self, collection):
        self.__collection = collection  # колекція, яку буде проходити ітератор
        self.__index = 0 # поточна позиція ітератора у колекції

    def __next__(self):
        if self.__index < len(self.__collection): # елементи ще є у колекції
            item = self.__collection[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration()  # за домовленістю розробників пайтон це треба для циклу for



if __name__ == '__main__':
    # lst = [1, 2, 3]
    # for item in lst:
    #     print(item)

    colection = Collection()
    colection.add(1)
    colection.add(2)
    colection.add(3)

    iterator = Iterator(colection)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    # for item in colection:
    #     print(item)




