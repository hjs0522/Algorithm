N = int(input())
board = input()
dp = [int(1e9)]*(N+1)
dp[0] = 0
for i in range(N):
    if board[i] == 'B':
        for j in range(i+1,N):
            if board[j] == 'O':
                dp[j] = min(dp[j],dp[i]+(j-i)**2)
        continue
    
    if board[i] == 'O':
        for j in range(i+1,N):
            if board[j] == 'J':
                dp[j] = min(dp[j],dp[i]+(j-i)**2)
        continue
    
    if board[i] == 'J':
        for j in range(i+1,N):
            if board[j] == 'B':
                dp[j] = min(dp[j],dp[i]+(j-i)**2)
        continue
if dp[N-1] >= int(1e9):
    print(-1)
else:
    print(dp[N-1])
