V,E = map(int,input().split())
graph = [[int(1e9)]*V for _ in range(V)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

ans = int(1e9)
for i in range(V):
    ans = min(ans,graph[i][i])
    
if ans == int(1e9):
    print(-1)
else:
    print(ans)