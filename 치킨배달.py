from itertools import combinations

n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i,j))
            continue
        if board[i][j] == 2:
            chicken.append((i,j))
            continue
combi = list(combinations(chicken,m))
ans = int(1e9)
for c in combi:
    temp = 0
    for h in home:
        min_distance = int(1e9)
        for chi in c:
            min_distance = min(min_distance,abs(chi[0]-h[0])+abs(chi[1]-h[1]))
        temp += min_distance
    ans = min(ans,temp)
print(ans)