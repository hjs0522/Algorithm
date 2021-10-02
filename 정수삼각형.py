def solution(triangle):
    answer = 0

    """첫번째 줄은 더해줄것이 없으므로 두번째 줄부터 시작"""
    for i in range(1, len(triangle)):

        """줄의 첫 번째 요소는 전 줄의 첫번째 요소만 더 해질수 있음"""
        triangle[i][0] += triangle[i-1][0]

        """줄의 두번째 요소 ~ 마지막-1 요소 까지는 두 가지 수 중 큰 값이 더해져야 함"""
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

        """줄의 마지막 요소는 전 줄의 마지막 요소만 더 해질수 있음"""
        triangle[i][-1] += triangle[i-1][-1]
    return max(triangle[-1])
