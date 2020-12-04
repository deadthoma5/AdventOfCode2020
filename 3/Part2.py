#!/usr/bin/python

with open("input") as f:
    data = f.read().splitlines()

def count_trees(stepright, stepdown):
    row = 0
    col = 0
    trees = 0
    for line in data:
        row += stepdown
        col += stepright
        if row <= len(data):
            if data[row-stepdown][col-stepright] == '#':
                trees += 1
        col %= len(line)
    return trees

stepright = 1
stepdown = 1
print(count_trees(stepright,stepdown))

stepright = 3
stepdown = 1
print(count_trees(stepright,stepdown))

stepright = 5
stepdown = 1
print(count_trees(stepright,stepdown))

stepright = 7
stepdown = 1
print(count_trees(stepright,stepdown))

stepright = 1
stepdown = 2
print(count_trees(stepright,stepdown))

print(68*268*73*75*31)