"""
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

def evaluate(expression):
    stack = []
    while expression:
        val = expression.pop(0)
        if (str(val) == "+" or str(val) == "*" or
                str(val) == "-" or str(val) == "/"):
            x, y = stack.pop(), stack.pop()
            stack.append(eval("{0}{1}{2}".format(y, val, x)))
        else:
            stack.append(val)
    return stack[0]

print evaluate(["2", "1", "+", "3", "*"])
print evaluate(["4", "13", "5", "/", "+"])