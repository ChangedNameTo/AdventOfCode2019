from tests import test_cases
from program import diag
from itertools import permutations
from Amplifier import Amplifier

intcode_comp = Amplifier()
passed = True
test_ind = 1
for case in test_cases:
    program = case[0]
    p_input = case[1]
    p_phases = case[2]
    p_output = None
    e_output = case[3]

    phase_shift = 0
    first_cycle = True

    running = True
    index   = 0
    while running:
        if first_cycle:
            running, inc, p_output = intcode_comp.read_frame(index, program, p_phases[phase_shift], p_output)
            first_cycle = False
        else:
            running, inc, p_output = intcode_comp.read_frame(index, program, p_input, p_output)

        if running == 'Jump':
            index = inc
            running = True
        else:
            index += inc

        if p_output and phase_shift < len(p_phases) - 1:
            p_input = p_output
            p_output = None
            first_cycle = True
            phase_shift += 1
            index = 0

            # print('=====')
            # print(p_input)
            # print(phase_shift)
            # print(program)


    if(p_output != e_output):
        passed = False
        print("Test failed: " + str(test_ind))
        print("Phase Shift: " + str(phase_shift))
        print('Actual: ' + str(p_output))
        print('Expected: ' + str(e_output))
        print(program)
        print('----')
        break
    else:
        print('Pass for Case ' + str(test_ind))
        test_ind += 1
        print('----')

if passed:
    print("Tests passed")
    print("========")

    l = list(permutations(range(0, 5)))
    max_value = 0
    phases = None
    for cycle in l:
        program = diag[0]
        p_input = diag[1]
        p_phases = cycle
        # Create phase tester
        p_output = None

        phase_shift = 0
        first_cycle = True

        running = True
        index   = 0
        while running:
            if first_cycle:
                running, inc, p_output = intcode_comp.read_frame(index, program, p_phases[phase_shift], p_output)
                # running, inc, p_output = read_frame(index, program, p_input, p_output)
                first_cycle = False
            else:
                # running, inc, p_output = read_frame(index, program, p_phases[phase_shift], p_output)
                running, inc, p_output = intcode_comp.read_frame(index, program, p_input, p_output)

            if running == 'Jump':
                index = inc
                running = True
            else:
                index += inc

            if p_output and phase_shift < len(p_phases) - 1:
                p_input = p_output
                p_output = None
                first_cycle = True
                phase_shift += 1
                index = 0

        if p_output > max_value:
            max_value = p_output
            phases = cycle

    print(max_value)
    print(phases)