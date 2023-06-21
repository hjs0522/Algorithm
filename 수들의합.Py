def check(s,number):
    if (number+1)*(number)//2 > s:
        return False
    else:
        return True
        
s = int(input())
l = 1
r = s
ans = 0
while l<=r:
    mid = (l+r)//2
    if check(s,mid):
        ans = max(ans,mid)
        l = mid+1
    else:
        r = mid-1
print(ans)