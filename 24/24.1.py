testing = False

from collections import defaultdict
import re
import shared

direction = {
    'e': 1,
    'se': 0.5 - 1j,
    'sw': -0.5 - 1j,
    'w': -1,
    'nw': -0.5 + 1j,
    'ne': 0.5 + 1j
}

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(f"input: {text}")
else:
    text = shared.read_input("input")

# Part 1
tiles = defaultdict(bool)
for line in text:
    tiles[sum(direction[step] for step in re.findall('e|se|sw|w|nw|ne', line))] ^= True    # True = Black
part1 = sum(tiles.values())
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
