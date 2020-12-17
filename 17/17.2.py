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
    startw = origin
    grid = np.zeros((dim, dim, dim, dim), dtype=int)
    for y in range(starty, starty+startingWidth):
        for x in range(startx, startx+startingWidth):
            if text[y - starty][x - startx] == '#':
                grid[startw][startz][y][x] = 1
            else:
                grid[startw][startz][y][x] = 0
    return grid

def evaluate(grid, w, z, y, x):
    count = 0
    gridValue = grid[w][z][y][x]
    for l in range(w-1, w+2):
        for k in range(z-1, z+2):
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    if (l != w) or (k != z) or (j != y) or (i != x):
                        if grid[l][k][j][i] == 1:    # neighbor is active
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

# Part 2
cycles = 6
startingWidth = len(text[0])
dim = startingWidth + cycles*3
if testing:
    print(f"dim: {dim}")

# note: w z y x (0,0,0,0 = first and top-left)
grid = init_grid(text)
if testing and printGrids:
    print("Before any cycles:")
    print("w=0, z=0")
    print(grid[dim // 2][dim // 2][:][:])

for c in range(6):
    work = grid.copy()
    for w in range(1, dim - 1):
        for z in range(1, dim - 1):
            for y in range(1, dim - 1):
                for x in range(1, dim - 1):
                    work[w][z][y][x] = evaluate(grid, w, z, y, x)
    grid = work

part2 = count_cubes(grid)
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
