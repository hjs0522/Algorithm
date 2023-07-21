def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            #과제를 다 못하고 다음과제 시작하는 경우 종료시간에 실행시간 만큼 추가
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "15:00", "30"], ["computer", "12:30", "100"]]))