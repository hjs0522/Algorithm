from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(input())
visited = [[[[False]* m for _ in range(n)]for _ in range(m)]for _ in range(n)]
q = deque()
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def init():
    ry,rx,by,bx = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                ry,rx = i,j
                continue
            if graph[i][j] == 'B':
                by,bx = i,j
                continue
    q.append((ry,rx,by,bx,1))
    visited[ry][rx][by][bx] = True

def move(y,x,dy,dx):
    count = 0
    while graph[y+dy][x+dx] != '#' and graph[y][x] != 'O':
        x+=dx
        y+=dy
        count+=1
    return y,x,count

def bfs():
    init()
    while q:
        ry,rx,by,bx,depth = q.popleft()
        if depth > 10:
            print(-1)
            return
        for i in range(4):
            next_ry,next_rx,r_count = move(ry,rx,dy[i],dx[i])
            next_by,next_bx,b_count = move(by,bx,dy[i],dx[i])
            if graph[next_by][next_bx] == 'O':
                continue
            if graph[next_ry][next_rx] == 'O':
                print(depth)
                return
            if next_ry == next_by and next_rx == next_bx:
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
                    
            if not visited[next_ry][next_rx][next_by][next_bx]:
                q.append((next_ry,next_rx,next_by,next_bx,depth+1))
                visited[next_ry][next_rx][next_by][next_bx] = True
    print(-1)
bfs()                