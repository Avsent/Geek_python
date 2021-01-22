my_list = [100, 101, 112, 12, 12, 30, 4, 51, 16, 77, 0, 5]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list[1:])
