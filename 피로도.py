from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for i in range(1, len(dungeons)+1):
        permu = list(permutations(dungeons, i))
        for j in range(len(permu)):
            temp = k
            cnt = 0
            for q in range(len(permu[j])):
                if permu[j][q][0] <= temp:
                    temp -= permu[j][q][1]
                    cnt += 1
            if cnt > answer:
                answer = cnt
    return answer
