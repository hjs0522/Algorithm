def solution(target):
    answer = []
    dp = [[int(1e9),0] for _ in range(target+61)]
    dp[0] = [0,0]
    for i in range(0,target):
        if dp[i+50][0] > dp[i][0]+1 or (dp[i+50][0] == dp[i][0]+1 and dp[i+50][1] < dp[i][1]+1):
            dp[i+50] = [dp[i][0]+1,dp[i][1]+1]
        
        for j in range(1,21):
            if dp[i+j][0] > dp[i][0]+1 or (dp[i+j][0] == dp[i][0]+1 and dp[i+j][1] < dp[i][1]+1):
                dp[i+j] = [dp[i][0]+1,dp[i][1]+1]
            if dp[i+j*2][0] > dp[i][0]+1 or (dp[i+j*2][0] == dp[i][0]+1 and dp[i+j*2][1] < dp[i][1]+1):
                dp[i+j*2] = [dp[i][0]+1,dp[i][1]]
            if dp[i+j*3][0] > dp[i][0]+1 or (dp[i+j*3][0] == dp[i][0]+1 and dp[i+j*3][1] < dp[i][1]+1):
                dp[i+j*3] = [dp[i][0]+1,dp[i][1]]
    return dp[target]