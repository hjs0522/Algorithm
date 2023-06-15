board = []
for i in range(9):
    board.append(list(map(int,input())))

blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))

#같은 열에 value가 이미 있는지 확인
def check_row(row,value):
    for i in range(9):
        if board[row][i] == value:
            return False
    return True

def check_col(col,value):
    for i in range(9):
        if board[i][col] == value:
            return False
    return True
    
def check_rec(x,y,value):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j] == value:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*board[i],sep='')
        exit(0)
    for value in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]
        
        if check_row(x,value) and check_col(y,value) and check_rec(x,y,value):
            board[x][y] = value
            dfs(idx+1)
            board[x][y] = 0
        
dfs(0)