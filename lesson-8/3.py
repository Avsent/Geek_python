class Exception(ValueError):
    pass

my_list = []

while True:
    try:
        num = input('enter a number or "Q" to exit - ')
        if num == 'q' or num == 'Q':
            break
        elif not num.isdigit():
            raise Exception(num)
        else:
            my_list.append(int(num))
            print(f'current list - {my_list}')
    except Exception as e:
        print(f'{e} - not a number!')

print(f'final list - {my_list}')
