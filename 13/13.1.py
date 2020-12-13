testing = False 

import shared
import re
import numpy as np

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

start = int(text[0])
time = start
target = 0
buses = re.findall(r'\d+',text[1])
n=0
isDone = False
while not isDone:
    for bus in buses:
        if time % int(bus) == 0:
            print(bus)
            target = int(bus)
            isDone = True
            break
    time +=1
    n += 1
part1 = (time - start - 1) * target
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
