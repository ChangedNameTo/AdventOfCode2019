# f = open('3/input.txt')
f = open('3/test.txt')

lines = f.read().splitlines()

paths = []
for line in lines:
    instructions = line.split(',')

    path = []
    curr_x = 0
    curr_y = 0

    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        if direction == 'R':
            for x in range(0,magnitude + 1):
                curr_x += 1
                path.append((curr_x,curr_y))
        elif direction == 'U':
            for x in range(0,magnitude + 1):
                curr_y += 1
                path.append((curr_x,curr_y))
        elif direction == 'L':
            for x in range(0,magnitude + 1):
                curr_x -= 1
                path.append((curr_x,curr_y))
        elif direction == 'D':
            for x in range(0,magnitude + 1):
                curr_y -= 1
                path.append((curr_x,curr_y))
        else:
            print('!!!!PANIC!!!!')
            break

    paths.append(path)

intersections = set(paths[0]).intersection(paths[1])

# Part 1
min_dist = 999999999999999
min_pair = (0,0)
for insersection in intersections:
    x = insersection[0]
    y = insersection[1]
    man_dist = abs(x) + abs(y)
    if man_dist < min_dist:
        min_dist = man_dist
        min_pair = insersection
# print(min_dist)

path_1 = paths[0]
path_2 = paths[1]

path_1_steps = []
path_2_steps = []
for intersection in intersections:
    path_1_steps.append(path_1.index(intersection))
    path_2_steps.append(path_2.index(intersection))
