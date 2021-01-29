my_f = open("my_f.txt", "w")
while True:
    my_str = input('Enter text - \n')
    if my_str == '':
        break
    else:
        my_f.writelines(my_str)
my_f.close()

with open("my_f.txt") as f:
    for i in f:
        print(i)
