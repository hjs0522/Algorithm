import heapq


def solution(jobs):
    time = 0
    answer = 0
    heap = []
    jobs_len = len(jobs)

    """jobs 이나 heap 중에 하나라도 남는 요소가 있으면 안 됨"""
    while jobs or heap:
        """jobs 배열내의 요소를 삭제 할 것이기 때문에 복사된 배열 사용"""
        for job in jobs[:]:
            if job[0] <= time:
                """종료 되는 시간을 기준으로 정렬"""
                heapq.heappush(heap, (job[1], job[0]))
                jobs.remove(job)
        if heap:
            working, request = heapq.heappop(heap)
            time += working
            answer += time - request
        else:
            time += 1
    return answer // jobs_len
