def solution(cap, n, deliveries, pickups):
    answer =0
    d = 0
    p =0
    pos = 0
    for i in range(n-1,-1,-1):
        if deliveries[i] != 0 or pickups[i]!=0:
            pos = i
            break
    
    for i in range(n-1,-1,-1):
        d += deliveries[i]
        p += pickups[i]
        while d>cap or p > cap:
            d -=cap
            p -=cap
            answer += 2*(pos+1)
            pos = i
    if d>0 or p>0:
        answer += 2*(pos+1)
            
    return answer