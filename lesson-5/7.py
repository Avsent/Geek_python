from json import dumps

results = [{}, {}]

with open("File-6.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
for i in lines:
    name, init, proc, exp = i.split()
    results[0][name] = int(proc) - int(exp)

sum = 0
comp = 0
for i in results[0].values():
    if i >= 0:
        sum += i
        comp += 1
results[1]['average_profit'] = round(sum / comp)

print(results)

with open("File-6.json", "w", encoding='utf-8') as f:
    f.write(dumps(results))
