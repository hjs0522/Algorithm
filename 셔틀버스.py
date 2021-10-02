def solution(n, t, m, timetable):
    answer = ''
    crew = [int(tt.split(':')[0])*60 + int(tt.split(':')[1])
            for tt in timetable]
    crew.sort()
    # 출발시간, 탄 사람 수, 마지막 탄 사람이 언제 탔는지
    bus = [(540 + t*i, 0, None) for i in range(n)]

    bus_idx, crew_idx = 0, 0
    while crew_idx < len(crew):
        c = crew[crew_idx]
        if bus_idx == len(bus):
            break
        # 버스시간보다 빠르게 나오고, 버스인원이 다 안 찬 경우
        if c <= bus[bus_idx][0] and bus[bus_idx][1] < m:
            time, person, _ = bus[bus_idx]
            bus[bus_idx] = time, person+1, c
            crew_idx += 1
        else:
            bus_idx += 1
    # 정답은 기본적으로 마지막 버스가 오는 시간
    answer = bus[-1][0]
    # 마지박 버스에 탄 사람이 있는 경우
    if bus[-1][2]:
        # 마지막 버스가 꽉찬 경우
        if bus[-1][1] == m:
            # 마지막으로 탄 사람 보다 1분 먼저 오면 됨
            answer = bus[-1][2]-1
    # 공백엔 0 넣어주고 오른쪽으로 정렬
    return'{0:0>2}:{1:0>2}'.format(answer//60, answer % 60)
