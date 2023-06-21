N,K = map(int,input().split())

visited = [-1]*(100001)

from collections import deque
def bfs():
    q = deque([N])
    visited[N]= 0
    while q:
        cur = q.popleft()
        if  cur == K:
            print(visited[K])
            break
            
        if 0<=cur*2 < 100001:
            if visited[2*cur] == -1:
                q.append(cur*2)
                visited[cur*2] = visited[cur]
        if 0<=cur -1 < 100001:
            if visited[cur -1] == -1:
                q.append(cur-1)
                visited[cur-1] = visited[cur]+1
                
        if 0<=cur +1 <100001:
            if visited[cur+1] == -1:
                q.append(cur+1)
                visited[cur+1] = visited[cur]+1
                
                

bfs()