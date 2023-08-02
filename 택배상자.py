from collections import deque
def solution(order):
    answer = 0
    q = deque([i for i in range(1,len(order)+1)])
    order = deque(order)
    stack = []
    while True:
        if len(stack)>0 and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer+=1
            continue
        if len(q) > 0:
            if q[0] == order[0]:
                q.popleft()
                order.popleft()
                answer+=1
                continue
            stack.append(q.popleft())
            continue
        break
            
    return answer