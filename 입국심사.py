def solution(n, times):
    answer = 0

    # 최대값과 최소값 사이 범위에서 값 하나를 찾는 것이므로 이분탐색 사용
    left = 1
    right = (n//len(times))*max(times)

    while(left <= right):
        mid = (left+right)//2
        cnt = 0
        for i in range(len(times)):
            cnt += mid//times[i]
            if cnt >= n:
                answer = mid
                right = mid-1
                break
        if cnt < n:
            left = mid+1
    return answer
