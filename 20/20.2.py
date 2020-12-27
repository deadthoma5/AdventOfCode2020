testing = True

from collections import defaultdict
from functools import reduce
import shared
import numpy as np
import re

MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines()

MONSTER_OFFSETS = [(i, j) for i in range(len(MONSTER)) for j in range(len(MONSTER[0])) if MONSTER[i][j] == '#']

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
        return
    
    def __str__(self):
        return str(self.id)

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

def find_adjacent(tilecheck, tiles, side):
    for tile in tiles:
        if tilecheck != tile:
            if check_connection(tilecheck, tile, side):
                return tile
            for _ in range(3):
                tile.rot()
                if check_connection(tilecheck, tile, side):
                    return tile
            tile.flip()
            if check_connection(tilecheck, tile, side):
                return tile
            for _ in range(3):
                tile.rot()
                if check_connection(tilecheck, tile, side):
                    return tile

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
            if testing:
                print(f"Found corners: {' '.join(map(str, corners))}")
            return corners

def init_row(corners):
    for corner in corners:
        if testing:
            print(f"init_row processing corner: {corner}")            
            print(f"top: {find_adjacent(corner, tiles, 'T')}")
            print(f"bottom: {find_adjacent(corner, tiles, 'B')}")
            print(f"left: {find_adjacent(corner, tiles, 'L')}")
            print(f"right: {find_adjacent(corner, tiles, 'R')}")
        if find_adjacent(corner, tiles, 'R') and (len(corners) == 1 or find_adjacent(corner, tiles, 'B')):
            current_leftmost = corner
            next_row = find_adjacent(corner, tiles, 'B')
            break
    return current_leftmost, next_row

def make_row(tileinit, tiles, row):
    if testing:
        print(f"Making row...")
    while True:
        next_right = find_adjacent(tileinit, tiles, 'R')
        if testing:
            print(f"adjacent tile to the right: {find_adjacent(tileinit, tiles, 'R')}")
        if not next_right:
            if testing:
                print(f"End of row reached.")
            break
        else:
            next_in_row = np.copy(next_right.image[1:-1, 1:-1])
            row = np.concatenate((row, next_in_row), axis=1)
            tileinit = next_right
    return row

def generate_map(tiles, corners):
    rows = []
    while True:
        current_leftmost, next_row = init_row(corners)
        if testing:
            print(f"current_leftmost: {current_leftmost}, next_row: {next_row}")
        row_init = np.copy(current_leftmost.image[1:-1, 1:-1])
        row = make_row(current_leftmost, tiles, row_init)
        corners = [next_row]
        rows.append(row)
        if not next_row:
            if testing:
                print(f"No more rows to process.")
            break
    if testing:
        print(f"Compiling map...")
    map_monsters = rows[0]
    for row in rows[1:]:
        map_monsters = np.concatenate((map_monsters, row))
    if testing:
        print(f"map_monsters:\n{map_monsters}")
    return map_monsters

def find_monsters(map_monsters):
    count = 0
    for i in range(len(map_monsters) - 2):
        j = 0
        while j+20 <= len(map_monsters):
            monster_window = map_monsters[i:i+3, j:j+20]
            is_monster = True
            for coord in MONSTER_OFFSETS:
                x, y = coord
                if monster_window[x][y] != 1:
                    is_monster = False
                    break
            if is_monster:
                if testing:
                    print("Monster Found!")
                count += 1
            j += 1
    return count

def count_monsters(map_monsters):
    count = find_monsters(map_monsters)
    if count == 0:
        if testing:
            print(f"No monsters found.")
        for _ in range(3):
            map_monsters = np.rot90(map_monsters)
            if testing:
                print(f"Rotating map.")
            count = find_monsters(map_monsters)
            if count != 0:
                return count
            if testing:
                print(f"No monsters found.")
        map_monsters = np.flipud(map_monsters)
        if testing:
            print(f"Flipping map.")
        count = find_monsters(map_monsters)
        if count != 0:
            return count
        else:
            if testing:
                print(f"No monsters found.")
            for _ in range(3):
                map_monsters = np.rot90(map_monsters)
                if testing:
                    print(f"Rotating map.")
                count = find_monsters(map_monsters)
                if count != 0:
                    return count
                if testing:
                    print(f"No monsters found.")
    return count

def calc_roughness(map_monsters, count):
    s = 0
    for row in map_monsters:
        s += np.sum(row)
    return s - (15 * count)

# import text from file
if testing:
    #text = shared.read_input("input_test")
    text = shared.read_input("input")
else:
    text = shared.read_input("input")

# Part 2
tiles = make_tiles(text)
corners = find_corners(tiles)
map_monsters = generate_map(tiles, corners)
count = count_monsters(map_monsters)
part2 = calc_roughness(map_monsters, count)
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
