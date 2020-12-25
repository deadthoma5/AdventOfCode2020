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

# Part 1
part1 = solve(rules, messages)
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
