from collections import deque
def bfs(start_x,start_y,maps,visited):
    n = len(maps)
    m = len(maps[0])
    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    result = int(maps[start_x][start_y])
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny] != 0:
                continue
            if maps[nx][ny] != 'X':
                q.append((nx,ny))
                visited[nx][ny] = 1
                result += int(maps[nx][ny])
    return result
                    

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] ==0:
                answer.append(bfs(i,j,maps,visited))
    return answer
                    

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))