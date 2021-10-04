def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    print(s)
    s.sort(key=len)
    for i in s:
        i = i.split(',')
        for j in i:
            if j not in answer:
                answer.append(j)
    answer = list(map(int, answer))
    return answer
