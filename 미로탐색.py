"""
n*m크기의 배열
1은 이동할 수 있는 칸,0은 이동할 수 없는 칸
1,1에서 출발하여 n,m의 위치로 이동할 때 지나야 하는 최소의 칸 수
"""

from collections import deque

def bfs(n,m,board):
    visited = [[0 for i in range(m)]for j in range(n)]
    queue = deque([[0,0]])
    visited[0][0]  = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while(queue):
        y,x = queue.popleft()
        for i in range(4):
            newY = y+dy[i]
            newX = x+dx[i]
            if 0<=newY<n and 0<= newX<m and board[newY][newX] == 1 and visited[newY][newX] ==0:
                visited[newY][newX] = visited[y][x] +1
                queue.append([newY,newX])
    return visited[n-1][m-1]
        

def main():
    n,m = map(int,input().split())
    board = [list(map(int,input())) for i in range(n)]
    return bfs(n,m,board)
print(main())