testing = False
DAYS = 100

from collections import defaultdict
import re
import shared

d = {
    'e': 1,
    'se': 0.5 - 1j,
    'sw': -0.5 - 1j,
    'w': -1,
    'nw': -0.5 + 1j,
    'ne': 0.5 + 1j
}

def init_tiles(text):
    tiles = defaultdict(bool)
    for line in text:
        tiles[sum(d[step] for step in re.findall('e|se|sw|w|nw|ne', line))] ^= True    # True = Black
    return tiles

def count_black(tiles):
    return sum(tiles.values())

def game_of_life(tiles):
    for day in range(1, DAYS+1):
        for tile in tiles.copy():
            for n in d.values():
                tiles[tile+n]    # Grow the existing tile board
        tiles_ = tiles.copy()
        for tile in tiles_.keys():
            neighbors = sum(tiles[tile+n] for n in d.values())
            if tiles[tile] and (neighbors == 0 or neighbors > 2):
                tiles_[tile] ^= True    # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
            elif not tiles[tile] and (neighbors == 2):
                tiles_[tile] ^= True    # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        tiles = tiles_
        if testing:
            print(f"Day {day}: {count_black(tiles)}")
    return tiles

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(f"input: {text}")
else:
    text = shared.read_input("input")

# Part 1
tiles = init_tiles(text)
part1 = count_black(tiles)
print(f"[Part 1] {part1}")

# Part 2
tiles = game_of_life(tiles)
part2 = count_black(tiles)
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
