subj = {}

with open("File-5.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for i in lines:
        data = i.replace('(', ' ').split()
        subj[data[0]] = sum(int(i) for i in data if i.isdigit())

print(subj)
