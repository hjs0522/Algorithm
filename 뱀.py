from collections import deque
n = int(input())
k = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
snake = deque([(1,1)])
time_table = ['n'] * 10001
#왼,위,오,아 순서 0,1,2,3
dy = [0,-1,0,1]
dx = [-1,0,1,0]
cur_dir = 2
for _ in range(k):
    y,x = map(int,input().split())
    board[y][x] = 1
    
l = int(input())
for _ in range(l):
    time,dir = input().split()
    time = int(time)
    time_table[time] = dir
    
for i in range(1,10001):
    ny = snake[0][0] + dy[cur_dir]
    nx = snake[0][1] + dx[cur_dir]
    #몸에 부딪히거나 벽에 부딪히면 시간 출력 후 종료
    if (ny,nx) in snake or ny< 1 or ny>n or nx<1 or nx >n:
        print(i)
        break
    if board[ny][nx] == 1:
        snake.appendleft((ny,nx))
        board[ny][nx] = 0
    else:
        snake.appendleft((ny,nx))
        snake.pop()
    
    if time_table[i] == 'D':
        cur_dir = (cur_dir+1)%4
    elif time_table[i] == 'L':
        cur_dir = (cur_dir-1)%4


    