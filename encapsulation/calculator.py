class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return c.first + c.second

    def sub(self):
        return c.second - c.first

    def mul(self):
        return c.first * c.second

    def div(self):
        return c.second / c.first

if __name__ == '__main__':
    c = Calculator()
    c.setdata(1, 2)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())