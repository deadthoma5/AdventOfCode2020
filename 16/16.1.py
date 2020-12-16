testing = True

import shared

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

# Part 1
rules, myTicket, nearbyTickets = shared.split_input(text)
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
