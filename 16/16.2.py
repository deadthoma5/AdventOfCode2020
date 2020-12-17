testing = False

import shared
import re

if testing:
    text = shared.read_input("input_test2")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

def split_rules(rules):
    newRules = []
    for rule in rules:
        match = re.findall(r'([a-z ]+)(: )(\d+)(-)(\d+)( or )(\d+)(-)(\d+)', rule)[0]
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
        print(f"checking if {x} against rule: {rule}")
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

def map_rules(rules, validTickets):
    mapping = dict()
    options = dict()
    for rule in rules:
        options[rule] = []
        for i in range(len(validTickets[0])):
            if all(check_rule(rule, ticket[i]) for ticket in validTickets):
                options[rule].append(i)
    if testing:
        print(f"possible options: {options}")
    while options:
        todo = options.copy()
        for rule in todo:
            if len(options[rule]) == 1:
                pos = options[rule][0]
                mapping[rule] = pos
                options.pop(rule)
                for r in options:
                    options[r].remove(pos)
    return mapping

def get_dep_rules(rules):
    depRules = []
    for rule in rules:
        if rule[0].startswith("departure"):
            depRules.append(rule)
    return depRules

# Part 2
validTickets = []
rules, myTicket, nearbyTickets = split_input(text)
if testing:
    print(f"rules: {rules}, myticket: {myTicket}, nearbyTickets: {nearbyTickets}")
for ticket in nearbyTickets:
    if testing:
        print(f"processing ticket: {ticket}, invalid number: {validate(rules, ticket)}")
    if validate(rules, ticket) == 0:
        validTickets.append(ticket)
if testing:
    print(f"valid tickets: {validTickets}")
if testing:
    print(f"-- finding mappings -- ")
mapping = map_rules(rules, validTickets)
if testing:
    print(f"mapping: {mapping}")
if testing:
    testRules = rules
else:
    depRules = get_dep_rules(rules)
    testRules = depRules
if testing:
    print(f"testing rules mappings: {testRules} against myTicket: {myTicket}")
part2 = 1
for rule in testRules:
    part2 *= myTicket[mapping[rule]]
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
