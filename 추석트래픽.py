def solution(lines):
    v = []
    # line은 종료시간 기준으로 오름차순 정렬 되어있으므로 따로 정렬할 필요 없음
    for line in lines:
        # 시간을 초로 변환
        end = int(line[11:13])*60*60 + int(line[14:16]) * \
            60+int(line[17:19])+int(line[20:23])/1000
        start = end - float(line[24:-1])
        v.append((start, end))

    answer = 0

    for i in range(len(v)):
        temp = 1
        for j in range(i+1, len(v)):
            if v[i][1] >= v[j][0] or v[i][1]+0.999 > v[j][0]:
                temp += 1
        answer = max(answer, temp)
    return answer
