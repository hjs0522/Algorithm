def solution(info, query):
    answer = []
    data = dict()
    for a in ["cpp", "java", "python", "-"]:
        for b in ["backend", "frontend", "-"]:
            for c in ["junior", "senior", "-"]:
                for d in ["chicken", "pizza", "-"]:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split(" ")
        for a in [i[0], "-"]:
            for b in [i[1], "-"]:
                for c in [i[2], "-"]:
                    for d in [i[3], "-"]:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

    for q in query:
        q = q.split(" ")
        score = data[(q[0], q[2], q[4], q[6])]
        l = 0
        r = len(score)
        while l < r:
            mid = (l+r) // 2
            if score[mid] >= int(q[7]):
                r = mid
            else:
                l = mid+1
        answer.append(len(score)-l)
    return answer
