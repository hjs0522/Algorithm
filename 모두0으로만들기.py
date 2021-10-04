import sys
sys.setrecursionlimit(10**6)


def dfs(tree, a, checked, idx):
    global answer
    checked[idx] = True
    for e in tree[idx]:
        if checked[e] == False:
            a[idx] += dfs(tree, a, checked, e)
    answer += abs(a[idx])
    return a[idx]


def solution(a, edges):
    if sum(a) != 0:
        return -1

    global answer
    answer = 0
    checked = [False for i in range(len(a))]
    tree = [[]for i in range(len(a))]

    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    # 0번째 인덱스에 위치한 것이 루트노드라 가정
    dfs(tree, a, checked, 0)
    return answer
