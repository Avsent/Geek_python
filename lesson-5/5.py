def my_sum():
    try:
        with open("File-4.txt", "w+") as f:
            line = input('Введите цифры через пробел -\n')
            f.writelines(line)
            my_num = line.split()
            print(sum(map(int, my_num)))
    except IOError:
        print('IOError')
    except ValueError:
        print('ValueError')

my_sum()
