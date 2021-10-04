# 크루스칼 알고리즘 이용
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    cost_set = set([costs[0][0]])
    while len(cost_set) != n:
        for i, cost in enumerate(costs):
            if cost[0] in cost_set and cost[1] in cost_set:
                continue
            if cost[0] in cost_set or cost[1] in cost_set:
                cost_set.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer


"""
#프림 알고리즘 이용
import heapq
def solution(n, costs):
    answer = 0
    
    board = [[]for i in range(n)]
    for u,v,cost in costs:
        board[u].append((cost,v))
        board[v].append((cost,u))
    
    checked = [False for i in range(n)]
    
    queue = []
    queue.append((0,0))
    
    while queue and not all(checked):
        cost,edge = heapq.heappop(queue)
        if checked[edge] == False:
            checked[edge] = True
            answer+= cost
        
            for i in range(len(board[edge])):
                if checked[board[edge][i][1]] == False:
                    heapq.heappush(queue,(board[edge][i][0],board[edge][i][1]))
    return answer
"""

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
