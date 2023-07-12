from collections import deque
T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    d = list(map(int,input().split()))
    graph = [[] for _ in range(N)]
    indgree = [0]*(N)
    time = [0]*(N)
    
    for _ in range(K):
        X,Y = map(int,input().split())
        graph[X-1].append(Y-1)
        indgree[Y-1] +=1
        
    W = int(input())
    W -=1

    q = deque()
    for i in range(N):
        if indgree[i] == 0:
            q.append(i)
            time[i] = d[i]
            if i == W:
                print(d[i])
                continue
    temp = []
    while q or temp:
        if q:
            flag = False
            now = q.popleft()
            for i in graph[now]:
                indgree[i] -=1
                # time[i]는 i를 만들기 위해 걸리는 시간
                time[i] = max(time[now],time[i])
                if indgree[i] == 0:
                    time[i] += d[i]
                    if i ==W:
                        print(time[i])
                        break
                    temp.append(i)
            if flag:
                break
        else:
            q = deque(temp)
            temp = []
        
                
