from collections import defaultdict

data = input()
data = data.upper()
dic = defaultdict(int)
for i in data:
    dic[i] += 1

ans = []
max_num = 0

for k,v in dic.items():
    if v > max_num:
        ans = [k]
        max_num = v
        continue
    
    if v == max_num:
        ans.append(k)
if len(ans)>=2:
    print('?')
else:
    print(ans[0])