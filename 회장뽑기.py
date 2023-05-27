"""
어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다.
어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다.
어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나 친구의 친구이거나,친구의 친구의 친구임을 말한다.
각 노드를 출발지점이라고 했을 때 다른 각 노드까지의 최소거리를 구하고 그 최소거리 값들중 최댓값이 가장 작은 노드가 회장이 된다.
"""

from collections import defaultdict


def main():
    n = int(input())
    candidate = defaultdict(list)
    while True:
        node1,node2 = map(int,input().split())
        if node1==-1 and node2 == -1:
            break
        candidate[node1].append(node2)
        candidate[node2].append(node1)
    