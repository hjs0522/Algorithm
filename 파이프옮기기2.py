"""
새집의 크기 n*n
집 수리를 위해 파이프 하나를 옮기려고 한다. 파이프는 2개의 연속된 칸을 차지하는 크기
파이프는 매우 무거워서 밀어서 이동, 파이프는 항상 빈 칸만 차지
밀수 있는 방향 오른쪽, 대각선 오른쪽으로 아래, 아래
밀면서 회전 가능
가장 처음에 파이프는 (1,1)와 (1,2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (n,n)로 이동시키는 방법의 개수를 구해보자

첫째 줄에 집의 크기 3<= n <= 32 주어짐
둘째 줄부터 n개의 줄에는 집의 상태가 주어짐
빈칸은 0, 벽은 1

첫째 줄에 파이프의 한쪽 끝을 n,n으로 이동시키는 방법의 수를 출력
이동시킬 수 없는 경우에는 0 출력
"""

n = int(input())
board = [list(map(int,input().split())) for i in range(n)]
dp = [[[0]*3 for i in range(n)]for j in range(n)]
#dp[][][0] 가로 [1] 세로 [2] 대각선

dp[0][1][0] = 1

for i in range(1,n):
    if board[0][i] == 1:
        break
    else:
        dp[0][i][0] = 1
        
for i in range(1,n):
    for j in range(2,n):
        if board[i][j] == 0:
            #가로는 가로형태나 대각선 형태에서 될 수 있음  
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            #세로는 세로형태나 대각선 형태에서 될 수 있음
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1]==0:
            #대각선은 가로 세로 대각선 형태에서 될 수 있음
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1]+dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))
