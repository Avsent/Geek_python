a, b = map(int, input('Введите 2 числа через пробел - ').split())
while b == 0:
    b = int(input('Число b не должно быть равно 0. Повторите ввод второго числа - '))
def div():
    return a / b
print(f'Результат от деления - {div()}')
