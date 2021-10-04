def check(stones, k, mid):
    cnt = 0
    for stone in stones:
        if stone < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True


def solution(stones, k):
    answer = 0
    r = max(stones) + 1
    l = 1
    while(l < r - 1):
        mid = (r+l)//2
        if check(stones, k, mid):
            l = mid
        else:
            r = mid
    return l

    return answer
