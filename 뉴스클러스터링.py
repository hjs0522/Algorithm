#자카드 유사도 = 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
from itertools import combinations
from collections import defaultdict
def solution(str1, str2):
    answer = 0
    str1 = list(str1)
    str2 = list(str2)
    
    s1 = defaultdict(int)
    s2 = defaultdict(int)
    
    set_s1 = set()
    for i in range(len(str1)-1):
        temp = ''.join([str1[i],str1[i+1]])
        if temp.isalpha():
            temp = temp.lower()
            set_s1.add(temp)
            s1[temp] += 1
    set_s2 = set()
    for i in range(len(str2)-1):
        temp = ''.join([str2[i],str2[i+1]])
        if temp.isalpha():
            temp = temp.lower()
            set_s2.add(temp)    
            s2[temp] +=1
            
    len_union = 0
    len_intersection = 0
    for i in set_s1|set_s2:
        len_union += max(s1[i],s2[i])
    for i in set_s1&set_s2:
        len_intersection +=min(s1[i],s2[i])
    if len_union == 0:
        return 65536
    return int(len_intersection/len_union*65536)