testing = False

from collections import defaultdict
from functools import reduce
import shared
import numpy as np
import re

class Tile:
    def __init__(self, raw_tile):
        parsed = parse_tile(raw_tile)
        self.id = parsed[0]
        self.image = parsed[1]
        self.__recalculate_borders()
        if testing:
            print(f"tile_id: {self.id}")
            print(f"tile_image:\n{self.image}")
            print(f"tile_borders: {self.top} {self.bottom} {self.left} {self.right}")
            print()

    def __calc_borders(self):
        top = '0b' + ''.join(map(str, self.image[0]))
        bottom = '0b' + ''.join(map(str, self.image[-1]))
        left = '0b' + ''.join(map(str, self.image[:,0]))
        right = '0b' + ''.join(map(str, self.image[:,-1]))
        return (int(x, 2) for x in (top, bottom, left, right))

    def __recalculate_borders(self):
        self.top, self.bottom, self.left, self.right = self.__calc_borders()
        return

    def rot(self, n=1):
        self.image = np.rot90(self.image, n)
        self.__recalculate_borders()
        return

    def flip(self):
        self.image = np.flipud(self.image)
        self.__recalculate_borders()
        return

def make_tiles(text):
    tiles = []
    for t in text:
        tiles.append(Tile(t))
    return tiles

def parse_tile(tile):
    lines = tile.splitlines()
    tile_id = int(re.findall(r'\d+', lines[0])[0])
    arr = []
    for l in lines[1:]:
        int_line = []
        for c in l:
            if c == '.':
                int_line.append(0)
            elif c == '#':
                int_line.append(1)
        arr.append(int_line)
    tile_image = np.array(arr)
    return tile_id, tile_image

def check_connection(A, B, side):
    if side == 'T' and A.top == B.bottom:
        return True
    elif side == 'B' and A.bottom == B.top:
        return True
    elif side == 'L' and A.left == B.right:
        return True
    elif side == 'R' and A.right == B.left:
        return True
    else:
        return False

def count_adjacent(tilecheck, tiles, side, edgecount):
    for tile in tiles:
        if tilecheck != tile:
            if check_connection(tilecheck, tile, side):
                edgecount[tilecheck.id] += 1
                return
            for _ in range(3):
                tile.rot()
                if check_connection(tilecheck, tile, side):
                    edgecount[tilecheck.id] += 1
            tile.flip()
            if check_connection(tilecheck, tile, side):
                edgecount[tilecheck.id] += 1
                return
            for _ in range(3):
                tile.rot()
                if check_connection(tilecheck, tile, side):
                    edgecount[tilecheck.id] += 1

def find_corners(tiles):
    edgecount = defaultdict(int)
    corners = []
    for tilecheck in tiles:
        if testing:
            print(f"Checking {tilecheck.id}")
        for side in ("TBLR"):
            count_adjacent(tilecheck, tiles, side, edgecount)
        if edgecount[tilecheck.id] == 2:
            corners.append(tilecheck)
        if len(corners) == 4:
            return corners

# import text from file
if testing:
    text = shared.read_input("input_test")
else:
    text = shared.read_input("input")

# Part 1
tiles = make_tiles(text)
corners = find_corners(tiles)
part1 = reduce(lambda a, b: a * b, [corner.id for corner in corners])
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
