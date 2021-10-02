from collections import deque


def solution(places):
    answer = []
    # 좌1 우1 하1 좌1하1 좌2 우2 우1하1 하2
    dx = [-1, 1, 0, -1, -2, 2, 1, 0]
    dy = [0, 0, 1, 1, 0, 0, 1, 2]

    for place in places:
        queue = deque()
        # 거리 두기를 잘 지켰는지 판별되는 값 result
        result = 1
        for i in range(len(place)):
            for j in range(len(place[i])):
                # 사람이 앉아 있는 곳의 좌표 큐에 넣기
                if place[i][j] == "P":
                    queue.append((i, j))

        flag = True
        while queue and flag:
            y, x = queue.popleft()
            for i in range(8):
                newY = y+dy[i]
                newX = x+dx[i]
                if newY >= 0 and newX >= 0 and newY < 5 and newX < 5:
                    if i == 0 or i == 1 or i == 2:
                        # 좌1 우1 하1
                        if place[newY][newX] == "P":
                            result = 0
                            flag = False
                            break
                    elif i == 3:
                        # 좌1 하1
                        if place[newY][newX] == "P" and (place[y][x-1] == "O" or place[y+1][x] == "O"):
                            result = 0
                            flag = False
                            break
                    elif i == 4:
                        # 좌2
                        if place[newY][newX] == "P" and place[y][x-1] == "O":
                            result = 0
                            flag = False
                            break
                    elif i == 5:
                        # 우2
                        if place[newY][newX] == "P" and place[y][x+1] == "O":
                            result = 0
                            flag = False
                            break
                    elif i == 6:
                        # 우1 하1
                        if place[newY][newX] == "P" and (place[y][x+1] == "O" or place[y+1][x] == "O"):
                            result = 0
                            flag = False
                            break
                    else:
                        # 하2
                        if place[newY][newX] == "P" and place[y+1][x] == "O":
                            result = 0
                            flag = False
                            break
        answer.append(result)

    return answer
