def solution(n, results):
    answer = 0
    fight = [[0 for i in range(n+1)]for j in range(n+1)]
    for w, l in results:
        fight[w][l] = 1

    for _ in range(2):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if fight[i][j] == 1:
                    for k in range(1, n+1):
                        if fight[j][k] == 1:
                            fight[i][k] = 1

    for i in range(1, n+1):
        temp = 0
        for j in range(1, n+1):
            if fight[i][j] == 1 or fight[j][i] == 1:
                temp += 1
        if temp == n-1:
            answer += 1

    return answer
