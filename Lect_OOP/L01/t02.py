class InitDelTest():
    def __init__(self):
        print("InitDelTest: __init__")

    def __del__(self):
        print("InitDelTest: __del__")


initDel = InitDelTest()
# del initDel
# print("Hello!")
