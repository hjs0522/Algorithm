from collections import defaultdict
def solution(n, lighthouse):
    dic = defaultdict(list)
    #dic = dict(zip(tuple([i for i in range(1, n + 1)]), tuple([[] for _ in range(n)])))
    for i in lighthouse:
        dic[i[0]].append(i[1])
        dic[i[1]].append(i[0])

    answer = 0
    while len(dic):
        temp = dic.copy()
        for i in temp.keys():
            if i in dic and len(dic[i]) == 1:
                answer += 1
                n = dic[i][0]
                dummy = dic[n]

                dic.pop(n)

                for j in dummy:
                    if len(dic[j]) == 1:
                        dic.pop(j)
                    else:
                        dic[j].remove(n)
    return answer
print(solution(8,[[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))