testing = False
printGrids = False

import shared
import numpy as np

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

def init_grid(text):
    global cycles, dim, startingWidth    
    origin = dim // 2
    startx = origin - startingWidth // 2
    starty = startx
    startz = origin
    grid = np.zeros((dim, dim, dim), dtype=int)
    for y in range(starty, starty+startingWidth):
        for x in range(startx, startx+startingWidth):
            if text[y - starty][x - startx] == '#':
                grid[startz][y][x] = 1
            else:
                grid[startz][y][x] = 0
    return grid

def evaluate(grid, z, y, x):
    count = 0
    gridValue = grid[z][y][x]
    for k in range(z-1, z+2):
        for j in range(y-1, y+2):
            for i in range(x-1, x+2):
                if (k != z) or (j != y) or (i != x):
                    if grid[k][j][i] == 1:    # neighbor is active
                        count += 1
    if gridValue == 1:
        if (count == 2) or (count == 3):
            return 1
        else:
            return 0
    elif gridValue == 0:
        if count == 3:
            return 1
        else:
            return 0

def count_cubes(grid):
    return np.count_nonzero(grid == 1)

# Part 1
if testing:
    cycles = 3
else:
    cycles = 6
startingWidth = len(text[0])
dim = startingWidth + cycles*10
if testing:
    print(f"dim: {dim}")

# note: z y x (0,0,0 = first and top-left)
grid = init_grid(text)
if testing and printGrids:
    print("Before any cycles:")
    print("z=0")
    print(grid[3][:][:])

for c in range(6):
    work = grid.copy()
    for z in range(1, dim - 1):
        for y in range(1, dim - 1):
            for x in range(1, dim - 1):
                work[z][y][x] = evaluate(grid, z, y, x)
    grid = work
    if testing and printGrids:
        print(f"\nAfter {c+1} cycles:")
        for z in range(1, dim - 1):
            print(f"z={z}")
            print(grid[z][:][:])
            print()

part1 = count_cubes(grid)
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
