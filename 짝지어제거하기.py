def solution(s):
    s = list(s)
    stack = []
    while s:
        item = s.pop()
        if(len(stack) == 0 or stack[-1] != item):
            stack.append(item)
        else:
            stack.pop()
    if(len(stack) == 0):
        return 1
    else:
        return 0
