N,M,K = map(int,input().split())
board = [[0]*M for _ in range(N)]
checked = [[False]*M for _ in range(N)]

for _ in range(K):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1

from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque([(x,y)])
    checked[x][y] = True
    cnt = 1
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0<=nx<N and 0<=ny<M:
                if checked[nx][ny] == False  and board[nx][ny] == 1:
                    q.append((nx,ny))
                    checked[nx][ny] = True
                    cnt+=1
    return cnt
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            ans= max(ans,bfs(i,j))
print(ans)