def solution(A, B):
    ans =0
    A.sort(reverse = True)
    B.sort(reverse = True)
    B_idx = 0
    for i in range(len(A)):
        if A[i] < B[B_idx]:
            ans+=1
            B_idx+=1
    return ans