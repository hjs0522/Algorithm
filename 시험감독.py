n = int(input())
test = list(map(int,input().split()))
b,c = map(int,input().split())
ans = 0
for t in test:
    t-=b
    ans+=1
    if t > 0:
        if t%c > 0:
            ans+=t//c +1
            continue
        ans += t//c
        
print(ans)