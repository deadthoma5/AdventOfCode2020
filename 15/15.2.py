testing = False

import shared

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

# Part 2
target=30000000
nums = ["-1"]
nums = nums[:] + text.split(",")
for i, n in enumerate(nums):
    nums[i] = int(n)
numset = set()
last = dict()
lastlast = dict()
for i, n in enumerate(nums):
    if i > 0 and i != len(nums)-1:
        numset.add(n)
        last[n] = i
        lastlast[n] = -1
for turn in range(len(nums), target+1):
    prev = nums[-1]
    if testing:
        print(f"turn {turn}: evaluating {prev}")
    if prev not in numset:
        if testing:
            print(f"turn {turn}: it's the first time {prev} has been spoken. The {turn}th number spoken is 0.")
        nums.append(0)
        numset.add(prev)
        last[prev] = turn - 1
        lastlast[0] = last[0]
        last[0] = turn
    else:
        newNumber = last[prev] - lastlast[prev]
        if testing:
            print(f"turn {turn}: {prev} was last spoken on turn {last[prev]} and previously spoken on turn {lastlast[prev]}. The {turn}th number spoken is {last[prev]} - {lastlast[prev]} = {newNumber}.")
        nums.append(newNumber)
        try:
            lastlast[newNumber] = last[newNumber]
        except KeyError:
            lastlast[newNumber] = -1
        last[newNumber] = turn
part2 = nums[-1]
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
