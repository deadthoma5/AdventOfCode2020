#!/usr/bin/python

with open("input") as f:
    data = f.read().splitlines()
    for x, first in enumerate(data):
        for y, second in enumerate(data):
            for z, third in enumerate(data):
                if x==y or y==z or x==z:
                    continue
                sum = int(first) + int(second) + int(third)
                if sum == 2020:
                    print("sum of " + first + " and " + second + " and " + third + ": " + str(sum))
                    product = int(first) * int(second) * int(third)
                    print("their product is: " + str(product))
