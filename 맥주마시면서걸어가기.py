from collections import defaultdict,deque
t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int,input().split()))
    market = []
    visited = defaultdict(int)
    visited[start] = 1
    for i in range(n):
        market.append(tuple(map(int,input().split())))
    end = tuple(map(int,input().split()))
    q = deque([start])
    flag = True
    while q:
        cur = q.popleft()
        if abs(cur[0] - end[0]) + abs(cur[1] - end[1])<=1000:
            print('happy')
            flag = False
            break
        remain = []
        for i in market:
            if visited[i] != 0:
                continue
            if abs(cur[0] - i[0]) + abs(cur[1] - i[1])<=1000:
                q.append(i)
                visited[i] = 1
            else:
                remain.append(i)
        market = remain
    if flag:
        print('sad')