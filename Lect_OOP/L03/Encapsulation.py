class Foo:
    def __init__(self):
        self._bar = "Hello World! (bar)"
        self.__baz = "Hello World! (baz)"

    def __str__(self):
        return "Foo: bar: " + self._bar + " baz: " + self.__baz


if __name__ == '__main__':
    foo = Foo()
    print(foo)
    foo._bar = "Hello World! 2"
    foo._Foo__baz = "New baz 3"
    print(foo)
