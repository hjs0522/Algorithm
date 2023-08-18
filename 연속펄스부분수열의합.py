def solution(sequence):
    answer = 0
    n = len(sequence)
    arr = [(-1)**(i)*sequence[i] for i in range(n)]
    subSum = [0]*(n+1)
    for i in range(1,n+1):
        subSum[i] = arr[i-1]+subSum[i-1]
    idx1,idx2 = subSum.index(min(subSum)),subSum.index(max(subSum))
    return subSum[idx2]-subSum[idx1]