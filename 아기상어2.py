N,M =map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

shark = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            shark.append((i,j))

from collections import deque
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]
def bfs(x,y):
    visitied = [[-1]*M for _ in range(N)]
    q = deque([(x,y)])
    visitied[x][y] = 0
    
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(8):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visitied[nx][ny] == -1:
                    visitied[nx][ny] = visitied[cur_x][cur_y] +1
                    q.append((nx,ny))
    
    res = int(1e9)
    for s_x,s_y in shark:
        res = min(visitied[s_x][s_y],res)
    return res
ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans,bfs(i,j))
print(ans)

        
    