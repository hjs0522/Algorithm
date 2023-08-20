import heapq
def dijkstra(start,distance,graph):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
def solution(N, road, K):
    answer = 1
    distance = [int(1e9)]*(N+1)
    graph = [[]for i in range(N+1)]
    for start,end,cost in road:
        graph[start].append((end,cost))
        graph[end].append((start,cost))
    dijkstra(1,distance,graph)
    for i in range(2,len(distance)):
        if distance[i] <=K:
            answer+=1
    return answer