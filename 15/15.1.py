testing = False

import shared

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

# Part 1
numbers = text.split(",")
for turn in range(len(numbers), 2020):
    last = numbers[-1]
    if testing:
        print(f"turn {turn+1}: evaluating {last}")
    indices = [i for i, x in enumerate(numbers) if x == last]
    if len(indices) == 1:
        if testing:
            print(f"turn {turn+1}: it's the first time {last} has been spoken. Adding 0 to the list.")
        numbers.append("0")
    else:
        if testing:
            print(f"turn {turn+1}: {last} was last spoken on turn {indices[-2]+1}. Adding {indices[-1]+1} - {indices[-2]+1} = {indices[-1] - indices[-2]} to the list.")
        numbers.append(str(indices[-1] - indices[-2]))
part1 = numbers[-1]
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
