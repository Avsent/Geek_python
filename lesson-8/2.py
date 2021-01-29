class Division:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    @staticmethod
    def divis(a, b):
        try:
            return f'result of division: {a / b}'
        except:
            return f'Error! Division by 0'


print(Division.divis(10, 0))
print(Division.divis(10, 0.5))
d = Division(1, 1)
print(d.divis(1, 0))
