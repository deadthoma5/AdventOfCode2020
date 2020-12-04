#!/usr/bin/python

with open("input") as f:
    data = f.read().splitlines()

valid = 0

for line in data:
    codeletter, seperator, password = line.partition(": ")
    codes, seperator, letter = codeletter.partition(" ")
    codemin, seperator, codemax = codes.partition("-")
    codemin = int(codemin)
    codemax = int(codemax)

    if (password[codemin-1]==letter or password[codemax-1]==letter) and (password[codemin-1] != password[codemax-1]):
        valid += 1 
    else:
        continue

print(valid)
