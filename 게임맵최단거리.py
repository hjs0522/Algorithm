from collections import deque

def solution(maps):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    m = len(maps)
    n = len(maps[0])
    
    graph = [[-1 for i in range(n)]for j in range(m)]
    
    queue = deque()
    queue.append([0,0])
    
    graph[0][0] = 1
    
    while queue:
        y,x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny,nx])
                    
    answer = graph[-1][-1]
    return answer