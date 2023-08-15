#temperature = 실외 온도, t1~t2 = 희망 온도 ,a = 희망온도와 실내온도가 다른 경우 소비량 ,b= 희망온도와 실내온도가 같은 경우 소비량 
def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    if temperature > t2:
        temperature = t1 - (temperature- t2)
    if temperature < 0:
        t1 += -temperature
        t2 += -temperature
        temperature = 0
    else:
        t1 -= temperature
        t2 -= temperature
        temperature = 0
    n = len(onboard)
    dp = [[int(1e9)]*(t2+2) for _ in range(n)]
    #dp[i][j] = i분 상태에서 j도를 만들수 있는 최소 소비 전력
    dp[0][0] = 0
    for i in range(1,n):
        start = 0
        if onboard[i] == 1:
            start = t1
        for j in range(start,t2+1):
            if j == temperature:
                dp[i][j] = dp[i-1][j]
            dp[i][j] = min(dp[i][j],dp[i-1][j-1]+a,dp[i-1][j]+b,dp[i-1][j+1])
    return min(dp[-1])