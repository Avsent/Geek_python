my_num = sorted([4, 6, 3, 8, 1, 3], reverse=True)

print(f'Текущий рейтинг - {my_num}')

num = int(input('Введите новый элемент рейтинга - '))

for i in range(len(my_num)):
    if my_num[i] == num and my_num[i + 1] != num:
        my_num.insert(i + 1, num)
        break

    elif my_num[0] < num:
        my_num.insert(0, num)
        break

    elif my_num[-1] > num:
        my_num.append(num)
        break

    elif my_num[i] > num > my_num[i + 1]:
        my_num.insert(i + 1, num)
        break

print(f'Новый рейтинг - {my_num}')
