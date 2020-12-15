testing = False

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
        address = 0
        value = inst[1]
        return op, address, value
    else:
        match = re.findall(r'([^\[\]]*)', inst[0])
        op = match[0]
        address = int(match[2])
        value = str(bin(int(inst[1])))[2:].zfill(36)
        return op, address, value

def decode(mask: str, address: int) -> List[int]:
    address = str(bin(int(address)))[2:].zfill(36)
    for i, c in enumerate(mask):
        if c == '0':
            continue
        else:
            if testing:
                print(f"changed at mask index {i}: {address[i]} to {mask[i]}")
            address = address[:i] + mask[i] + address[i+1:]
            if testing:
                print(f"address is now: {address}")
    if testing:
        print("-- unpacking Xs... --")
    addresses = unpack([address])
    for i, a in enumerate(addresses):
        addresses[i] = int(a, 2)
    if testing:
        print(f"decoded addresses: {addresses}")
    return addresses

def unpack(addresses: List[str], n:int=0) -> List[str]:
    if testing:
        print(f"recursion depth: {n}, input: {addresses}")
    newAddresses = []
    if addresses:
        for a in addresses:
            if testing:
                print(f"examining address: {a}")
            for i, c in enumerate(a):
                if c == 'X':
                    newAddresses.append(a[:i] + '0' + a[i+1:])
                    newAddresses.append(a[:i] + '1' + a[i+1:])
                    if testing:
                        print(f"newAddresses: {newAddresses}")
                    break
                else:
                    continue
    if not newAddresses:
        return addresses
    else:
        return unpack(newAddresses, n+1)

# Part 2
instructions = shared.parse_input(text)
if testing: 
    print(instructions)
mem = dict()
for inst in instructions:
    op, address, value = read(inst)
    if testing:
        print(f"instruction: op {op}, address {address}, value {value}")
    if op == "mask":
        mask = value
    else:
        for a in decode(mask, address):
            mem[a] = value
if testing:
    print(f"final state of mem: {mem}")
total = 0
for address in mem:
    total += int(mem[address],2)
part2 = total
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
