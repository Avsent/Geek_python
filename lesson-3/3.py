a, b, c = map(int, input('Введите 3 числа через пробел - ').split())


def my_func():
    big_num = sorted([a, b, c], reverse=True)
    return big_num[0] + big_num[1]


print(my_func())
