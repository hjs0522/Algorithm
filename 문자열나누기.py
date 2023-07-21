def solution(s):
    answer = 0
    x = s[0]
    x_cnt = 1
    other_cnt = 0
    for i in range(1,len(s)):
        if s[i] == x:
            x_cnt+=1
        else:
            other_cnt+=1
        if x_cnt == other_cnt:
            answer+=1
            x_cnt =0
            other_cnt = 0
            if i+1 <len(s):
                x=s[i+1]
    if x_cnt != 0 or other_cnt !=0:
        answer+=1
        
    return answer

s = input()
solution(s)