import re
from time import time

_startTime = None

def read_input(filename):
    global _startTime
    
    with open(filename) as f:
        rules, messages = [line.rstrip('\n') for line in f.read().split('\n\n')]

    _startTime = time()

    return rules, messages
    
def printTimeElapsed():
    global _startTime
    _endTime = time()
    elapsed = _endTime - _startTime
    print(f"\n\nTime: {elapsed:.3f}s")

def parse_input(text):
    parsed = []
    for line in text:
        parsed.append((* line.rstrip(".\n").split(" = "),))    # store each step as a tuple
    return parsed