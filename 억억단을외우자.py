def solution(e, starts):
    answer = []
    arr = [1]*(e+1)
    for i in range(2,e+1):
        for j in range(i,e+1,i):
            arr[j] += 1
    memo = 0
    sorted_s = sorted(starts)
    dic = {}
    for s in sorted_s:
        if memo >= s:
            dic[s] = memo
            continue
        maxIdx = s
        for j in range(s,e+1):
            if arr[maxIdx] < arr[j]:
                maxIdx = j
        memo = maxIdx
        dic[s] = memo
    for s in starts:
        answer.append(dic[s])
    return answer