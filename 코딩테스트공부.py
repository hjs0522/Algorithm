import heapq
def solution(alp, cop, problems):
    answer = 0
    max_alp = 0
    max_cop = 0
    for p in problems:
        max_alp = max(max_alp,p[0])
        max_cop = max(max_cop,p[1])
    problems += [[0,0,1,0,1],[0,0,0,1,1]]
    dp = [[int(1e9)]*151 for _ in range(151)]
    q = [(0,alp,cop)]
    dp[alp][cop] = 0
    while q:
        cur_cost,cur_alp,cur_cop = heapq.heappop(q)
        if cur_alp >= max_alp and cur_cop >= max_cop:
            return cur_cost
        for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
            next_alp,next_cop = min(150,cur_alp + alp_rwd),min(150,cur_cop+cop_rwd)
            if(cur_alp >= alp_req and cur_cop >=cop_req and cur_cost + cost < dp[next_alp][next_cop]):
                dp[next_alp][next_cop] = cur_cost + cost
                heapq.heappush(q,(cur_cost+cost,next_alp,next_cop))
    
    return answer
print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))