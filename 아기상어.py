from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

#상어의 위치 저장
pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0

def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    queue = deque([[x,y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ii, jj = i + dx[idx] , j + dy[idx]
            
            if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
                #물고기를 먹는 경우
                if space[x][y] > space[ii][jj] and space[ii][jj] != 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    #이동횟수,좌표 저장
                    cand.append((visited[ii][jj] - 1, ii, jj))
                #지나가는 경우
                elif space[x][y] == space[ii][jj] or space[ii][jj] == 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
    #가장 가까운 물고기, 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기 순으로 저장
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))[0] if cand else []


i, j = pos
size = [2, 0]
while True:
    space[i][j] = size[0]
    cand = bfs(i,j)
    if not cand:
        break
        
    step, xx, yy = cand
    cnt += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[i][j] = 0
    i, j = xx, yy
        
print(cnt)