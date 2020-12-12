testing = False

import shared
import operator

if testing:
    seats = shared.read_input("input_test")
    print(f"Instructions: {seats}")
else:
    seats = shared.read_input("input")

def moveTarget(target, direction):
    movedTarget = tuple(map(lambda a,b: a+b, target, direction))
    return movedTarget

def isTargetOutOfBounds(target, rowmax, colmax):
    y, x = target
    if (x < 0) or (x >= colmax) or (y < 0) or (y >= rowmax):
        #if testing:
        #    print("out of bounds")
        return True
    else:
        #if testing:
        #    print("not out of bounds")
        return False

def getTarget(seats, target):
    y, x = target
    return seats[y][x]

def evalSeat(seats, row, col, rowmax, colmax):
    if seats[row][col] == '.':
        return '.'
    else:
        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),               # skip (0, 0)
                    (1, -1), (1, 0), (1, 1)]
        for direction in directions:
            target = (row, col)
            target = moveTarget(target, direction)
            #if testing:
            #    print(f"checking target position: {target} | heading: {direction} | seat: {row}, {col}")
            while not isTargetOutOfBounds(target, rowmax, colmax):
            #    if testing:
            #        print(f"checking target position: {target} | heading: {direction} | seat: {row}, {col}")
                targetSeat = getTarget(seats, target)
                if targetSeat == '.':
            #        if testing:
            #            print(f"seat: {row, col}, target {target} is: ., ")
                    target = moveTarget(target, direction)
                    continue
                elif targetSeat == '#':
                    count += 1
            #        if testing:
            #            print(f"seat: {row, col}, target {target} is: #, ")
                    break
                elif targetSeat == 'L':
            #        if testing:
            #            print(f"seat: {row, col}, target {target} is: L, ")
                    break
        if seats[row][col] == 'L':
            if count == 0:
            #    if testing:
            #        print(f"Flipping L to #, count: {count}")
                return '#'
            else:
                return 'L'
        elif seats[row][col] == '#':
            if count >= 5:
            #    if testing:
            #        print(f"Flipping # to L, count: {count}")
                return 'L'
            else:
                return '#'

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
