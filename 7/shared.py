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

def parse_rules(text):
    parsed = dict()
    for line in text:
        key, value = line.rstrip(".\n").split(" bags contain ")
        parsed[key] = {}
        for section in value.split(", "):
            try:
                pattern = re.compile("(\d+)( )([a-zA-Z ]+)( bag)([s]?)")
                match = pattern.match(section).groups()
                new_contents = dict()
                new_contents[match[2]] = int(match[0])
                parsed[key].update(new_contents)
            except AttributeError:
                parsed[key] = {}
    return parsed