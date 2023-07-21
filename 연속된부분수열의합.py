def solution(sequence, k):
    answer = [0,len(sequence)]
    subSum = [0]*(len(sequence)+1)
    for i in range(len(sequence)):
        subSum[i+1] = subSum[i] + sequence[i]
    p2 = 0
    p1 = 0
    while p2<len(subSum):
        result = subSum[p2] - subSum[p1]
        if result < k:
            p2+=1
        elif result > k:
            p1 +=1
        else:
            if answer[1] - answer[0] > p2-p1-1:
                answer[1] = p2-1
                answer[0] = p1
            p1+=1
            p2+=1
            
    return answer
print(solution([1, 1, 1, 2, 3, 4, 5], 5))