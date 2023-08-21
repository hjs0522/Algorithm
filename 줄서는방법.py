def factorial(num):
    temp = 1
    for i in range(1,num+1):
        temp*=i
    return temp
def solution(n, k):
    answer = []
    num = [i for i in range(1,n+1)]
    while n!= 0:
        temp = factorial(n-1)
        idx = k//temp
        k = k% temp
        if k==0:
            answer.append(num.pop(idx-1))
        else:
            answer.append(num.pop(idx))
        n-=1
    return answer