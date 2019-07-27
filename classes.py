class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def do(self):
        print(self.x, self.y)


a = vector(1, 2)

a.do()

a = vector(3, 4)

a.do()
