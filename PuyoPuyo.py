from collections import deque
from copy import deepcopy

board = []
for i in range(12):
    board.append(input())
board = list(map(list,zip(*board)))

def bfs(x,y):
    n = len(board)
    m = len(board[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    index = [(x,y)]
    while q:
        cur_x,cur_y = q.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y +dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and board[nx][ny] == board[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    cnt+=1
                    index.append((nx,ny))
    if cnt >= 4:
        for x,y in index:
            board[x][y] = '.'
        return True
    else:
        return False

def down():
    n = len(board)
    m = len(board[0])
    
    new_board = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != '.':
                new_board[i].append(board[i][j])
        new_board[i] = ['.']* (12 - len(new_board[i]))+new_board[i]
    return new_board
    
ans = 0

while True:
    n = len(board)
    m = len(board[0])
    flag = False
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != '.':
                if bfs(i,j):
                    flag = True
    if flag:
        ans += 1
        board = down()
    else:
        break
print(ans)