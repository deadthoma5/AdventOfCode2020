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

#print(f"Worklist: {text[preamble:]}")
#print(f"Combinations: {list(combinations(text[:preamble],2))}")

for i in range(preamble,len(text)):
    combos = list(combinations(text[i-preamble:i],2))
    sums = [sum(x) for x in combos]
    if testing:
        print(f"index: {i}, value: {text[i]}, combinations: {combos}")
        print(f"sums: {sums}")
    if text[i] not in sums:
        res = text[i]
        break

print(f"This value doesn't have a match in its preceding preamble: {res}")

shared.printTimeElapsed()