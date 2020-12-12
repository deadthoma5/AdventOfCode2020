testing = False

import shared
import operator

if testing:
    seats = shared.read_input("input_test")
    print(f"Instructions: {seats}")
else:
    seats = shared.read_input("input")

def moveTarget(target, direction):
    return tuple(map(lambda a,b: a+b, target, direction))

def isTargetOutOfBounds(target, rowmax, colmax):
    y, x = target
    if (x < 0) or (x >= colmax) or (y < 0) or (y >= rowmax):
        return True
    else:
        return False

def evalSeat(seats, row, col, rowmax, colmax):
    seat = seats[row][col]
    if seat == '.':
        return '.'
    else:
        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),               # skip (0, 0)
                    (1, -1), (1, 0), (1, 1)]
        for direction in directions:
            target = (row, col)
            target = moveTarget(target, direction)
            while not isTargetOutOfBounds(target, rowmax, colmax):
                targetSeat = seats[target[0]][target[1]]
                if targetSeat == '.':
                    target = moveTarget(target, direction)
                    continue
                elif targetSeat == '#':
                    count += 1
                    break
                elif targetSeat == 'L':
                    break
        return 'L' if (seat == 'L' and count != 0) or (seat == '#' and count >= 5) else '#'

# Part 2
rowmax, colmax = len(seats), len(seats[0])
working = seats.copy()
isDone = False
n = 0
while not isDone:
    for i in range(rowmax):
        for j in range(colmax):
            working[i] = working[i][:j] + evalSeat(seats, i, j, rowmax, colmax) + working[i][j+1:]
    if seats == working:
        isDone = True
    else:
        n += 1
        seats = working.copy()
        if testing:
            print(f"Iteration {n}:")
            for row in seats:
                print(row)
            print()
print(f"Completed after {n} iterations.")
total = 0
for row in seats:
    total += row.count('#')
print(f"\n[Part 2] {total}")

# Display the time this took to run
shared.printTimeElapsed()
