def solution(number, k):
    answer = ''
    stack = []
    number = list(number)
    number = map(int,number)
    for num in number:
        while k>0 and stack and num>stack[-1]:
                k-=1
                stack.pop()
        stack.append(num)
    while k>0:
        stack.pop()
        k-=1
    stack = map(str,stack)
    return ''.join(stack)
print(solution("1924",2))