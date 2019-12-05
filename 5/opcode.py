from tests import test_cases
from program import program

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

    elif opcode == 3:
        program[position ]

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
