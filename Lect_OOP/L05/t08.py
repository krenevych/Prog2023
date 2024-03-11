class Waiter:
    def __init__(self, name):
        self.waiter_name = name

    def serve(self):
        print(f'Waiter {self.waiter_name} serves...')

class Singer:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(f'Singer {self.name} sings...')


class SingerWaiter(Singer, Waiter):
    def __init__(self, name):
        Singer.__init__(self, name)
        Waiter.__init__(self, name)

if __name__ == '__main__':
    # waiter = Waiter('Nikolya')
    # waiter.serve()
    #
    # singer = Singer('Nikolya')
    # singer.sing()

    singer_waiter = SingerWaiter('Nikolya')

    singer_waiter.serve()
    singer_waiter.sing()