from sys import argv

name, time, rate, bonus = argv

try:
    time = int(time)
    rate = int(rate)
    bonus = int(bonus)
    res = time * rate + bonus
    print(f"the employee's salary - {res}")

except ValueError:
    print('Not a number')
