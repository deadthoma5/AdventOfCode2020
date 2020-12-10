testing = True

import shared
from itertools import permutations
        
if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

# Part 1
p1text = text
p1text.insert(0,0)
p1text.append(max(text) + 3)
p1text.sort()
diff1, diff3 = 0, 0
for i in range(1,len(p1text)):
    diff = p1text[i] - p1text[i-1]
    if diff == 1:
        diff1 +=1
    elif diff == 3:
        diff3 += 1
print(f"[Part 1] {diff1*diff3}")

# Part 2
p2text = text
p2perm = permutations(p2text)
print(list(p2perm))
shared.printTimeElapsed()