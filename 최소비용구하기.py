n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
distance = [int(1e9)]*(n+1)
for _ in range(m):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))
import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        now_distance,now_idx = heapq.heappop(q)
        if now_distance > distance[now_idx]:
            continue
        for idx,cost in graph[now_idx]:
            if distance[idx] > now_distance + cost:
                distance[idx] = now_distance+cost
                heapq.heappush(q,(distance[idx],idx))
start,end = map(int,input().split())
dijkstra(start)
print(distance[end])