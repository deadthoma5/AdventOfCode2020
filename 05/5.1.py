import re

#filename = "input_test"
filename = "input"

seat_IDs = []

def row_count(row):
    seat_row = 0
    row = row.replace('F','0')
    row = row.replace('B','1')
    for char_index in range(len(row)):
        value = int(row[char_index])
        seat_row += value*2**(len(row)-char_index-1)
    return seat_row

def col_count(col):
    seat_col = 0
    col = col.replace('L','0')
    col = col.replace('R','1')
    for char_index in range(len(col)):
        value = int(col[char_index])
        seat_col += value*2**(len(col)-char_index-1)
    return seat_col

with open(filename) as f:
    for line in f:
        seatfilter = re.compile("([FB]{7})([LR]{3})") 
        row, col = seatfilter.match(line).groups()
        seat_IDs.append(row_count(row)*8+col_count(col))

print(max(seat_IDs))