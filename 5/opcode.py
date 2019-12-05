from tests import test_cases
from program import diag

def get_values(index, program, opcode, mode_arr):
    values = []

    if opcode in [1,2,7,8]:
        for x in range(0, len(mode_arr) - 1):
            if mode_arr[x]:
                values.append(program[index + x + 1])
            else:
                values.append(program[program[index + x + 1]])
        values.append(program[index + 3])

    elif opcode in [3]:
        values.append(program[index + 1])

    elif opcode in [4]:
        if mode_arr[0]:
            values.append(program[index + 1])
        else:
            values.append(program[program[index + 1]])

    elif opcode in [5,6]:
        for x in range(0, len(mode_arr) - 1):
            if mode_arr[x]:
                values.append(program[index + x + 1])
            else:
                values.append(program[program[index + x + 1]])
        values.append(program[index + 3])

    return values


def read_frame(index, program, p_input, p_output):
    abcde = program[index]
    tens = int(((abcde/10) % 10)) * 10
    ones = int(((abcde % 10)))
    opcode = tens + ones

    mode_1 = int((abcde / 100) % 10)
    mode_2 = int((abcde / 1000) % 10)
    mode_3 = int((abcde / 10000) % 10)

    mode_arr = [mode_1, mode_2, mode_3]

    # Halt
    if opcode == 99:
        return False, 0, p_output

    values = get_values(index, program, opcode, mode_arr)

    # Add
    if opcode == 1:
        program[values[2]] = values[0] + values[1]
        return True, 4, p_output

    # Multiply
    elif opcode == 2:
        program[values[2]] = values[0] * values[1]
        return True, 4, p_output

    # Input
    elif opcode == 3:
        program[values[0]] = p_input
        return True, 2, p_output

    # Output
    elif opcode == 4:
        p_output = values[0]
        return True, 2, p_output

    # Jump if true
    elif opcode == 5:
        if values[0]:
            return 'Jump', values[1], p_output
        else:
            return True, 3, p_output

    # Jump if false
    elif opcode == 6:
        if not values[0]:
            return 'Jump', values[1], p_output
        else:
            return True, 3, p_output

    # Less than
    elif opcode == 7:
        program[values[2]] = int(values[0] < values[1])
        return True, 4, p_output

    # Equals
    elif opcode == 8:
        program[values[2]] = int(values[0] == values[1])
        return True, 4, p_output

    else:
        print("!!!Error!!!")
        return False, 0, p_output

passed = True
test_ind = 1
for case in test_cases:
    program = case[0]
    p_input = case[1]
    p_output = None
    e_output = case[2]

    running = True
    index   = 0
    while running:
        running, inc, p_output = read_frame(index, program, p_input, p_output)
        if running == 'Jump':
            index = inc
            running = True
        else:
            index += inc

    if(p_output != e_output):
        passed = False
        print("Test failed: " + str(test_ind))
        print('Actual: ' + str(p_output))
        print('Expected: ' + str(e_output))
        print(program)
        break

    # print('Pass for Case ' + str(test_ind))
    # test_ind += 1
    # print('-----')

if passed:
    print("Tests passed")
    print("========")

    program = diag[0]
    p_input = diag[1]
    p_output = None

    running = True
    index   = 0
    while running:
        running, inc, p_output = read_frame(index, program, p_input, p_output)
        if running == 'Jump':
            index = inc
            running = True
        else:
            index += inc

    print(p_output)