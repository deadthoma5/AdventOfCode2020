testing = False
part1 = False

import shared

if testing or part1:
    CUPMAX = 9
else:
    CUPMAX = 1_000_000

def init_cups(text):
    cups_list = list(map(int, str(text)))
    cups_dict = dict()
    for idx, c in enumerate(cups_list[:-1]):
        cups_dict[c] = cups_list[idx+1]
    if CUPMAX > len(cups_list):
        cups_dict[cups_list[-1]] = len(cups_list) + 1
        for idx in range(len(cups_list)+1,CUPMAX):
            cups_dict[idx] = idx+1
        cups_dict[CUPMAX] = cups_list[0]
    else:
        cups_dict[cups_list[-1]] = cups_list[0]
    if testing:
        print(f"cups_dict: {cups_dict}")
    return cups_dict, cups_list[0]

def pickup_cups(cups, c):
    pickup = []
    c_pickup = cups[c]
    for _ in range(3):
        c_next = cups[c_pickup]
        pickup.append(c_pickup)
        del cups[c_pickup]
        c_pickup = c_next
    cups[c] = c_pickup
    return cups, pickup

def destination_cup(pickup, c):
    d = c - 1
    if d < 1:
        d = CUPMAX
    while d in pickup:
        d -= 1
        if d < 1:
            d = CUPMAX
    return d

def place_pickup(cups, pickup, d):
    c_next = cups[d]
    for p in pickup:
        cups[d] = p
        d = p
    cups[d] = c_next
    return cups

def current_cup(cups, c):
    return cups[c]

def solve1(cups):
    part1 = []
    c = 1
    for _ in range(len(cups)-1):
        part1.append(cups[c])
        c = cups[c]
    return ''.join([str(x) for x in part1])

def solve2(cups):
    return cups[1]*cups[cups[1]]

def moves(cups, c_start):
    if testing or part1:
        idx_stop = 100
    else:
        idx_stop = 10_000_000
    c = c_start
    for n in range(1, idx_stop+1):
        if testing:
            print(f"\n-- move {n} --")
            print(f"cups: {cups}")
            print(f"current cup: {c}")        

        cups, pickup = pickup_cups(cups, c)
        if testing:
            print(f"pick up: {pickup}")

        d = destination_cup(pickup, c)
        if testing:
            print(f"destination: {d}")

        cups = place_pickup(cups, pickup, d)

        c = current_cup(cups, c)
    if testing:
        print(f"\n-- final --")
        print(f"cups: {cups}")
        print(f"current cup: {c}\n\n")
    if part1:
        return solve1(cups)
    else:
        return solve2(cups)

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(f"input: {text}")
else:
    text = shared.read_input("input")
    #text = shared.read_input("input_test")

# Part 2
cups, c_start = init_cups(text)
part2 = moves(cups, c_start)
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
