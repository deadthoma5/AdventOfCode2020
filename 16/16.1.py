testing = False

import shared
import re

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

def split_rules(rules):
    newRules = []
    for rule in rules:
        match = re.findall(r'([a-z]+)(: )(\d+)(-)(\d+)( or )(\d+)(-)(\d+)', rule)[0]
        newRule = (match[0], int(match[2]), int(match[4]), int(match[6]), int(match[8]))
        newRules.append(newRule)
    return newRules

def split_input(text):
    splits = [i for i, x in enumerate(text) if x == ""]
    rules = text[:splits[0]]
    rules = split_rules(rules)
    myTicket = tuple(map(int, text[splits[0]+2:splits[1]][0].split(',')))
    nearbyTickets = text[splits[1]+2:]
    nearbyTickets = [ticket.split(',') for ticket in nearbyTickets]
    nearbyTickets = [tuple(map(int, ticket)) for ticket in nearbyTickets]
    return rules, myTicket, nearbyTickets

def check_rule(rule, x):
    if testing:
        print(f"checking if {x} is between {rule[1]}-{rule[2]} or {rule[3]}-{rule[4]}")
    if ((x >= rule[1]) and (x <= rule[2])) or ((x >= rule[3]) and (x <= rule[4])):
        if testing:
            print("true")
        return True
    else:
        if testing:
            print("false")
        return False

def validate(rules, ticket):
    if testing:
        for x in ticket:
            print(f"validating ticket value {x}, any rules: {any(check_rule(rule, x) for rule in rules)}")
    for x in ticket:
        if any(check_rule(rule, x) for rule in rules):
            continue
        else:
            return x
    return 0

# Part 1
part1 = 0
rules, myTicket, nearbyTickets = split_input(text)
if testing:
    print(f"rules: {rules}, myticket: {myTicket}, nearbyTickets: {nearbyTickets}")
for ticket in nearbyTickets:
    if testing:
        print(f"processing ticket: {ticket}, invalid number: {validate(rules, ticket)}")
    part1 += validate(rules, ticket)
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
