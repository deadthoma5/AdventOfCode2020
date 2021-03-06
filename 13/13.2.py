testing = False

import shared
import re
import numpy as np

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

# Part 2
buses = text[1].split(',')
timestamp = np.int64(1)    # Because 32 bits isn't enough!
lcm = np.int64(1)    # Because 32 bits isn't enough!
for i, bus in enumerate(buses):
    if bus == 'x':
        continue
    else:
        bus = int(bus)        
    while ((timestamp + i) % bus) != 0:
        timestamp += lcm    # Don't need to iterate through every integer. Can skip ahead to next time sub-pattern repeats (every lcm).
    if testing:
        print(f"timestamp: {timestamp}, i: {i}, bus: {bus}, old lcm: {lcm}, new lcm: {np.lcm(lcm, bus)}")
    lcm = np.lcm(lcm, bus)
part2 = timestamp
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
