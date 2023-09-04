from collections import defaultdict
from heapq import heappop,heappush

def solution(n, paths, gates, summits):
    def get_min_intensity():
        pq = []
        visited = [10000001]*(n+1)

        for gate in gates:
            heappush(pq,(0,gate))
            visited[gate] = 0

        while pq:
            intensity, node = heappop(pq)

            if node in summits_set or intensity > visited[node]:
                continue

            for weight, next_node in graph[node]:
                new_intensity = max(intensity,weight)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(pq,(new_intensity,next_node))
        min_intensity = [0,10000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
        return min_intensity

    summits.sort()
    summits_set= set(summits)
    graph = defaultdict(list)
    for i,j,w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))

    return get_min_intensity()
print(solution(6,[[1, 2, 3],[2, 3, 5],[2, 4, 2],[2, 5, 4],[3, 4, 4],[4, 5, 3],[4, 6, 1],[5, 6, 1]],[1,3],[5]))