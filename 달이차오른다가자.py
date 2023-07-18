from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(x,y):
    q = deque([(x,y,0,0)])
    check = [[[False]*(1<<6) for _ in range(50)]for _ in range(50)]
    check[x][y][0] = True
    
    while q:
        x,y,cnt,key = q.popleft()
        if board[x][y] == '1': return cnt
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0>nx or nx>=N or 0>ny or ny>=M or check[nx][ny][key]:
                continue
            #현재 칸이 이동할 수 있는 경우
            if board[nx][ny] == '1' or board[nx][ny] == '.':
                check[nx][ny][key] = True
                q.append((nx,ny,cnt+1,key))
            #현재 칸에 열쇠가 있는 경우
            elif 'a'<= board[nx][ny] <= 'f':
                tmp_key = key | (1<<(ord(board[nx][ny])-ord('a')))
                check[nx][ny][tmp_key] = True
                q.append((nx,ny,cnt+1,tmp_key))
            elif 'A'<=board[nx][ny]<='F':
                if key & (1<< (ord(board[nx][ny]) - ord('A'))):
                    check[nx][ny][key] = True
                    q.append((nx,ny,cnt+1,key))


N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            sx,sy = i,j
            board[i][j] = '.'
print(bfs(sx,sy))
    