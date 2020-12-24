num = int(input('Введите целое положительное число - '))
num_max = num % 10
num = num // 10
while num > 0:
    if num % 10 > num_max:
        num_max = num % 10
    num = num // 10
print(f'Самая большая цифра в веденном числе - {num_max}')
