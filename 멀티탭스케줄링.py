n,k = map(int,input().split())
elect = list(map(int,input().split()))
curUse = []
ans = 0

for idx,e in enumerate(elect):
    if e in curUse:
        continue
    
    if idx  == len(elect) -1:
        if e in curUse:
            break
        if e not in curUse:
           ans+=1
           break

    if len(curUse) < n:
        curUse.append(e)
        continue
    
    if len(curUse) >= n:
        max_idx = idx
        flag = False
        ans+=1
        for cur_idx,cur in enumerate(curUse):
            if cur not in elect[idx+1:]:
                curUse[cur_idx] = e
                flag = True
                break
            max_idx = max(elect[idx+1:].index(cur)+idx+1,max_idx)
        if flag:
            continue
        curUse[curUse.index(elect[max_idx])] = e
print(ans)