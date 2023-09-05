def solution(info, edges):
    answer = 0
    n = len(info)
    visited = [0]*n
    visited[0] = 1
    def dfs(sheep,wolf):
        nonlocal answer
        if wolf >= sheep:
            return
        answer = max(answer,sheep)
        for a,b in edges:
            if visited[a] and not visited[b]:
                visited[b] = 1
                if info[b] == 0:
                    dfs(sheep+1,wolf)
                else:
                    dfs(sheep,wolf+1)
                visited[b] = 0
    dfs(1,0)
    return answer
print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))