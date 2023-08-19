def solution(scores):
    answer = 1
    user = scores[0]
    sum_user = sum(user)
    scores.sort(key = lambda x:(-x[0],x[1]))
    max_com = 0
    for s in scores:
        if user[0] < s[0] and user[1] < s[1]:
            return -1
        #s[0]의 값이 큰 값부터 s[0]의 값이 같다면 s[1]이 작은 값부터 정렬하므로 뒤에 나오는 것은 s[1]이 이전 것보다 더 크거나 같아야 인센티브를 받을 수 있다
        if max_com <= s[1]:
            if sum_user < s[0]+s[1]:
                answer+=1
            max_com = s[1]
            
    return answer