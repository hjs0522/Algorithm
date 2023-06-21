N = int(input())
visited = [[int(1e9)]*(N+1) for _ in range(N+1)]

from collections import deque

q = deque([(1,0)])
visited[1][0] = 0
while q:
    screen, clip = q.popleft()
    if visited[screen][screen] ==  int(1e9):
        visited[screen][screen] = visited[screen][clip] +1
        q.append((screen,screen))
    if screen+clip<=N and visited[screen+clip][clip] == int(1e9):
        visited[screen+clip][clip] = visited[screen][clip]+1
        q.append((screen+clip,clip))
    if screen -1 >0 and visited[screen-1][clip] == int(1e9):
        visited[screen-1][clip] = visited[screen][clip] +1
        q.append((screen-1,clip))

answer = int(1e9)
for i in range(N+1):
    answer = min(answer,visited[N][i])
print(answer)