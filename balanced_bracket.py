def balancedBrackets(str):
    stack = []
    for c in str:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' or c == '}' or c == ']':
            if(len(stack) == 0):
                return False
            top = stack.pop()
            if not comapareBrackets(top, c):
                return False

    if(len(stack) != 0):
        return False
    return True


def comapareBrackets(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '{' and closing == '}':
        return True
    if opening == '[' and closing == ']':
        return True
    return False
val = input("enter the value:")
print(balancedBrackets(val))