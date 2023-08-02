def solution(elements):
    answer = 0
    elements = elements*2
    ele_set = set()
    for i in range(1,len(elements)//2+1):
        for j in range(len(elements)//2):
            ele_set.add(sum(elements[j:j+i]))
    return len(ele_set)