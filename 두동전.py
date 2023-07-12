N,M = map(int,input().split())
board = []

for _ in range(N):
    board.append(list(input()))
p1_pos = (-1,-1)
p2_pos= (-1,-1)
for i in range(N):
    for j in range(M):
        if p1_pos == (-1,-1) and board[i][j] == 'o':
            p1_pos = (i,j)
        elif p1_pos != (-1,-1) and board[i][j] == 'o':
            p2_pos = (i,j)

visited = [[[[-1]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx= [-1,1,0,0]
dy = [0,0,-1,1]
from collections import deque
def bfs(p1_pos,p2_pos):
    q = deque([(p1_pos,p2_pos)])
    visited[p1_pos[0]][p1_pos[1]][p2_pos[0]][p2_pos[1]] = 0
    
    while q:
        p1_pos,p2_pos =q.popleft()
        p1_x,p1_y = p1_pos
        p2_x,p2_y = p2_pos
        if visited[p1_pos[0]][p1_pos[1]][p2_pos[0]][p2_pos[1]] >=10:
            return -1
            
        for i in range(4):
            nx1 = p1_x+dx[i]
            ny1 = p1_y+dy[i]
            nx2 = p2_x+dx[i]
            ny2 = p2_y+dy[i]
            if (0<= nx1 < N and 0<=ny1<M) and not (0<=nx2<N and 0<=ny2<M):
                return visited[p1_pos[0]][p1_pos[1]][p2_pos[0]][p2_pos[1]] + 1
            if not (0<= nx1 < N and 0<=ny1<M) and (0<=nx2<N and 0<=ny2<M):
                return visited[p1_pos[0]][p1_pos[1]][p2_pos[0]][p2_pos[1]] + 1
            if (0<= nx1 < N and 0<=ny1<M) and (0<=nx2<N and 0<=ny2<M):
                if (board[nx1][ny1] == '.' or board[nx1][ny1] == 'o') and (board[nx2][ny2] == '.' or board[nx2][ny2] == 'o'):
                    if visited[nx1][ny1][nx2][ny2] == -1:
                        visited[nx1][ny1][nx2][ny2] = visited[p1_pos[0]][p1_pos[1]][p2_pos[0]][p2_pos[1]] + 1
                        q.append(((nx1,ny1),(nx2,ny2)))
                        continue
                if (board[nx1][ny1] == '.' or board[nx1][ny1] == 'o') and board[nx2][ny2] == '#':
                    if visited[nx1][ny1][p2_pos[0]][p2_pos[1]] == -1:
                        visited[nx1][ny1][p2_pos[0]][p2_pos[1]] = visited[p1_pos[0]][p1_pos[1]][p2_pos[0]][p2_pos[1]] + 1
                        q.append(((nx1,ny1),(p2_pos[0],p2_pos[1])))
                        continue
                if (board[nx1][ny1] == '#') and (board[nx2][ny2] == '.' or board[nx2][ny2] == 'o'):
                    if visited[p1_pos[0]][p1_pos[1]][nx2][ny2] == -1:
                        visited[p1_pos[0]][p1_pos[1]][nx2][ny2] = visited[p1_pos[0]][p1_pos[1]][p2_pos[0]][p2_pos[1]] + 1
                        q.append(((p1_pos[0],p1_pos[1]),(nx2,ny2)))
                        continue
                        
    return -1
print(bfs(p1_pos,p2_pos))
                        
                    
                    