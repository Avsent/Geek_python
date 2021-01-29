from math import factorial

n = int(input('Укажите число для получения факториала - '))

def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)

for el in fact(n):
    print(el)
