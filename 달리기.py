N,M,K = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(input()))

x1,y1,x2,y2 = map(int,input().split())

visited = [[-1]* M for _ in range(N)]
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque([(x1-1,y1-1)])
visited[x1-1][y1-1] = 0
while q:
    cur_x,cur_y = q.popleft()
    for i in range(4):
        for j in range(1,K+1):
            nx = cur_x+dx[i]*j
            ny = cur_y+dy[i]*j
            if nx<0 or nx>=N or ny<0 or ny>=M or board[nx][ny] == '#':
                break
            
            if visited[nx][ny] != -1 and visited[nx][ny] <=visited[cur_x][cur_y]:
                break
            
            if visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[cur_x][cur_y] +1
            q.append((nx,ny))

print(visited[x2-1][y2-1])