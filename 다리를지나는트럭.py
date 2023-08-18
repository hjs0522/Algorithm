from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)
    queue = deque([0]*bridge_length)
    sum_queue = 0
    while truck:
        if len(queue) == bridge_length:
            sum_queue -= queue.popleft()
        
        if truck and truck[0] + sum_queue <= weight:
            cur = truck.popleft()
            queue.append(cur)
            sum_queue += cur
        else:
            queue.append(0)
        answer+=1
    for i in range(len(queue)-1,-1,-1):
        if queue[i] != 0:
            answer+= i+1
            break
    return answer
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))