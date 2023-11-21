try:
    print("hello")
    raise ConnectionError
    print("world")
except ConnectionError:
    print("raise ConnectionError")