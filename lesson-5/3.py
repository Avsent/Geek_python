with open("salary", "r", encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f'{key}: оклад меньше 20000 руб. и составляет - {value} руб.')
