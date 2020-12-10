testing = False

import shared

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")
    
# Part 1
text.sort()
text.insert(0,0)
text.append(text[-1] + 3)
if testing:
    print(f"Sorted: {text}")
diff = [0] * 4
for i in range(1,len(text)):
    x = text[i] - text[i-1]
    assert x <= 3
    diff[x] += 1
print(f"[Part 1] {diff[1]*diff[3]}")

# Part 2
res = [1]
for i in range(1, len(text)):
    count = 0
    for j in range(i):
        if text[i] - text[j] <= 3:
            count += res[j]
    res.append(count)
print(f"[Part 2] {res[-1]}")

# Display the time this took to run
shared.printTimeElapsed()