def solution():
    dp[0][1][0] = 1
    for i in range(2,N):
        if board[0][i] == 0:
            dp[0][i][0] = dp[0][i-1][0]
    
    for i in range(1,N):
        for j in range(1,N):
            if board[i][j] == 0 and board[i][j-1] == 0 and board[i-1][j] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            
            if board[i][j] == 0:
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
    
    ans = 0
    for i in range(3):
        ans+= dp[N-1][N-1][i]
    print(ans)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# 파이프 끝나는 지점 x,y,파이프 모양 0: 가로 1: 세로 2: 대각선
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
solution()