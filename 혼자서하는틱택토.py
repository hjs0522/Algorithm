def solution(board):
    answer = 0
    o_count = 0
    x_count = 0
    for i in board:
        o_count += i.count('O')
        x_count += i.count('X')
    if o_count - x_count > 1 or o_count - x_count < 0:
        return 0
    o_check = False
    x_check = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'O':
                o_check = True
            elif board[i][0] =='X':
                x_check = True
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O':
                o_check=True
            elif board[0][i] == 'X':
                x_check = True
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] == 'O':
                o_check=True
        elif board[1][1] == 'X':
                x_check = True
    if o_check == True and x_check == False:
        if o_count == x_count+1:
            return 1
    if o_check == False and x_check == True:
        if o_count == x_count:
            return 1
    if o_check == False and x_check == False:
        return 1
    return answer