def find_parent(parent,r,c):
    if parent[r][c] != (r,c):
        parent[r][c] = find_parent(parent,parent[r][c][0],parent[r][c][1])
    return parent[r][c]

def union_parent(parent,r1,c1,r2,c2):
    r1,c1= find_parent(parent,r1,c1)
    r2,c2 = find_parent(parent,r2,c2)
    if r1 < r2:
        parent[r2][c2] = (r1,c1)
        return (r1,c1)
    else:
        parent[r1][c1] = (r2,c2)
        return (r2,c2)

def update(board,parent,r,c,value):
    r,c = find_parent(parent,r,c)
    board[r][c] = value

def convert(board,parent,value1,value2):
    for i in range(len(board)):
        for j in range(len(board)):
            r,c = find_parent(parent,i,j)
            if board[r][c] == value1:
                board[r][c] = value2

def merge(board,parent,r1,c1,r2,c2):
    if r1==r2 and c1==c2:
        return
    r1,c1 = find_parent(parent,r1,c1)
    r2,c2 = find_parent(parent,r2,c2)
    r,c = union_parent(parent,r1,c1,r2,c2)
    for i in range(len(parent)):
        for j in range(len(parent[i])):
            find_parent(parent,i,j)
    if board[r1][c1] == -1:
        board[r1][c1] = board[r2][c2]
        return
    if board[r2][c2] == -1:
        board[r2][c2] = board[r1][c1]
        return
    board[r][c] = board[r1][c1]


def unmerge(board,parent,r,c):
    #temp는 해체의 주체가 되는 좌표
    temp = (r,c)
    r,c = find_parent(parent,r,c)
    value = board[r][c]
    for i in range(len(parent)):
        for j in range(len(parent[i])):
            if parent[i][j] == (r,c):
                parent[i][j] = (i,j)
                board[i][j] = -1
    board[temp[0]][temp[1]] = value

def Print(board,parent,r,c):
    r,c = find_parent(parent,r,c)
    if board[r][c] == -1:
        return "EMPTY"
    return board[r][c]


def solution(commands):
    answer = []
    board = [[-1 for i in range(51)]for j in range(51)]
    parent = [[(r,c) for c in range(51)]for r in range(51)]
    for command in commands:
        command = command.split(" ")
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r,c,value = int(command[1]),int(command[2]),command[3]
                update(board,parent,r,c,value)
                continue
            if len(command) == 3:
                value1,value2 = command[1],command[2]
                convert(board,parent,value1,value2)
                continue
        if command[0] == 'MERGE':
            r1,c1,r2,c2 = int(command[1]),int(command[2]),int(command[3]),int(command[4])
            merge(board,parent,r1,c1,r2,c2)
            continue
        if command[0] == 'UNMERGE':
            r,c = int(command[1]),int(command[2])
            unmerge(board,parent,r,c)
            continue
        if command[0] == 'PRINT':
            r,c = int(command[1]),int(command[2])
            answer.append(Print(board,parent,r,c))
            continue
    return answer