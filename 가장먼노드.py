from collections import deque


def solution(n, edge):
    answer = 0
    queue = deque()
    queue.appendleft(1)
    dist = [0]*(n+1)

    """가중치가 없으므로 가장 처음 방문하였을때가 최소 거리이다. 따라서 CHECKED를 이용하여
    한번 방문 한것은 다시 방문 하지 않도록 하였다"""
    checked = [False] * (n+1)
    checked[1] = True

    """인접리스트 방법 사용"""
    vertex = [[]for i in range(n+1)]
    for e in edge:
        vertex[e[0]].append(e[1])
        vertex[e[1]].append(e[0])

    while queue:
        start = queue.popleft()
        for v in vertex[start]:
            if checked[v] == False:
                queue.append(v)
                checked[v] = True
                dist[v] = dist[start]+1

    max_dist = max(dist)
    for d in dist:
        if d == max_dist:
            answer += 1

    return answer
