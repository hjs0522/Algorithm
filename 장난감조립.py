from collections import deque
n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
need = [[0]*(n+1) for _ in range(n+1)]
inDegree = [0]*(n+1)
for i in range(m):
    #x를 만들기 위해 y가 k개 필요함
    x,y,k = map(int,input().split())
    graph[y].append((x,k))
    inDegree[x] +=1

def topology_sort():
    q = deque()
    result = [0]*(n+1)
    for i in range(1,n+1):
        if inDegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for next,next_need in graph[now]:
            #now가 기본부품인 경우
            if need[now].count(0) == n+1:
                need[next][now] += next_need
            else:
            #now가 중간부품인 경우
                for i in range(1,n+1):
                    need[next][i] += need[now][i]*next_need
            inDegree[next] -=1
            if inDegree[next] == 0:
                q.append(next)
    for x in enumerate(need[n]):
        if x[1] > 0:
            print(*x)
topology_sort()