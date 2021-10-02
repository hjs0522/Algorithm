import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    if(heap[0] == 0 and heap[1] == 0):
        return -1
    while(heap[0] < K):
        if(len(heap) < 2):
            return -1
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)
        heapq.heappush(heap, s1+s2*2)
        answer += 1
    return answer
