#!/usr/bin/python

with open("input") as f:
    data = f.read().splitlines()

valid = 0

for line in data:
    codeletter, seperator, password = line.partition(": ")
    codes, seperator, letter = codeletter.partition(" ")
    codemin, seperator, codemax = codes.partition("-")
    
    count = password.count(letter)
    if count>=int(codemin) and count<=int(codemax):
        valid += 1

print(valid)
