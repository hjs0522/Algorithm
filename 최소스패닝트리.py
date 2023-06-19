# 정점의 개수, 간선의 개수
v,e = map(int,input().split())
import heapq
q = []
for _ in range(e):
    a,b,c = map(int,input().split())
    heapq.heappush(q,(c,a,b))
parent = [0]*(v+1)
for i in range(v+1):
    parent[i] = i
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
ans = 0
while q:
    cost, start,end = heapq.heappop(q)
    if find_parent(parent,start) != find_parent(parent,end):
        union_parent(parent,start,end)
        ans +=cost
print(ans)