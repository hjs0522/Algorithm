from collections import deque
r,c,t = map(int,input().split())
board = []
for _ in range(r):
    board.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def spread(x1,y1,x2,y2):
    temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                cnt = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if nx == x1 and ny ==y1:
                        continue
                    if nx == x2 and ny == y2:
                        continue
                    if 0<=nx<r and 0<=ny<c:
                        cnt+=1
                        temp[nx][ny] += board[i][j]//5
                temp[i][j] += board[i][j] - board[i][j]//5*cnt
    temp[x1][y1] = -1
    temp[x2][y2] = -1
    return temp
def up_cycle(x,y):
    q = deque()
    q.append(board[x][y])
    for i in range(y+1,c-1):
        q.append(board[x][i])
        board[x][i] = q.popleft()
    for i in range(x,0,-1):
        q.append(board[i][c-1])
        board[i][c-1] = q.popleft()
    for i in range(c-1,0,-1):
        q.append(board[0][i])
        board[0][i] = q.popleft()
    for i in range(x):
        q.append(board[i][0])
        board[i][0] = q.popleft()
    board[x][y] = -1
    board[x][y+1] = 0
    
def down_cycle(x,y):
    q = deque()
    q.append(board[x][y])
    for i in range(y+1,c-1):
        q.append(board[x][i])
        board[x][i] = q.popleft()
    for i in range(x,r-1):
        q.append(board[i][c-1])
        board[i][c-1] = q.popleft()
    for i in range(c-1,0,-1):
        q.append(board[r-1][i])
        board[r-1][i] = q.popleft()
    for i in range(r-1,x,-1):
        q.append(board[i][0])
        board[i][0] = q.popleft()
    board[x][y] = -1
    board[x][y+1] = 0

x1,x2 =0,0
for i in range(r):
    if board[i][0] == -1:
        x1 = i
        x2 = i+1
        break

while(t):
    t-=1
    board = spread(x1,0,x2,0)
    up_cycle(x1,0)
    down_cycle(x2,0)
ans = 0
for i in range(r):
    for j in range(c):
        if board[i][j] !=0 and board[i][j] !=-1:
            ans+=board[i][j]
print(ans)

