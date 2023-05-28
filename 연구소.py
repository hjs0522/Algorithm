from collections import deque
import copy
n, m = map(int,input().split(" "))
board = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(n):
    board.append(list(map(int,input().split())))

ans = 0

def bfs():
    q = deque()
    visited = [[False]*m for _ in range(n)]
    temp = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i,j))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >=0 and ny <n and nx >=0 and nx <m and visited[ny][nx] == False:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 2
                    q.append((ny,nx))
                    visited[ny][nx] = True
    cnt = 0
    global ans
    for i in range(n):
        cnt+= temp[i].count(0)
    ans = max(ans,cnt)
    
def makeWall(cnt):
    if cnt ==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(cnt+1)
                board[i][j] = 0

makeWall(0)
print(ans)
        
    