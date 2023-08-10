def solution(grid):
    answer = []
    #아,왼,위,오
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    n = len(grid)
    m = len(grid[0])
    visited = [[[False]*4 for _ in range(m)]for _ in range(n)]
    for x in range(n):
        for y in range(m):
            for d in range(4):
                if visited[x][y][d]:
                    continue
                count = 0
                nx,ny = x,y
                while not visited[nx][ny][d]:
                    visited[nx][ny][d] = True
                    count+=1
                    if grid[nx][ny] == 'L':
                        d = (d-1)%4
                    elif grid[nx][ny] == 'R':
                        d = (d+1)%4
                    nx = (nx+dx[d])%n
                    ny = (ny+dy[d])%m
                answer.append(count)
    answer.sort()
                        
    return answer