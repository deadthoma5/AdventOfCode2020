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

    def evaluate(self, instructions):
        for index in range(len(instructions)-1):
            if (self.position >= len(instructions)):
                print(f"\nProgram completed successfully at Step {index}. Position: {reader.position}, Accumulator: {reader.accumulator}")
                return True

            if instructions[self.position][0] == "nop":
                self.nop(int(instructions[self.position][1]))
            elif instructions[self.position][0] == "acc":
                self.acc(int(instructions[self.position][1]))
            elif instructions[self.position][0] == "jmp":
                self.jmp(int(instructions[self.position][1]))
                if self.checkhistory():
                    print(f"\nExiting. Infinite loop encountered at Step {index}. Position: {reader.position}, Accumulator: {reader.accumulator}")
                    print(f"History: {reader.history}\n")
                    return False
        
if testing:
    text = shared.read_input("input_test")    # expected test value in accumulator = 5
else:
    text = shared.read_input("input")

instructions = shared.parse_input(text)

if testing:
    print(f"Instructions: {instructions}")

for index in range(len(instructions)):
    if instructions[index][0] == "nop":
        worklist = instructions[:index] + [("jmp", instructions[index][1])] + instructions[index+1:]
        print(f"nop changed to jmp at Line {index}")
        reader = Reader()
        if reader.evaluate(worklist):
            break
        else:
            continue
    elif instructions[index][0] == "jmp":
        worklist = instructions[:index] + [("nop", instructions[index][1])] + instructions[index+1:]
        print(f"jmp changed to nop at Line {index}")
        reader = Reader()
        reader.evaluate(worklist)
        if reader.evaluate(worklist):
            break
        else:
            continue
    
shared.printTimeElapsed()