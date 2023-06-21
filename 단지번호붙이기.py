from collections import deque
N = int(input())
board = []
checked = [[False]*N for _ in range(N)]
for _ in range(N):
    board.append(list(map(int,input())))
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
            if 0<=nx<N and 0<=ny<N:
                if checked[nx][ny] == False and board[nx][ny] == 1:
                    q.append((nx,ny))
                    checked[nx][ny] = True
                    cnt+=1
                    
                    
    return cnt
    
ans = []
for i in range(N):
    for j in range(N):
        if checked[i][j] == False and board[i][j] == 1:
            ans.append(bfs(i,j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)