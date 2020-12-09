testing = False

import shared
from itertools import combinations
        
if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
    preamble = 5
else:
    text = shared.read_input("input")
    preamble = 25

# Part 1
for i in range(preamble,len(text)):
    combos = list(combinations(text[i-preamble:i],2))
    sums = [sum(x) for x in combos]
    if testing:
        print(f"index: {i}, value: {text[i]}, combinations: {combos}")
        print(f"sums: {sums}")
    if text[i] not in sums:
        part1 = text[i]
        break

print(f"[Part 1] This value doesn't have a match in its preceding preamble: {part1}")

# Part 2
p1index = text.index(part1)
for i in range(p1index):
    flag = False
    indexcombos = list(combinations(range(p1index),2))
    ranges = [(x[0],x[1]+1) for x in indexcombos]
    for x in ranges:
        sums = [sum(text[x[0]:x[1]])]
        if part1 in sums:
            if testing:
                print(f"we got a match at indices: {x[0]} thru {x[1]-1}")
            startindex = x[0]
            endindex = x[1]
            resultlist = text[startindex:endindex]
            part2 = min(resultlist) + max(resultlist)
            flag = True
            break
    if flag:
        break

print(f"[Part 2] The sum of min/max values are: {part2}")

shared.printTimeElapsed()