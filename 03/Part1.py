#!/usr/bin/python

with open("input") as f:
    data = f.read().splitlines()

trees = 0
row = 0
col = 0
ymove = 1
xmove = 3

for line in data:
    row += ymove
    col += xmove
    if row <= len(data):
        if data[row-ymove][col-xmove] == '#':
            trees += 1
    col %= len(line)

print(trees)