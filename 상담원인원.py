#n:멘토, 1~k: 상담유형, 
#기다린 시간 = 참가자 상담 요청시작~상담 시작
#기다린 시간의 합이 최소가 되도록 각 상담 유형별로 멘토 인원을 정해 기다린 시간의 합의 최솟값을 반환
import heapq
from itertools import combinations_with_replacement
def solution(k, n, reqs):
    answer = int(1e9)
    time = [[int(1e9) for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,n+1):
            wait_time = 0
            q = []
            for a,b,c in reqs:
                if c == i:
                    if len(q)<j:
                        heapq.heappush(q,a+b)
                    else:
                        temp = heapq.heappop(q)
                        if a<temp:
                            wait_time += temp-a
                        heapq.heappush(q,max(a+b,temp+b))
            time[i][j] = wait_time
    combi = list(combinations_with_replacement([i for i in range(1,k+1)],n-k))
    for c in combi:
        temp = [1 for _ in range(k+1)]
        for i in c:
            temp[i] += 1
        wait_time = 0
        for i in range(1,k+1):
            wait_time += time[i][temp[i]]
        answer = min(answer,wait_time)
        
            
                    
        
    return answer