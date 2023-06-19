import copy
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M,K = map(int,input().split())
graph = []
shark_priority = [[] for _ in range(M)]
shark_direction = []
smell = [[[]for _ in range(N)]for _ in range(N)]
for i in range(N):
    graph.append(list(map(int,input().split())))
shark_direction = list(map(int,input().split()))
for i in range(M):
    for _ in range(4):
        shark_priority[i].append(list(map(int,input().split())))

def check(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] >1:
                return False
    return True

def expose_smell(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                smell[i][j].append((graph[i][j],K))

def shark_move(graph):
    temp = copy.deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                shark_number = graph[i][j]
                flag = False
                #냄새가 없는칸, 자신의 냄새가 있는 칸, 그게 아니면 진행방향
                
                #냄새가 없는 빈칸인 경우
                for k in range(4):
                    cur_direction = shark_direction[shark_number-1] - 1
                    move = shark_priority[shark_number-1][cur_direction][k] -1
                    nx = i + dx[move]
                    ny = j + dy[move]
                    if 0<=nx<N and 0<=ny<N:
                        if len(smell[nx][ny]) == 0:
                            flag = True
                            if temp[nx][ny] != 0 and temp[nx][ny] < shark_number:
                                temp[i][j] = 0
                                break
                            else:
                                temp[nx][ny] = shark_number
                                temp[i][j] = 0
                                shark_direction[shark_number-1] = move +1
                                break
                    if flag:
                        break
                
                #자신의 냄새가 있는 칸
                if flag == False:
                    for k in range(4):
                        cur_direction = shark_direction[shark_number-1] - 1
                        move = shark_priority[shark_number-1][cur_direction][k] -1
                        nx = i + dx[move]
                        ny = j + dy[move]
                        if 0<=nx<N and 0<=ny<N:
                            for l in smell[nx][ny]:
                                if l[0] == shark_number:
                                    flag = True
                                    if temp[nx][ny] != 0 and temp[nx][ny] < shark_number:
                                        temp[i][j] = 0
                                        break
                                    else:
                                        temp[nx][ny] = shark_number
                                        temp[i][j] = 0
                                        shark_direction[shark_number-1] = move +1
                                        break
                        if flag:
                            break
                #그냥 우선순위에 따라
                if flag == False:
                    for k in range(4):
                        cur_direction = shark_direction[shark_number-1] -1
                        move = shark_priority[shark_number-1][cur_direction][k]-1
                        nx = i + dx[move]
                        ny = j + dy[move]
                        if 0<=nx<N and 0<=ny<N:
                            flag = True
                            if temp[nx][ny] != 0 and temp[nx][ny] < shark_number:
                                temp[i][j] = 0
                                break
                            else:
                                temp[nx][ny] = shark_number
                                temp[i][j] = 0
                                shark_direction[shark_number-1] = move + 1
                                break
                    if flag:
                        break
    return temp

def decrease_smell(smell):
    for i in range(N):
        for j in range(N):
            temp = []
            for num,k in smell[i][j]:
                if k > 1:
                    temp.append((num,k-1))
            smell[i][j] = temp
ans = 0

while not check(graph):
    expose_smell(graph)
    graph = shark_move(graph)
    decrease_smell(smell)
    ans+=1
    if ans > 1000:
        ans = -1
        break
print(ans)
