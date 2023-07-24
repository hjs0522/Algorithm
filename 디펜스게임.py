
def solution(n, k, enemy):
    answer = 0
    def dfs(n,k,idx,enemy):
        nonlocal answer
        if idx == len(enemy):
            answer = idx
            return
        if n-enemy[idx]>=0:
            dfs(n - enemy[idx],k,idx+1,enemy)
        if k>0:
            dfs(n,k-1,idx+1,enemy)
        
        if enemy[idx] > n and k == 0:
            answer = max(answer,idx)
            return
        
    dfs(n,k,0,enemy)
    return answer
print(solution(	7, 3, [4, 2, 4, 5, 3, 3, 1]))
