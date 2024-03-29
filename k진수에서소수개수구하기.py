def convert(num,base):
    temp = '0123456789ABCDEF'
    q,r = divmod(num,base)
    if q == 0:
        return temp[r]
    else:
        return convert(q,base)+temp[r]

def isPrime(num):
    if num <2:
        return False
    for i in range(2,int((num)**0.5)+1):
        if num%i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    number = convert(n,k)
    number = number.split('0')
    for num in number:
        num = int(num)
        if isPrime(num):
            answer+=1
    return answer
n,k = map(int,input().split())
print(solution(n,k))