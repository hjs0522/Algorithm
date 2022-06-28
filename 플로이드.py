"""
n개의 도시 m개의 버스 a,b에 대해서 도시 a에서 b로 가는데 필요한 비용의 최솟값을 구하라

첫째 줄 도시의 개수 n
둘째 줄 버스의 개수 m
셋째 줄 ~ m +2 줄 출발 도시, 도착 도시, 비용

"""


n = int(input())
m = int(input())

board = [[float("inf") for i in range(n+1)]for j in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    if c < board[a][b]:
        board[a][b] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i ==j:
                board[i][j] = 0
            elif board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if board[i][j] == float("inf"):
            print(0,end=" ")
        else:
            print(board[i][j],end=" ")
    print()
            