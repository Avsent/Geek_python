my_str = "text"
my_bool = True
my_float = 3.14
my_int = 123
my_set = {"hi", "bye"}
my_tuple = ("qwerty", 12345)
my_dict = {'a': 1, 'b': 2}

com_list = [my_str, my_bool, my_float, my_int, my_set, my_tuple, my_dict]
for i in com_list:
    print(f'"{i}" - отностится к {type(i)}')
