def solution(n, *args):
    for element in args:
        stack.add(element)
    
    while(len(stack) != 0):
        print(stack.pop())