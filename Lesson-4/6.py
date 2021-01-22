from itertools import count, cycle

a, b = map(int, input('Введите начальное и конечное число через пробел - ').split())
for el in count(a):
    if el > b:
        break
    else:
        print(el)


my_list = [123, 'abc', True, False]
i = 0
for el in cycle(my_list):
    if i > 10:
        break
    print(el)
    i += 1

