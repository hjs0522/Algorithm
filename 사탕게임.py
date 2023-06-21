n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))

def check(board):
    max_cnt = 0
    for i in range(n):
        cnt_row = 1
        cnt_col = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt_row += 1
            else:
                cnt_row = 1
            if board[j][i] == board[j-1][i]:
                cnt_col += 1
            else:
                cnt_col = 1
            max_cnt = max(cnt_row,cnt_col,max_cnt)
    
    return max_cnt
ans = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
            ans = max(ans,check(board))
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
        
        if i+1 < n:
            board[i][j],board[i+1][j] = board[i+1][j],board[i][j]
            ans = max(ans,check(board))
            board[i][j],board[i+1][j] = board[i+1][j],board[i][j]
    
print(ans)