def rotate(key):
    key = [k[::-1] for k in zip(*key)]
    return key


def check(key, lock):
    m = len(key)
    n = len(lock)

    for i in range(n+m-1):
        for j in range(n+m-1):
            flag = True
            board = [[0 for i in range(n+2*m-2)]for j in range(n+2*m-2)]

            # board에 key 복사
            for k in range(m):
                for l in range(m):
                    board[i+k][j+l] = key[k][l]

            # board와 lock이 맞는지 비교
            for k in range(n):
                for l in range(n):
                    # board랑 lock이 같으면 돌기끼리 맞거나 남는 홈이 있다는 것 이기 때문에 False
                    if board[k+m-1][l+m-1] == lock[k][l]:
                        flag = False
                        break
            if flag == True:
                return True

    return flag


def solution(key, lock):
    answer = False
    for k in range(4):
        answer = check(key, lock)
        if answer == True:
            return True
        key = rotate(key)

    return answer
