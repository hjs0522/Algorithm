M,N = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(input()))

from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
checked = [[False]*M for _ in range(N)]
def bfs(x,y,value):
    q = deque([(x,y)])
    checked[x][y] = True
    cnt = 1
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if checked[nx][ny] == False and board[nx][ny] == value:
                    q.append((nx,ny))
                    checked[nx][ny] = True
                    cnt+=1
    return cnt**2

b_score = 0
w_score = 0
for i in range(N):
    for j in range(M):
        if checked[i][j]:
            continue
        if board[i][j] == 'W':
            w_score += bfs(i,j,'W')
            continue
        if board[i][j] == 'B':
            b_score += bfs(i,j,'B')
            continue
print(w_score,b_score)