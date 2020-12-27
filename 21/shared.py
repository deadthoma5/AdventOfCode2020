from time import time

_startTime = None

def read_input(filename):
    global _startTime
    
    with open(filename) as f:
        #data = [line.strip() for line in f]
        data = f.read().split('\n\n')

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