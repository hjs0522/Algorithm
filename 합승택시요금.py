def solution(n, s, a, b, fares):
    answer = float("inf")

    distance = [[float("inf") for i in range(n+1)]for j in range(n+1)]

    for e1, e2, cost in fares:
        distance[e1][e2] = cost
        distance[e2][e1] = cost

    # 플로이드 와샬 알고리즘 사용
    for k in range(1, n+1):
        distance[k][k] = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                distance[i][j] = distance[j][i] = min(
                    distance[i][j], distance[i][k] + distance[k][j])

    for i in range(1, n+1):
        answer = min(answer, distance[s][i] + distance[i][a] + distance[i][b])
    return answer
