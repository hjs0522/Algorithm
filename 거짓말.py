import sys
input = sys.stdin.readline
n,m = map(int,input().split())
know = set(input().split()[1:])
party = []
for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p & know:
            know = know.union(p)
cnt = 0
for p in party:
    if p&know:
        continue
    else:
        cnt+=1
print(cnt)