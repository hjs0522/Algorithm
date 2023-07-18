def draw():
    global n
    x = y = n//2
    cnt = 2
    num = 2
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    board[x][y] = 1
    x-=1
    y-=1
    if n==1:
        return
    
    while True:
        for i in range(4):
            for j in range(cnt):
                x +=dx[i]
                y +=dy[i]
                board[x][y] = num
                if num==m:
                    ans[0] = x+1
                    ans[1] = y+1
                if num==n**2:
                    return
                num+=1
        cnt+=2
        x-=1
        y-=1
        
    
n =int(input())
m = int(input())
board = [[0]*n for _ in range(n)]
ans = [n//2+1,n//2+1]
draw()
for i in board:
    print(*i)
print(ans[0],ans[1])
