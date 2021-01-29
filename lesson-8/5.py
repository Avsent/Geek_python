class ComplexNum:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'sum of numbers (a + b * i) + (c + d * i): ')
        return f'z = {self.a + other.a + self.b + other.b} * i'

    def __mul__(self, other):
        print(f'\nmultiplication of numbers (a + b * i)(c + d * i): ')
        return f'z = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'

z_1 = ComplexNum(5, -3)
z_2 = ComplexNum(2, 1)
print(z_1 + z_2)
print(z_1 * z_2)
