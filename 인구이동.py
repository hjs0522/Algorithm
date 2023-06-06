from collections import deque

n,l,r = map(int,input().split())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    temp = []
    q.append((a,b))
    temp.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] ==0:
                if l<=abs(board[nx][ny] - board[x][y])<=r:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    temp.append((nx,ny))
    return temp

ans = 0
while 1:
    visited = [[0]*(n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                if len(country) > 1:
                    flag = 1
                    number = sum([board[x][y] for x,y in country])//len(country)
                    for x,y in country:
                        board[x][y] = number
    if flag ==0:
        break
    ans+=1
print(ans)