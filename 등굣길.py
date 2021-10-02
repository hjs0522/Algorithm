def solution(m, n, puddles):
    board = [[0 for j in range(m+1)]for i in range(n+1)]
    # (1,1) 에서 시작
    board[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                continue
            elif [j, i] in puddles:
                board[i][j] = 0
            else:
                # 움직이는 방법이 오른쪽 or 아래 이므로
                board[i][j] = board[i-1][j]+board[i][j-1]

    return board[n][m] % 1000000007
