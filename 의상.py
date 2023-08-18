from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for c,c_type in clothes:
        dic[c_type] += 1
    for value in dic.values():
        answer*=(value+1)
    return answer-1