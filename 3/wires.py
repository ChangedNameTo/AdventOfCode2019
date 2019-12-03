f = open('3/input.txt')
# f = open('3/test.txt')
# f = open('3/test2.txt')
# f = open('3/test3.txt')

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
            for x in range(0,magnitude):
                curr_x += 1
                path.append((curr_x,curr_y))
        elif direction == 'U':
            for x in range(0,magnitude):
                curr_y += 1
                path.append((curr_x,curr_y))
        elif direction == 'L':
            for x in range(0,magnitude):
                curr_x -= 1
                path.append((curr_x,curr_y))
        elif direction == 'D':
            for x in range(0,magnitude):
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

step_counts = []
int_count = 1

for intersection in intersections:
    step_1 = (path_1.index(intersection))
    step_2 = (path_2.index(intersection))
    # Accounts for (0,0)
    step_counts.append(step_1 + step_2 + 2)

print(min(step_counts))