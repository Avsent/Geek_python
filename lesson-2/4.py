# Попытался решить задание в минимум строк

for i, w in enumerate(input('Введите несколько слов через пробел - ').split(' '), 1):
    print(f'{i}. {w[0 : 10]}' if len(w) > 10 else f'{i}. {w}')
