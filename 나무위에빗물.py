"""
매초마다 모든 정점은 아래의 작업을 순서대로 반복
 - 물을 가지고 있으며, 자식 정점이 있다면 자식 정점 중 하나를 골라 물을 1 준다. 여러개이면 그 중 하나 골라서
 - 만약 부모 정점이 자신에게 물을 흘려보내면 받아서 쌓아둔다.
부모에게 받은 물을 바로 자식에게 줄 수 없음
더 이상 물이 움직이지 않는 상태가 되었을때 각 정점에 있는 물의 양이 궁금
i번 정점에 쌓인 물의 양의 기댓값을 pi라 할때, pi가 0보다 큰 정점들에 대해서 pi들의 평균은 어느정도 일까?

노드의 수  n 물의 양 w 
"""

from collections import defaultdict, deque



def main():
    n,w = map(int,input().split())
    tree = defaultdict(list)
    
    for i in range(n-1):
        node1,node2 = map(int,input().split())
        tree[node1].append(node2)
        tree[node2].append(node1)
        
    queue = deque()
    queue.append(1)
    checked = [False for i in range(n+1)]
    cnt = 0
    while(queue):
        node = queue.pop()
        if not checked[node]:
            checked[node] = True
        else:
            continue
        
        flag = True
        for i in range(len(tree[node])):
            if checked[tree[node][i]] ==False:
                queue.append(tree[node][i])
                flag = False
        if flag:
         cnt+=1
    print('%.10f' %(w/cnt))
main()