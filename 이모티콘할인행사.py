from itertools import product
def solution(users, emoticons):
    answer = [0,0]
    pro = list(product([10,20,30,40],repeat = len(emoticons)))
    for p in pro:
        subscribe= 0
        cost = 0
        for user in users:
            temp = 0 
            for ratio,emoticon in zip(p,emoticons):
                if ratio >= user[0]:
                    temp += emoticon*(100-ratio)//100
            if temp >= user[1]:
                subscribe += 1
            else:
                cost+=temp
        if subscribe > answer[0]:
            answer[0] = subscribe
            answer[1] = cost
        elif subscribe == answer[0]:
            if cost > answer[1]:
                answer[1] = cost
    return answer