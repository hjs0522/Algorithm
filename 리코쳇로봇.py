from collections import deque
def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    r_x,r_y = -1,-1
    t_x,t_y = -1,-1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                r_x,r_y = i,j
                continue
            if board[i][j] == 'G':
                t_x,t_y = i,j
                continue
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[-1]*m for _ in range(n)]
    q = deque([(r_x,r_y)])
    visited[r_x][r_y] = 0
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            nx,ny = cur_x,cur_y
            while 0<=nx<n and 0<=ny<m and board[nx][ny] !='D':
                nx+=dx[i]
                ny+=dy[i]
            nx -=dx[i]
            ny -=dy[i]
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx,ny))
    print(visited)
    answer = visited[t_x][t_y]
    
    return answer
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))