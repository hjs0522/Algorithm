n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
dp = [int(1e9) for _ in range(k+1)]

dp[0] = 0

for c in coin:
    for i in range(k+1):
        if i - c >= 0:
            dp[i] = min(dp[i-c]+1,dp[i])

if dp[k] == int(1e9):
    dp[k] = -1
print(dp[k])