sum = 0
iter = True
while iter == True:
    num = input('Input numbers or Q for quit - ').split()
    res = 0
    for i in range(len(num)):
        if num[i].upper() == 'Q':
            iter = False
            break
        else:
            res += int(num[i])
    sum += res
    print(f'Current amount - {sum}')
print(f'Final amount - {sum}')
