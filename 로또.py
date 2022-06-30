"""
1부터 m까지의 숫자 중에 n개의 수를 고르는 로또
고를 때 각 숫자느 이전에 고른 수보다 적어도 2배가 되어야 함
"""

def main():
    dp = [[0]*2001 for i in range(11)]
    dp[0] = [1]*2001
    for i in range(1,11):
        for j in range(1,2001):
        #j 이하의 i개 수를 만드는 방법 = j-1 이하의 i 개를 만드는 방법 + j//2 이하의 i-1개를 만드는 방법
            dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
    t= int(input())
    for i in range(t):
        n,m = map(int,input().split()) 
        print(dp[n][m])
main()
    
    
        
    
    