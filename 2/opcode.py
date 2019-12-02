from tests import test_cases

def read_frame(index, program):
    opcode = program[index]

    # Halt
    if opcode == 99:
        return False

    position_1 = program[index + 1]
    position_2 = program[index + 2]
    position_3 = program[index + 3]

    # Add
    if opcode == 1:
        program[position_3] = program[position_1] + program[position_2]
        return True

    # Multiply
    elif opcode == 2:
        program[position_3] = program[position_1] * program[position_2]
        return True

    else:
        print("!!!Error!!!")
        return False

def output_sentence(program):
    print('======')
    print('('+str(program[1])+','+str(program[2])+')')
    print(program[0])

passed = True
for case in test_cases:
    program = case[0]
    asert   = case[1]

    running = True
    index   = 0
    while running:
        running = read_frame(index, program)
        index += 4

    if(program != asert):
        passed = False
        print("Test failed")
        print(program)
        print(asert)
        break

# Part 1
# if passed:
if False:
    print("Tests Passed")
    print("==============")

    program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]

    program[1] = 12
    program[2] = 2

    running = True
    pointer = 0
    while running:
        running = read_frame(index, program)
        index += 4

    print(program[0])
    print(program)

# Part 2
if passed:
    print("Tests Passed")
    print("==============")

    for i in range(0, 100):
        for j in range(0, 100):
            program = [1,i,j,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]

            running = True
            index   = 0
            while running:
                running = read_frame(index, program)
                index += 4

            # output_sentence(program)

            if(program[0] == 19690720):
                print('Value Found')
                print('---------')
                print(program[1])
                print(program[2])
                print((100 * program[1]) + program[2])
                break