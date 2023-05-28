from collections import deque
n,m = map(int,input().split())
y,x,d = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
dy = [-1,0,1,0]
dx = [0,1,0,-1]
visited = [[False]*m for _ in range(n)]

visited[y][x] = True
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3)%4
        ny = y + dy[d]
        nx = x + dx[d]
        
        if 0 <= ny < n and 0<= nx <m and board[ny][nx] == 0:
            if visited[ny][nx] == False:
                visited[ny][nx] = True
                cnt+=1
                y = ny
                x = nx
                flag = 1
                break
    if flag == 0:
        if board[y-dy[d]][x-dx[d]] == 1:
            print(cnt)
            break
        else:
            y,x = y-dy[d],x-dx[d]