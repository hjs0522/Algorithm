n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
dp = [0 for _ in range(k+1)]

dp[0] = 1

for c in coin:
    for i in range(k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]

print(dp[k])

dp2 = [0]*(k+1)
dp2[0] = 1
for i in range(k+1):
    for c in coin:
        if i -c >=0:
            dp2[i] += dp2[i-c]
print(dp)
print(dp2)