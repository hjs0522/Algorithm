from collections import deque
N,M,T = map(int,input().split())
circle = []
for i in range(N):
    circle.append(deque(list(map(int,input().split()))))

for _ in range(T):
    xi,di,ki = map(int,input().split())
    
    if di ==0:
        for i in range(1,N//xi+1):
            circle[i*xi-1].rotate(ki)
    elif di == 1:
        for i in range(1,N//xi+1):
            circle[i*xi-1].rotate(-ki)

    from copy import deepcopy
    temp = deepcopy(circle)
    flag = False
    for i in range(N):
        for j in range(M-1):
            if circle[i][j] == circle[i][j+1] and circle[i][j]!=0:
                temp[i][j] =0
                temp[i][j+1] = 0
                flag = True
        if circle[i][M-1] == circle[i][0] and circle[i][0] != 0:
            temp[i][M-1] = 0
            temp[i][0] = 0
            flag = True
    for i in range(M):
        for j in range(N-1):
            if circle[j][i] == circle[j+1][i] and circle[j][i] != 0:
                temp[j][i] = 0
                temp[j+1][i] = 0
                flag = True
    circle = temp
    circle_sum = 0
    cnt = 0
    if flag == True:
        continue
        
    for i in range(N):
        for j in range(M):
            if circle[i][j] != 0:
                cnt+=1
                circle_sum+=circle[i][j]
    if cnt == 0:
        continue
    avg = circle_sum/cnt
    for i in range(N):
        for j in range(M):
            if circle[i][j] ==0:
                continue
            if circle[i][j] > avg:
                circle[i][j]-=1
                continue
            if circle[i][j] < avg:
                circle[i][j]+=1
                continue
ans = 0
for i in range(N):
    for j in range(M):
        ans+=circle[i][j]
print(ans)