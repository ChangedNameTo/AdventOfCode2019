class Amplifier():
    def __init__(self, phase, program, name, prev=None):
        self.program = program
        self.phase = phase
        self.state = 'Run'
        self.index = 0
        self.name = name

        self.input  = None
        self.output = None

        self.next = None
        self.prev = prev

        self.first_cycle = True

    def step(self):
        if self.first_cycle:
            self.input = self.phase
            self.read_frame()
            self.first_cycle = False
            self.input = 0
        else:
            if self.state == 'Run':
                self.read_frame()
            elif self.state == 'Wait':
                pass
            elif self.state == 'Stop':
                pass

    def get_output(self):
        return self.output

    def get_input(self):
        return self.prev.get_output()

    def get_state(self):
        return [self.state, self.name, self.program]

    def is_halted(self):
        return self.state == 'Stop'

    def get_values(self, opcode, mode_arr):
        values = []
        print(mode_arr)
        if opcode in [1,2,7,8]:
            for x in range(0, len(mode_arr) - 1):
                if mode_arr[x]:
                    values.append(self.program[self.index + x + 1])
                else:
                    values.append(self.program[self.program[self.index + x + 1]])
            values.append(self.program[self.index + 3])

        elif opcode in [3]:
            values.append(self.program[self.index + 1])

        elif opcode in [4]:
            if mode_arr[0]:
                values.append(self.program[self.index + 1])
            else:
                values.append(self.program[self.program[self.index + 1]])

        elif opcode in [5,6]:
            for x in range(0, len(mode_arr) - 1):
                if mode_arr[x]:
                    values.append(self.program[self.index + x + 1])
                else:
                    values.append(self.program[self.program[self.index + x + 1]])
            values.append(self.program[self.index + 3])

        return values

    def read_frame(self):
        abcde = self.program[self.index]
        tens = int(((abcde/10) % 10)) * 10
        ones = int(((abcde % 10)))
        opcode = tens + ones
        print(opcode)
        mode_1 = int((abcde / 100) % 10)
        mode_2 = int((abcde / 1000) % 10)
        mode_3 = int((abcde / 10000) % 10)

        mode_arr = [mode_1, mode_2, mode_3]

        # Halt
        if opcode == 99:
            self.phase = 'Stop'
            self.index += 0

        values = self.get_values(opcode, mode_arr)

        # Add
        if opcode == 1:
            self.program[values[2]] = values[0] + values[1]
            self.state = 'Run'
            self.index += 4

        # Multiply
        elif opcode == 2:
            self.program[values[2]] = values[0] * values[1]
            self.state = 'Run'
            self.index += 4

        # Input
        elif opcode == 3:
            self.program[values[0]] = self.input
            self.input = None
            self.state = 'Run'
            self.index += 2

        # Output
        elif opcode == 4:
            self.output = values[0]
            self.state = 'Wait'
            self.index += 2

        # Jump if true
        elif opcode == 5:
            self.state = 'Run'
            if values[0]:
                self.index = values[1]
            else:
                self.index += 3

        # Jump if false
        elif opcode == 6:
            self.state = 'Run'
            if not values[0]:
                self.index = values[1]
            else:
                self.index += 3

        # Less than
        elif opcode == 7:
            self.program[values[2]] = int(values[0] < values[1])
            self.state = 'Run'
            self.index += 4

        # Equals
        elif opcode == 8:
            self.program[values[2]] = int(values[0] == values[1])
            self.state = 'Run'
            self.index += 4

        else:
            print("!!!Error!!!")
            self.state = 'Stop'
            self.index += 0