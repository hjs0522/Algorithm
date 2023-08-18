def solution(prices):
    n = len(prices)
    answer = [n-i-1 for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if prices[i]<=prices[j]:
                continue
            else:
                answer[i] = j-i
                break
    return answer