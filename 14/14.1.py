testing = False

import shared
import re

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

def read(inst):
    if inst[0] == "mask":
        if testing:
            print(f"updating mask to {inst[1]}")
        op = "mask"
        index = 0
        value = inst[1]
        return op, index, value
    else:
        match = re.findall(r'([^\[\]]*)', inst[0])
        op = match[0]
        index = int(match[2])
        value = str(bin(int(inst[1])))[2:].zfill(36)
        return op, index, value

def calculate(mask, value):
    for i, c in enumerate(mask):
        if c == 'X':
            continue
        else:
            if testing:
                print(f"changed at mask index {i}: {value[i]} to {mask[i]}")
            value = value[:i] + mask[i] + value[i+1:]
            if testing:
                print(f"value is now: {value}")
    return value

# Part 1
instructions = shared.parse_input(text)
if testing: 
    print(instructions)
mem = dict()
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for inst in instructions:
    op, index, value = read(inst)
    if testing:
        print(f"instruction: op {op}, index {index}, value {value}")
    if op == "mask":
        mask = value
    else:
        mem[index] = calculate(mask, value)
if testing:
    print(f"final state of mem: {mem}")
total = 0
for i in mem:
    total += int(mem[i],2)
part1 = total
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
