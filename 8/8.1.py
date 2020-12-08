testing = False

import shared

class Reader:
    def __init__(self):
        self.position = 0
        self.accumulator = 0
        self.history = []

    def nop(self, value):
        if testing:
            print(f"Step: nop {value}, pos: {self.position}, acc: {self.accumulator}")
        self.history.append(self.position)
        self.position += 1

    def acc(self, value):
        if testing:
            print(f"Step: acc {value}, pos: {self.position}, acc: {self.accumulator}")
        self.history.append(self.position)
        self.accumulator += value
        self.position += 1

    def jmp(self, value):
        if testing:
            print(f"Step: jmp {value}, pos: {self.position}, acc: {self.accumulator}")
        self.history.append(self.position)
        self.position += value

    def checkhistory(self):
        return self.position in self.history

if testing:
    text = shared.read_input("input_test")    # expected test value in accumulator = 5
else:
    text = shared.read_input("input")

instructions = shared.parse_input(text)

if testing:
    print(f"Instructions: {instructions}")

reader = Reader()

for index in range(len(instructions)):
    if instructions[reader.position][0] == "nop":
        reader.nop(int(instructions[reader.position][1]))
    elif instructions[reader.position][0] == "acc":
        reader.acc(int(instructions[reader.position][1]))
    elif instructions[reader.position][0] == "jmp":
        reader.jmp(int(instructions[reader.position][1]))
        if reader.checkhistory():
            print(f"\nInfinite loop encountered at Step {index}. Position: {reader.position}, Accumulator: {reader.accumulator}")
            print(f"History: {reader.history}\n")
            break
    
shared.printTimeElapsed()