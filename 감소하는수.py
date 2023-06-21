from itertools import combinations

nums = []
for i in range(1,11):
    combi = list(combinations(range(10),i))
    for com in combi:
        com = list(com)
        com.sort(reverse = True)
        nums.append(int("".join(map(str,com))))
nums.sort()
n = int(input())
try:
    print(nums[n])
except:
    print(-1)