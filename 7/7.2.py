testing = False

import shared

def countBags(bags, outerBag):
    return sum(quantity * (countBags(bags, bag) + 1) for bag, quantity in bags[outerBag].items())

if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input_test2")
else:
    text = shared.read_input("input")

bags = shared.parse_rules(text)

if testing:
    print(bags)

target = "shiny gold"
part2 = 0
part2 = countBags(bags, target)
print(f"Individual bags required inside single {target} bag: {part2}")

shared.printTimeElapsed()