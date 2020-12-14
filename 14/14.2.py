testing = True

import shared
import re
from typing import Tuple, List

if testing:
    text = shared.read_input("input_test2")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

def read(inst: str) -> Tuple[str, int, str]:
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

def decode(mask: str, value: str) -> List[str]:
    for i, c in enumerate(mask):
        if c == '0':
            continue
        else:
            if testing:
                print(f"changed at mask index {i}: {value[i]} to {mask[i]}")
            value = value[:i] + mask[i] + value[i+1:]
            if testing:
                print(f"value is now: {value}")
    return [value]

def unpack(values: List[str], n:int=0) -> List[str]:
    if testing:
        print(f"recursion depth: {n}, input: {values}")
    if testing:
        print(f"values: {values}")
    valueList = []
    if values:
        for value in values:
            if testing:
                print(f"examining value: {value}")
            for i, c in enumerate(value):
                if c == 'X':
                    valueList.append(value[:i] + '0' + value[i+1:])
                    valueList.append(value[:i] + '1' + value[i+1:])
                    if testing:
                        print(f"valueList: {valueList}")
                    break
                else:
                    continue
    if not valueList:
        return values
    else:
        return unpack(valueList, n+1)

def getTotal(mem):
    return 0

# Part 2
instructions = shared.parse_input(text)
if testing: 
    print(instructions)
mem = dict()
for inst in instructions:
    op, index, value = read(inst)
    if testing:
        print(f"instruction: op {op}, index {index}, value {value}")
    if op == "mask":
        mask = value
    else:
        mem[index] = decode(mask, value)
for address in mem:
    if testing:
        print("-- unpacking Xs... --")
    mem[address] = unpack(mem[address])
if testing:
    print(f"final state of mem: {mem}")
total = 0
for address in mem:
    for x in mem[address]:
        total += int(x,2)
part2 = total
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
