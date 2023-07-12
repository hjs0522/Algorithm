from collections import deque
T = int(input())

for _ in range(T):
    K,M,P =map(int,input().split())
    graph = [[] for _ in range(M+1)]
    indgree = [0]*(M+1)
    strahler = [0]*(M+1)
    count = [[0,0] for _ in range(M+1)]
    for _ in range(P):
        a,b = map(int,input().split())
        graph[a].append(b)
        indgree[b] += 1
        
    q = deque()
    for i in range(1,M+1):
        if indgree[i] == 0:
            q.append(i)
            strahler[i] = 1
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            indgree[i] -=1
            if count[i][0] == strahler[now]:
                count[i][1] += 1
            elif count[i][0] < strahler[now]:
                count[i][0] = strahler[now]
                count[i][1] = 1
            
            if indgree[i] == 0:
                q.append(i)
                if count[i][1] >= 2:
                    strahler[i] = count[i][0] + 1
                else:
                    strahler[i] = count[i][0]
    print(K,max(strahler))
            
    