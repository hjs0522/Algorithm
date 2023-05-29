n = int(input())
dp = [0]*(n+6)


for i in range(1,n+1):
    ti,pi = map(int,input().split())
    dp[i] = max(dp[i],dp[i-1])
    dp[i + ti - 1] = max(dp[i-1] + pi,dp[i+ti-1])
print(dp[n])
