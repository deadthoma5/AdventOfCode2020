testing = False

import shared
        
if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

# Part 1
text.insert(0,0)
text.append(max(text) + 3)
text.sort()
diff1, diff3 = 0, 0
for i in range(1,len(text)):
    diff = text[i] - text[i-1]
    if diff == 1:
        diff1 +=1
    elif diff == 3:
        diff3 += 1

print(f"[Part 1] {diff1*diff3}")

shared.printTimeElapsed()