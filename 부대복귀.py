from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    q = deque([destination])
    board = [[] for _ in range(n+1)]
    for r in roads:
        board[r[0]].append(r[1])
        board[r[1]].append(r[0])
    visited = [-1]*(n+1)
    visited[destination] = 0
    while q:
        cur = q.popleft()
        for i in board[cur]:
            if visited[i] == -1:
                visited[i] = visited[cur] + 1
                q.append(i)
    for s in sources:
        answer.append(visited[s])
    return answer