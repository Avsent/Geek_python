my_f = "File-1.txt"

lines_num = 0

with open(my_f, 'r') as f:
    for line in f:
        words_num = 0
        words = line.split()
        lines_num += 1
        words_num += len(words)
        print(f'Количество слов в {lines_num} строке - {words_num}')

    print(f'Количество строк - {lines_num}')
