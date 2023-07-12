import sys
import heapq

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A,B,C = map(int,sys.stdin.readline().split())
    graph[A-1].append([B-1,C])
    graph[B-1].append([A-1,C])


def dijskstra(start):
    distance = [int(1e9)]*(N)
    distance[start] = 0
    pq = []
    heapq.heappush(pq,[0,start])
    while pq:
        cur_cost,cur_node = heapq.heappop(pq)
        
        if distance[cur_node] < cur_cost:
            continue
        
        for next_node, next_cost in graph[cur_node]:
            if distance[next_node] > cur_cost + next_cost:
                distance[next_node] = cur_cost + next_cost
                heapq.heappush(pq,[cur_cost+next_cost,next_node])
    return distance

distance = dijskstra(1)
    
dp = [0]*N
dp[1] = 1

def path(cur_node):
    if dp[cur_node] == 0:
        for next_node,next_cost in graph[cur_node]:
            if distance[cur_node] > distance[next_node]:
                dp[cur_node] += path(next_node)
        return dp[cur_node]
    else:
        return dp[cur_node]
        
print(path(0))