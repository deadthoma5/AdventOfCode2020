import re
from time import time

_startTime = None

def read_input(filename):
    global _startTime
    
    with open(filename) as f:
        data = [line.strip() for line in f]

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
    print(f"\n\nTime: {elapsed:.3f}s")

def split_input(text):
    splits = [i for i, x in enumerate(text) if x == ""]
    rules = text[:splits[0]]
    print(rules)
    for line in text:
        parsed.append((* line.rstrip(".\n").split(" = "),))    # store each step as a tuple
    return parsed