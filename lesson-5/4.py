my_trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}

res = []

with open("File-2.txt", "r", encoding='utf-8') as f:
    for line in f:
        tok = line.split()
        if tok[0] in my_trans:
            word = my_trans[tok[0]]
            res.append(word +' - '+ tok[2] + '\n')
    print(res)

out_f = open("File-3.txt", "w", encoding='utf-8')
for i in res:
    out_f.writelines(i)
out_f.close()
