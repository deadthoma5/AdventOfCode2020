testing = False

# Reference for infix/prefix/postfix calculations:
# https://sites.google.com/site/advancedpythonprogramming/basic-data-structures/infix-prefix-and-postfix-expressions

import shared

def fix_parenthesis(text):
    if type(text) == str:
        text = text.replace('(', '( ')
        text = text.replace(')', ' )')
        return text
    else:
        newText = []
        for line in text:
            line = line.replace('(', '( ')
            line = line.replace(')', ' )')
            newText.append(line)
        return newText

if testing:
    text = shared.read_input("input_test")
    print(f"Instructions: {text}")
else:
    text = shared.read_input("input")

text = fix_parenthesis(text)

# infix to postfix conversion from Reference
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 2    # changed priority of */ to same as +-. Was originally 3.
    prec["/"] = 2    # changed priority of */ to same as +-. Was originally 3.
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

# postfix evaluation from Reference
from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# Part 1
part1 = 0
if testing:
    part1 += postfixEval(infixToPostfix(text))
else:
    for line in text:
        part1 += postfixEval(infixToPostfix(line))
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
