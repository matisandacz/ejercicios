def solution(s):
    for symbol in s:
        if symbol in  ['(', '[', '{']:
            stack.add(symbol)
        elif symbol in [')', ']', '}']:
            last = stack.pop()
            if symbol == ')' and last != '(' or symbol == ']' and last != '[' or symbol == '}' and last != '{':
                return False
        else:
            pass
    return len(stack) == 0
