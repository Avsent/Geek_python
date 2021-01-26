class Cell:

    def __init__(self, param):
        self.param = int(param)

    def __add__(self, other):
        return f'amount of cells: {self.param + other.param}'

    def __sub__(self, other):
        return f'difference between the cells: {self.param - other.param}'\
            if self.param - other.param > 0 else 'the difference is less than 0'

    def __mul__(self, other):
        return f'composition of cells: {self.param * other.param}'

    def __truediv__(self, other):
        return f'cell division: {self.param // other.param}'

    def make_order(self, other):
        result = ''
        for i in range(int(self.param / other)):
            result += '*' * other + '\n'
        result += '*' * (self.param % other) + '\n'
        return result

c_1 = Cell(10)
c_2 = Cell(8)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order(5))
