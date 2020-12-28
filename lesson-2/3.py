seasons = {
    'winter': (12, 1, 2),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}

month = int(input('Введите месяц в виде целого числа от 1 до 12 - '))

for i in seasons.keys():
    if month in seasons[i]:
        print(i)

seasons_list = list(seasons.keys())
if 3 <= month <= 5:
    print(seasons_list[1])
elif 6 <= month <= 8:
    print(seasons_list[2])
elif 9 <= month <= 11:
    print(seasons_list[3])
elif month == 12 or 1 <= month <= 2:
    print(seasons_list[0])
else:
    print('Вы ввели неправильное число!')
