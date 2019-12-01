from math import trunc

f = open('1/input.txt')
# f = open('1/test.txt')

def fuel_left(x):
    if x <= 0:
        return 0
    else:
        iter_fuel = fuel_needed(x)
        return (iter_fuel + fuel_left(iter_fuel))

def fuel_needed(x):
    need = x // 3 - 2
    if need > 0:
        return need
    else:
        return 0

total = 0
for line in f:
    fueled = fuel_needed(int(line))
    total += (fueled + fuel_left(fueled))

# total += fuel_left(total)

print(total)