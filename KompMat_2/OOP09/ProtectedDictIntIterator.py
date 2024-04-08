class ProtectedDictIntIterator:
    """
    Реалізуйте для класу ProtectedDictInt з задачі 5.2.1,
    підтримку ітераційного протоколу, таким чином,
    щоб ітератор перебирав усі ключі словника у порядку зростання.
    """

    def __init__(self, collection):
        self.collection = collection
        self.keys = list(collection.keys())
        self.keys.sort()
        self.index = 0 # поточна позиція у колекції


    def __next__(self):
        try:
            current = self.keys[self.index]
            self.index += 1
            return current
        except IndexError:
            raise StopIteration










