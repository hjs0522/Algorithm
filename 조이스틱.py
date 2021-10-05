def solution(name):
    answer = 0
    idx = 0
    new_name = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1)for i in name]
    while(True):
        answer += new_name[idx]
        new_name[idx] = 0
        if(sum(new_name) == 0):
            break
        left, right = 1, 1
        while new_name[idx - left] == 0:
            left += 1
        while new_name[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer
