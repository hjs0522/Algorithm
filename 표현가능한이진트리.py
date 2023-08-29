def getLength(n):
    length = 1
    while 2**length-1<n:
        length += 1
    return 2**length -1
flag = True
def check(num):
    global flag
    if len(num)<3 or '1' not in num or '0' not in num:
        return
    mid = len(num)//2
    if num[mid] == '0':
        flag = False
        return
    check(num[:mid])
    check(num[mid+1:])
def solution(numbers):
    global flag
    answer = []
    for number in numbers:
        num = bin(number)[2:]
        num = (getLength(len(num))-len(num))*'0'+num
        check(num)
        if flag:
            answer.append(1)
        else:
            answer.append(0)
        flag = True
    return answer


print(solution([7, 42, 5]))