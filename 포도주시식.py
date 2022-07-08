def main():
    n = int(input())
    grape = [int(input()) for i in range(n)]
    dp = [[0 for _ in range(3)]for _ in range(n)]
    dp[0][1] = grape[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2]);
        dp[i][1] = dp[i-1][0] +grape[i]
        dp[i][2] = dp[i-1][1] + grape[i]
        
    ans = 0
    ans = max(dp[n-1][0],dp[n-1][1],dp[n-1][2])
    print(ans)
main()