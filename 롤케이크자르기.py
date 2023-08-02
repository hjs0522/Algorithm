from collections import Counter
def solution(topping):
    answer = 0
    counter= Counter(topping)
    counter_set = set()
    for t in topping:
        counter[t] -=1
        counter_set.add(t)
        if counter[t] == 0:
            counter.pop(t)
        if len(counter) == len(counter_set):
            answer+=1
    return answer