from collections import deque
def bfs(maps,start_x,start_y,target_x,target_y):
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[int(1e9)]*m for _ in range(n)]
    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = 0
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            nx = cur_x +dx[i]
            ny = cur_y + dy[i]
            if 0>nx or nx>=n or 0>ny or ny>=m or visited[nx][ny] != int(1e9):
                continue
            if maps[nx][ny] != 'X': 
                q.append((nx,ny))
                visited[nx][ny] = visited[cur_x][cur_y]+1
    return visited[target_x][target_y]
    
    
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    start_x,start_y,lever_x,lever_y,final_x,final_y = -1,-1,-1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if maps[i][j] =='S':
                start_x,start_y = i,j
                continue
            if maps[i][j] == 'L':
                lever_x,lever_y = i,j
                continue
            if maps[i][j] =='E':
                final_x,final_y = i,j
                continue
    answer+= bfs(maps,start_x,start_y,lever_x,lever_y)
    answer+= bfs(maps,lever_x,lever_y,final_x,final_y)
    if answer >= int(1e9):
        return -1
    return answer