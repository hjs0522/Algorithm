r,c,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(3)]

def rotate(board):
    n = len(board)
    m = len(board[0])
    new_board = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_board[j][n-i-1] = board[i][j]
    return new_board
    
def calc(board,dir):
    new_board,length = [],0
    for row in board:
        num_cnt,new_row = [],[]
        for num in set(row):
            if num == 0:
                continue
            cnt = row.count(num)
            num_cnt.append((num,cnt))
        num_cnt = sorted(num_cnt,key=lambda x: [x[1],x[0]])
        for num,cnt in num_cnt:
            new_row += [num,cnt]
        new_board.append(new_row)
        length = max(length,len(new_row))
    
    for row in new_board:
        row+=[0]*(length-len(row))
        if len(row) > 100:
            row = row[:100]
    return list(zip(*new_board)) if dir == 'C' else new_board

time = 0
while True:
    if time>100:
        time= -1
        break
    if 0<=r-1<len(board) and 0<=c-1<len(board[0]) and board[r-1][c-1] == k:
        break
    if len(board) >= len(board[0]):
        board = calc(board,'R')
    else:
        board = calc(list(zip(*board)),'C')
    time+=1
print(time)