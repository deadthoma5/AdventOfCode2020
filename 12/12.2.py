testing = False

import shared
import re
import numpy as np

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

def rotate(velocity, step):
    n = int(step[1])
    theta = np.radians(n)
    c, s = np.cos(theta), np.sin(theta)
    if step[0] == 'L':
        R = np.array(((c, -s), (s, c)))
        R = np.matrix.round(R).astype(int)
        if testing:
            print(f"rotating L {n}. new velocity {R.dot(velocity)}")
        return R.dot(velocity)
    elif step[0] == 'R':
        R = np.array(((c, s), (-s, c)))
        R = np.matrix.round(R).astype(int)
        if testing:
            print(f"rotating R {n}. new velocity {R.dot(velocity)}")
        return R.dot(velocity)
    
def move(position, velocity, step):
    n = int(step[1])
    if (step[0] == 'L') or (step[0] == 'R'):
        velocity = rotate(velocity, step)
        return position, velocity
    elif step[0] == 'F':
        if testing:
            print(f"moving {step[0]} {n}")
        return np.add(position, n*velocity), velocity
    else:
        if testing:
            print(f"moving {step[0]} {n}")
        if step[0] == 'N':
            shift = np.array((0, 1))
        elif step[0] == 'S':
            shift = np.array((0, -1))
        elif step[0] == 'E':
            shift = np.array((1, 0))
        elif step[0] == 'W':
            shift = np.array((-1, 0))
        return position, np.add(velocity, n*shift)

# Part 2
position = np.array((0, 0))
velocity = np.array((10, 1))    # +x = east, +y = north
instructions=[]
for line in text:
    step = re.findall(r'\d+|\D+', line)
    instructions.append(step)
for step in instructions:
    position, velocity = move(position, velocity, step)
    if testing:
        print(f"current position: {position}")
part2 = abs(position[0]) + abs(position[1])
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
