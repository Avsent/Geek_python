my_str = input('Enter a word or letter - ').split()

def int_func(words):
    res = ""
    for i in words:
        i = i[0].upper() + i[1:]
        res += i + " "
    return res

print(int_func(my_str))
