from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(prior,idx) for idx,prior in enumerate(priorities)])
    priorities.sort(reverse = True)
    priorities = deque(priorities)
    while queue:
        if queue[0][0] == priorities[0]:
            if location == queue[0][1]:
                answer+=1
                break
            else:
                queue.popleft()
                priorities.popleft()
                answer+=1
        else:
            queue.append(queue.popleft())
    return answer