import re
from time import time

_startTime = None

def read_input(filename):
    global _startTime
    with open(filename) as f:
        data = [l.rstrip("\n") for l in f.readlines()]

    _startTime = time()

    if len(data) == 1:
        try:
            return int(data[0])
        except:
            try:
                return [int(i) for i in data[0].split()]
            except:
                return data[0]
    else:
        try:
            return [int(i) for i in data]
        except:
            return data

def printTimeElapsed():
    global _startTime
    _endTime = time()
    elapsed = _endTime - _startTime
    print(f"Time: {elapsed:.3f}s")

def parse_input(text):
    parsed = []
    for line in text:
        parsed.append((* line.rstrip(".\n").split(" "),))    # store each step as a tuple
    return parsed