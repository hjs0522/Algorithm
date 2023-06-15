#격자판의 크기 R,C 상어의 수 M
R,C,M = map(int,input().split())

board = [[(0,0,0)]*C for _ in range(R)]
for _ in range(M):
    #r,c는 상어의 위치 s는 속력, d는 이동방향, z는 크기
    #d = 1 위, d=2 아래, d=3 오른, d=4 왼
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = (s,d-1,z)

board = list(map(list,zip(*board)))
dx = [0,0,1,-1]
dy = [-1,1,0,0]
def move(board):
    temp = [[(0,0,0)]*R for _ in range(C)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != (0,0,0):
                s,d,z = board[i][j]
                temp_x = i
                temp_y = j
                temp_s = s
                while temp_s:
                    nx = temp_x+dx[d]
                    ny = temp_y+dy[d]
                    if nx < 0 or nx>=C or ny<0 or ny>=R:
                        if d == 0:
                            d=1
                        elif d==1:
                            d=0
                        elif d==2:
                            d=3
                        else:
                            d=2
                        continue
                    temp_s -=1
                    temp_x = nx
                    temp_y = ny
                if temp[temp_x][temp_y] == (0,0,0):
                    temp[temp_x][temp_y] = (s,d,z)
                elif temp[temp_x][temp_y] != (0,0,0):
                    t_s,t_d,t_z = temp[temp_x][temp_y]
                    if t_z > z:
                        continue
                    else:
                        temp[temp_x][temp_y] = (s,d,z)
    return temp
ans = 0
for i in range(C):
    for j in range(R):
        if board[i][j] != (0,0,0):
            ans += board[i][j][2]
            board[i][j] = (0,0,0)
            break
    board = move(board)
    
    
print(ans)