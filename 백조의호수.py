from collections import deque

R,C = map(int,input().split())
board = []

for _ in range(R):
    board.append(list(input()))

swan_q1,swan_q2 = deque(),deque()
water_q1,water_q2 = deque(),deque()
swan_visited = [[0]*C for _ in range(R)]
water_visited = [[0]*C for _ in range(R)]
target_x,target_y= -1,-1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            if not swan_q1:
                swan_q1.append((i,j))
                swan_visited[i][j] = 1
            else:
                target_x,target_y = i,j
            board[i][j] = '.'
        
        if board[i][j] == '.':
            water_q1.append((i,j))
            water_visited[i][j] =1
        

def swanMove():
    while swan_q1:
        x,y = swan_q1.popleft()
        if x==target_x and y == target_y:
            return True
        
        for i in range(4):
            nx = x+dx[i]    
            ny = y+dy[i]
            if nx<0 or nx>=R or ny<0 or ny>=C or swan_visited[nx][ny] == 1:
                continue
            if board[nx][ny] == '.':
                swan_q1.append((nx,ny))
            else:
                swan_q2.append((nx,ny))
            swan_visited[nx][ny] = 1
    return False

def waterMove():
    while water_q1:
        x,y = water_q1.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=R or ny<0 or ny>=C or water_visited[nx][ny] == 1:
                continue
            if board[nx][ny] == '.':
                water_q1.append((nx,ny))
            else:
                water_q2.append((nx,ny))
                
            water_visited[nx][ny] = 1
ans = 0
while True:
    waterMove()
    if swanMove():
        break
    water_q1 = water_q2
    water_q2 = deque()
    swan_q1 = swan_q2
    swan_q2 = deque()
    ans+=1
print(ans)


                    