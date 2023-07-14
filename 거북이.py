T = int(input())
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(T):
    command = input()
    max_x,max_y,min_x,min_y = 0,0,0,0
    direction = 0
    cur_x,cur_y = 0,0
    for c in command:
        if c == 'L':
            direction = (direction+1)%4
            continue
        if c == 'R':
            direction = (direction-1)%4
            continue
        if c == 'F':
            cur_x += dx[direction]
            cur_y += dy[direction]
            max_x = max(cur_x,max_x)
            min_x = min(cur_x,min_x)
            max_y = max(cur_y,max_y)
            min_y = min(cur_y,min_y)
            continue
        if c == 'B':
            cur_x -= dx[direction]
            cur_y -= dy[direction]
            max_x = max(cur_x,max_x)
            min_x = min(cur_x,min_x)
            max_y = max(cur_y,max_y)
            min_y = min(cur_y,min_y)
    print(abs(max_x-min_x)*abs(max_y-min_y))
    