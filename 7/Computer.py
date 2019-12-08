from itertools import permutations

from Amplifier import Amplifier

l = list(permutations(range(5, 9)))
max_value = 0
DEBUG = True

class Computer():
    def __init__(self, phases, program):
        a = Amplifier(phases[0], program, 'a')
        b = Amplifier(phases[1], program, 'b', a)
        c = Amplifier(phases[2], program, 'c', b)
        d = Amplifier(phases[3], program, 'd', c)
        e = Amplifier(phases[4], program, 'e', d)

        a.prev = e

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = a

        cycle = 1
        curr = a

        while not e.is_halted():
            curr.step()

            if curr.get_state()[0] == 'Wait':
                curr = curr.next
                curr.state = 'Run'
                print(curr.get_state())
                print(cycle)
                print(curr.get_input())

                input()
            cycle += 1



        print(e.get_output())


phases = [9,8,7,6,5]
program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

Computer(phases, program)