from itertools import permutations


def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2, int((n**0.5))+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    # 소수의 길이는 1부터 numbers의 길이와 같은 수까지 될수 있음
    for i in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(perlist)):
            if(isPrime(j)):
                answer.append(int(j))
    answer = len(set(answer))
    return answer
