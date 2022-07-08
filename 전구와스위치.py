"""
i 번 스위치를 누르면 i-1,i,i+1 세개의 전구의 상태가 바뀐다.
n개의 전구들의 현재 상태와 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내보자

"""

def two_flip(diff,i,j):
    diff[i] = abs(1-diff[i])
    diff[j] = abs(1-diff[j])

def three_flip(diff,i,j,k):
    diff[i] = abs(1-diff[i])
    diff[j] = abs(1-diff[j])
    diff[k] = abs(1-diff[k])

def main():
    n = int(input())
    now = list(map(int,input()))
    goal = list(map(int,input()))
    diff = [abs(now[i]-goal[i]) for i in range(n)]
    
    ans = 100001
    cnt = 0
    diffCopy = diff[:]
    
    for i in range(n):
        if i == 0 and sum(diff) != 0:
            cnt+=1
            two_flip(diffCopy,i,i+1)
        elif 1<=i<=n-2 and diffCopy[i-1]:
            cnt+=1
            three_flip(diffCopy,i-1,i,i+1)
        elif i == n-1 and diffCopy[i-1]:
            cnt+=1
            two_flip(diffCopy,i-1,i)
    
    if sum(diffCopy) == 0:
        ans = min(ans,cnt)
        
    diffCopy = diff[:]
    cnt = 0
    for i in range(1,n):
        if 1<=i<=n-2 and diffCopy[i-1]:
            cnt+=1
            three_flip(diffCopy,i-1,i,i+1)
        elif i == n-1 and diffCopy[i-1]:
            cnt+=1
            two_flip(diffCopy,i-1,i)
     
    if sum(diffCopy) == 0:
        ans = min(ans,cnt)
        
    return ans if ans!= 100001 else -1
            
print(main())

    
