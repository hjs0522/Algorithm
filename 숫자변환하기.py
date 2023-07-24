def solution(x, y, n):
    dp = [int(1e9)]*(y+1)
    dp[x] = 0
    for i in range(n,y+1):
        dp[i] = min(dp[i],dp[i-n]+1)
        if i%2==0:
            dp[i] = min(dp[i],dp[i//2]+1)
        if i%3==0:
            dp[i] = min(dp[i],dp[i//3]+1)
    if dp[y] >= int(1e9):
        return -1
    return dp[y]