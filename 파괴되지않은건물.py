def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    new_board = [[0]*(m+1) for _ in range(n+1)]
    for s in skill:
        t,sx,sy,ex,ey,degree = s
        if t == 1:
            new_board[sx][sy] -= degree
            new_board[sx][ey+1] += degree
            new_board[ex+1][sy] += degree
            new_board[ex+1][ey+1] -= degree
        else:
            new_board[sx][sy] += degree
            new_board[sx][ey+1] -= degree
            new_board[ex+1][sy] -= degree
            new_board[ex+1][ey+1] += degree
    for i in range(n+1):
        for j in range(1,m+1):
            new_board[i][j] += new_board[i][j-1]
    for j in range(m+1):
        for i in range(1,n+1):
            new_board[i][j] += new_board[i-1][j]
    for i in range(n):
        for j in range(m):
            board[i][j] = board[i][j] + new_board[i][j]
            if board[i][j] > 0:
                answer+=1
            
    return answer