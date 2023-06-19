N,M,fuel = map(int,input().split())
graph = []

#지도
for i in range(N):
    graph.append(list(map(int,input().split())))

#택시 위치
position_x,positoin_y = map(int,input().split())
position_x -=1
positoin_y -=1
user_start = []
user_end = []
#출발 행,열 도착 행,열
for i in range(M):
    data = list(map(int,input().split()))
    user_start.append([data[0]-1,data[1]-1])
    user_end.append([data[2]-1,data[3]-1])

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs(start_x,start_y):
    distance = [[0]*N for _ in range(N)]
    q = deque([(start_x,start_y)])
    minDistance = int(1e9)
    candidate = []
    while q:
        x,y = q.popleft()
        if minDistance < distance[x][y]:
            break
        if [x,y] in user_start:
            minDistance = distance[x][y]
            candidate.append((x,y))
            continue
            
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
                if distance[nx][ny] == 0:
                    q.append((nx,ny))
                    distance[nx][ny] = distance[x][y]+1
    if candidate:
        candidate.sort()
        return distance[candidate[0][0]][candidate[0][1]],candidate[0][0],candidate[0][1]
    else:
        return -1,-1,-1
def go_destination(start_x,start_y,end_x,end_y):
    distance = [[0]*N for _ in range(N)]
    q = deque([(start_x,start_y)])
    while q:
        x,y = q.popleft()
        if x== end_x and y == end_y:
            return distance[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
                if distance[nx][ny] == 0:
                    q.append((nx,ny))
                    distance[nx][ny] = distance[x][y]+1
    return -1



    
for _ in range(M):
    distance,x,y = bfs(position_x,positoin_y)
    if distance == -1 or fuel <distance:
        fuel = -1
        break
    
    fuel -= distance
    idx = user_start.index([x,y])
    user_start[idx] = [-1,-1]
    distance2 = go_destination(x,y,user_end[idx][0],user_end[idx][1])
    if distance2 == -1 or fuel < distance2:
        fuel = -1
        break
    fuel += distance2
    position_x,positoin_y = user_end[idx][0],user_end[idx][1]
print(fuel)