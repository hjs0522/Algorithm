import sys
sys.setrecursionlimit(100001)

N = int(input())
inhabitant = list(map(int,input().split()))
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a,b=  map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
dp = [[0,0] for _ in range(N)]
visited = [0]*(N)

def dfs(start,root):
    visited[start] = 1
    if start != root and len(graph[start])==1:
        dp[start][1] = inhabitant[start]
        dp[start][0] = 0
    else:
        for i in graph[start]:
            if visited[i] == 0:
                dfs(i,root)
                dp[start][1] += dp[i][0]
                #적어도 하나의 우수마을이 인접해 있어야 하는데 이렇게 계산해도 되는 이유
                # => 세개 연속 우수마을이 아닌 경우가 우수 x 우수 o 우수 x 보다 큰 값일 수 없기 때문에
                dp[start][0] += max(dp[i][1],dp[i][0])
        dp[start][1] += inhabitant[start]
dfs(0,0)
print(max(dp[0][0],dp[0][1]))