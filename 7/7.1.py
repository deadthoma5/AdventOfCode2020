import shared

testing = True

if testing:
    text = shared.read_input("input_test")
else:
    text = shared.read_input("input")

rules = shared.parse_rules(text)

if testing:
    print(rules)

count_gold = 0
sum = 0

def get_contents(color):
    global count_gold
    if rules[color]:
        if color == 'shiny gold':
            count_gold += 1
        for contents_color, quantity in rules[color].items():
            for index in range(quantity):
                get_contents(contents_color)
    else:
        return
    
    return rules[color]

for color in rules:
    count_gold = 0
    get_contents(color)
    if (color != "shiny gold") and (count_gold > 0):
        sum += 1

print(f"Total bag colors that contain at least one shiny gold bag: {sum}")

shared.printTimeElapsed()

# expected answer for part 1 = 326