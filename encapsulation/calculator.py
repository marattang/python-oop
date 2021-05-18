def add_function(first, second):
    return first+second

def sub_function(first, second):
    return first-second

def mul_function(first, second):
    return first*second

def div_function(first, second):
    return first/second

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
# 다중 주석 ctrl /
if __name__ == '__main__':
    c = Calculator()
    c.setdata(1, 2)
    # print(c.add())
    # print(c.sub())
    # print(c.mul())
    # print(c.div())
    print(add_function(5, 4))
    print(sub_function(5, 4))
    print(mul_function(5, 4))
    print(div_function(5, 4))
