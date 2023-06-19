n,s = map(int,input().split())
num = list(map(int,input().split()))

head = 1
tail = 0
ans = int(1e9)

subSum = [0 for _ in range(n+1)]
for i in range(1,len(num)+1):
    subSum[i] = subSum[i-1]+num[i-1]
while True:
    if head == n+1:
        break
    
    if subSum[head] - subSum[tail] < s:
        head += 1
        continue
    
    if subSum[head] - subSum[tail] >= s:
        ans = min(ans,head-tail)
        tail+=1
if ans == int(1e9):
    ans = 0
print(ans)