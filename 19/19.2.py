testing = False

import shared
from lark import Lark, LarkError

if testing:
    rules, messages = shared.read_input("input_test")
    print(f"Rules:\n{rules}")
    print(f"Messages:\n{messages}")
else:
    rules, messages = shared.read_input("input")

def solve(rules, messages):
    rules = rules.translate(str.maketrans('0123456789', 'abcdefghij'))
    parser = Lark(rules, start='a')
    match = 0
    for line in messages.splitlines():
        try:
            parser.parse(line)
            match += 1
        except LarkError:
            pass
    return match

# Part 2
rules = rules.replace('8: 42', '8: 42 | 42 8')
rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
part2 = solve(rules, messages)
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
