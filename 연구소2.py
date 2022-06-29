"""
승원이는 연구소의 특정 위치에 바이러스 m개를 놓을 것이고
승원이의 신호와 동시에 바이러스는 퍼지게 된다.
바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제
0은 빈칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸

첫째 줄에 연구소의 크기 n, 놓을 수 있는 바이러스의 개수 m

"""
from itertools import combinations
from collections import deque

def check(n,board,visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and board[i][j] == 0:
                return False
    return True

def bfs(n,board,virusLoc):
    visited = [[-1 for i in range(n)]for j in range(n)]
    queue = deque([])
    maxTime = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for virus in virusLoc:
        queue.append(virus)
        visited[virus[0]][virus[1]] = 0
    while queue:
        y,x = queue.popleft()
        maxTime = max(maxTime,visited[y][x])
        for i in range(4):
            newY = y+dy[i]
            newX = x + dx[i]
            if 0 <= newY <n and 0<=newX<n and board[newY][newX] != 1 and visited[newY][newX] == -1:
                visited[newY][newX] = visited[y][x] +1
                queue.append([newY,newX])
    if check(n,board,visited) == True:
        return maxTime
    else:
        return float("inf")

def main():
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for i in range(n)]
    
    virus = []
    ans = float("inf")
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                virus.append([i,j])
                
    virusCombi = list(combinations(virus,m))
    for c in virusCombi:
        ans = min(ans,bfs(n,board,c))
        
    return ans if ans!=float("inf") else -1
    
print(main())