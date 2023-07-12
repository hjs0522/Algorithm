from copy import deepcopy
data = list(input().split(" "))
for i in range(1,len(data)):
    stack = []
    alpha = ''
    for j in range(len(data[i])):
        if data[i][j].isalpha():
            alpha += data[i][j]
            continue
        
        if data[i][j] == '*' or data[i][j] == '&' or data[i][j] == '['or data[i][j] == ']':
            stack.append(data[i][j])
            
    temp = deepcopy(data[0])
    stack.reverse()
    for s in stack:
        if s == '[':
            temp+= ']'
        elif s == ']':
            temp+= '['
        else:
            temp += s
    temp += ' '
    temp+= alpha
    temp += ';'
    print(temp)