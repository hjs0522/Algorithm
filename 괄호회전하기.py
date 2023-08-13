def check(s):
    stack = []
    dic = {')':'(',']':'[','}':'{'}
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i in dic and dic[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    return 1 if len(stack) == 0 else 0
        
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s):
            answer+=1
        s = s[1:] + s[:1]
    return answer
print(solution('[](){}'))