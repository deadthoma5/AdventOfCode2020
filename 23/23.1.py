testing = False

import shared

def pickup_cups(cups, c):
    cups_copy = cups.copy() * 2
    idx_pickup = cups.index(c) + 1
    pickup = cups_copy[idx_pickup:idx_pickup+3]
    for p in pickup:
        cups.remove(p)
    return cups, pickup

def destination_cup(cups, c):
    d = c - 1
    while d not in cups:
        d -= 1
        if d < min(cups):
            d = max(cups)
    return d

def place_pickup(cups, pickup, d):
    idx_d = cups.index(d)
    cups = cups[:idx_d+1] + pickup + cups[idx_d+1:]
    return cups

def current_cup(cups, c):
    cups_copy = cups.copy() * 2
    idx_c = cups.index(c)
    c = cups_copy[idx_c+1]
    return c

def get_order(cups):
    cups_copy = cups.copy() * 2
    idx_1 = cups.index(1)
    return ''.join([str(x) for x in cups_copy[idx_1+1:idx_1+len(cups)]])

def moves(cups):
    c = cups[0]
    idx_stop = 100
    for n in range(1, idx_stop+1):
        if testing:
            print(f"\n-- move {n} --")
            print(f"cups: {cups}")
            print(f"current cup: {c}")        

        cups, pickup = pickup_cups(cups, c)
        if testing:
            print(f"pick up: {pickup}")

        d = destination_cup(cups, c)
        if testing:
            print(f"destination: {d}")

        cups = place_pickup(cups, pickup, d)

        c = current_cup(cups, c)
    if testing:
        print(f"\n-- final --")
        print(f"cups: {cups}\n\n")
    return get_order(cups)

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(f"input: {text}")
else:
    text = shared.read_input("input")

# Part 1
cups = list(map(int, str(text)))
part1 = moves(cups)
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
