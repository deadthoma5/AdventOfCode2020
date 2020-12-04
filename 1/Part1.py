#!/usr/bin/python

with open("input") as f:
    data = f.read().splitlines()
    for x, left in enumerate(data):
        for y, right in enumerate(data):
            if x == y:
                continue
            sum = int(left) + int(right)
            if sum == 2020:
                print("sum of " + left + " and " + right + ": " + str(sum))
                product = int(left) * int(right)
                print("their product is: " + str(product))
