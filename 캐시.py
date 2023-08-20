from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = []
    if cacheSize == 0:
        return len(cities)*5
    for c in cities:
        c = c.lower()
        if c in q:
            if q:
                q.pop(q.index(c))
            q.append(c)
            answer+=1
        else:
            if len(q) == cacheSize:
                q.pop(0)
            q.append(c)
            answer+=5
    return answer
print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))