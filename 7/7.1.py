testing = False

import shared

def containsBag(bags, outerBag, target):
    return outerBag == target or any(containsBag(bags, bag, target) for bag in bags[outerBag])

if testing:
    text = shared.read_input("input_test")
else:
    text = shared.read_input("input")

bags = shared.parse_rules(text)

if testing:
    print(bags)

target = "shiny gold"
part1 = sum(containsBag(bags, bag, target) for bag in bags) - 1    # remove the top-most target bag from input list of bags

print(f"Total bag colors that contain at least one shiny gold bag: {part1}")

shared.printTimeElapsed()