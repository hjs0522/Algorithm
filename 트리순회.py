from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

left = defaultdict(int)
right = defaultdict(int)
 
n = int(input())
parent = [0] * (n+1)
node_count = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    left[a] = b
    right[a] = c
 
    if b != -1:
        parent[b] = a
        node_count += 1
    if c != -1:
        parent[c] = a
        node_count += 1
 
# 마지막 노드 구하는 파트
last_node = 0
def inorder(node):
    global last_node
    if node == -1:
        return
    inorder(left[node])
    last_node = node
    inorder(right[node])
 
inorder(1)
edge_count = node_count * 2
movement = 0
# 마지막 노드까지 이동 경로의 거리 구함
while last_node != 1:
    movement += 1
    last_node = parent[last_node]
print(edge_count - movement)
