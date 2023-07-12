import sys
sys.setrecursionlimit(1000001)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int , sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(start):
    visited[start] = 1
    
    if not graph[start]:
        dp[start][0] = 0
        dp[start][1] = 1
    else:
        for i in graph[start]:
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0],dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1
dfs(1)
print(min(dp[1][0],dp[1][1]))