n = int(input())
a = list(map(int,input().split()))
oper = list(map(int,input().split()))
max_value = -int(1e9)
min_value = int(1e9)
def dfs(value,idx):
    global max_value
    global min_value
    if idx == len(a):
        max_value = max(max_value,value)
        min_value = min(min_value,value)
        return
    if oper[0] > 0:
        oper[0] -=1
        dfs(value+a[idx],idx+1)
        oper[0] += 1
    
    if oper[1] > 0:
        oper[1] -=1
        dfs(value-a[idx],idx+1)
        oper[1] +=1
        
    if oper[2] > 0:
        oper[2] -=1
        dfs(value*a[idx],idx+1)
        oper[2] +=1
    
    if oper[3] > 0:
        oper[3] -=1
        if value < 0:
            dfs(-(-value//a[idx]),idx+1)
        else:
            dfs(value//a[idx],idx+1)
        oper[3] +=1
dfs(a[0],1)
print(max_value)
print(min_value)
    
    