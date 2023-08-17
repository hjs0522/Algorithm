#h번 이상 인용된 논문이 h개 이상이고 나머지 논문이 h번이하라면 h의 최댓값이 h-index
from bisect import bisect_left,bisect_right
def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse = True)
    for h in range(n,-1,-1):
        position = bisect_right([-c for c in citations],-h)
        if position >=h and n - position <=h:
            return h
    return answer

print(solution([3, 0, 3, 6, 1, 5]))