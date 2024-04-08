class ProtectedDictIntIterator:
    """
    ітератор для колекції ProtectedDictInt, який перебирає колекцію,
     таким чином, щоб усі ключі словника були у порядку зростання.
    """
    def __init__(self, collection):
        self.collection = collection
        self.keys = list(collection.keys())
        self.keys.sort()
        self.index = 0

    def __next__(self):
        try:
            curr_key = self.keys[self.index]
            self.index += 1
            return curr_key, self.collection[curr_key]
        except IndexError:
            raise StopIteration

