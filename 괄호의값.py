data = input()
stack = []
stack_level = [[] for _ in range(len(data)+1)]
for d in data:
    if d == '(':
        stack.append('(')
    elif d == '[':
        stack.append('[')
    else:
        if stack:
            if stack[-1] == '(' and d == ')':
                stack.pop()
                value = 1
                if stack_level[len(stack)+1]:  
                    value = sum(stack_level[len(stack)+1])
                    stack_level[len(stack)+1] = []
                stack_level[len(stack)].append(value*2)
            elif stack[-1] == '[' and d == ']':
                stack.pop()
                value = 1
                if stack_level[len(stack)+1]:  
                    value = sum(stack_level[len(stack)+1])
                    stack_level[len(stack)+1] = []
                stack_level[len(stack)].append(value*3)
        else:
            stack.append(0)
            break
    
if stack:
    print(0)
else:
    print(sum(stack_level[0]))