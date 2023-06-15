n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split(" "))))

virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i,j))

from itertools import combinations
from collections import deque
combi = list((combinations(virus,m)))
from copy import deepcopy

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = int(1e9)
for com in combi:
    flag = True
    temp = deepcopy(board)
    checked = [[-1]*n for _ in range(n)]
    q = deque()
    for x,y in com:
        q.append((x,y,0))
        checked[x][y] = 0
    while q:
        x,y,t = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n or temp[nx][ny]==1:
                continue
            if checked[nx][ny] == -1:
                q.append((nx,ny,t+1))
                if temp[nx][ny] == 2:
                    temp[nx][ny] = 3
                    checked[nx][ny] = 0
                    continue
                temp[nx][ny] = 3
                checked[nx][ny] = t+1
    res = -1                
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == False:
        res = int(1e9)
    else:
        for i in range(n):
            for j in range(n):
                res = max(res,checked[i][j])
    ans = min(res,ans)
if ans == int(1e9):
    print(-1)
else:
    print(ans)