n,m,x,y,k = map(int,input().split(" "))
board = []
for i in range(n):
    board.append(list(map(int,input().split(" "))))
# 위,북,동,서,남,아래
dice = [0,0,0,0,0,0]
def turn(dir):
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if dir == 1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    elif dir == 2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    elif dir == 3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    else:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e

command = list(map(int,input().split(" ")))
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for c in command:
    x+=dx[c-1]
    y += dy[c-1]
    
    if x<0 or x>=n or y<0 or y>=m:
        x-=dx[c-1]
        y-=dy[c-1]
        continue
    turn(c)
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    print(dice[0])
        