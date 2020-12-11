testing = False

import shared

if testing:
    seats = shared.read_input("input_test")
    print(f"Instructions: {seats}")
else:
    seats = shared.read_input("input")

def evalSeat(seats, row, col):
    if row == 0:
        rowrange = range(0, 2)
    elif row == len(seats) - 1:
        rowrange = range(-1, 1)
    else:
        rowrange = range(-1, 2)
    if col == 0:
        colrange = range(0, 2)
    elif col == len(seats[0]) - 1:
        colrange = range(-1, 1)
    else:
        colrange = range(-1, 2)
    count = 0
    for i in rowrange:
        for j in colrange:
            if i == 0 and j == 0:
                continue
            elif seats[row + i][col + j] == '#':
                count += 1
    if seats[row][col] == '.':
        return '.'
    elif seats[row][col] == 'L':
        if count == 0:
            return '#'
        else:
            return 'L'
    elif seats[row][col] == '#':
        if count >= 4:
            return 'L'
        else:
            return '#'

# Part 1
rows, cols = len(seats), len(seats[0])
working = seats.copy()

flag = True
n = 0
while flag:
    for i in range(rows):
        for j in range(cols):
            working[i] = working[i][:j] + evalSeat(seats, i, j) + working[i][j+1:]
    if seats == working:
        flag = False
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
print(f"\n[Part 1] {total}")

# Display the time this took to run
shared.printTimeElapsed()
