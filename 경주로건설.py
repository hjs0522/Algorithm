from collections import deque


def solution(board):
    n = len(board)

    cost = [[[float('inf')for k in range(4)] for i in range(n)]
            for j in range(n)]
    # 왼,오,위,아래
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    # y좌표,x좌표, 마지막으로 움직인 방향

    # 오른쪽 방향으로 시작하는 경우
    queue.append((0, 0, 1))
    # 아래쪽 방향으로 시작하는 경우
    queue.append((0, 0, 3))

    for k in range(4):
        cost[0][0][k] = 0

    while queue:
        y, x, cur_dir = queue.pop()
        for i in range(4):
            newY = y+dy[i]
            newX = x+dx[i]
            newDir = i
            if newY >= 0 and newX >= 0 and newY < n and newX < n and board[newY][newX] == 0:
                temp = cost[y][x][cur_dir]
                if cur_dir == newDir:
                    temp += 100
                else:
                    temp += 600

                if cost[newY][newX][newDir] > temp:
                    cost[newY][newX][newDir] = temp
                    queue.append((newY, newX, newDir))
    return min(cost[n-1][n-1])
