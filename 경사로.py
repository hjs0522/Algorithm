n,l = map(int,input().split())
board = []

for _ in range(n):
    board.append(list(map(int,input().split())))
ans = 0
for i in range(n):
    value = board[i][0]
    check = [False]*n
    res = True
    for j in range(1,n):
        if board[i][j] != value and board[i][j] != value-1 and board[i][j] != value+1:
            res = False
            break
        
        if board[i][j] == value+1:
            if j<l:
                res = False
                break
            flag = True
            for k in range(1,l+1):
                if check[j-k]:
                    flag = False
                    break
                if board[i][j-k] != value:
                    flag = False
                    break
            if flag == False:
                res = False
                break
            
            for k in range(1,l+1):
                check[j-k] = True
            value = value + 1
            continue
        
        if board[i][j] == value - 1:
            if n-j < l:
                res = False
                break
            flag = True
            for k in range(l):
                if check[j+k]:
                    flag = False
                    break
                
                if board[i][j+k] != value - 1:
                    flag = False
                    break
            if flag == False:
                res = False
                break
            for k in range(l):
                check[j+k] = True
            value = value-1
            continue
    if res:
        ans+=1
        
for i in range(n):
    value = board[0][i]
    check = [False]*n
    res = True
    for j in range(1,n):
        if board[j][i] != value and board[j][i] != value-1 and board[j][i] != value+1:
            res = False
            break
        
        if board[j][i] == value+1:
            if j<l:
                res = False
                break
            flag = True
            for k in range(1,l+1):
                if check[j-k]:
                    flag = False
                    break
                if board[j-k][i] != value:
                    flag = False
                    break
            if flag == False:
                res = False
                break
            
            for k in range(1,l+1):
                check[j-k] = True
            value = value + 1
            continue
        
        if board[j][i] == value - 1:
            if n-j < l:
                res = False
                break
            flag = True
            for k in range(l):
                if check[j+k]:
                    flag = False
                    break
                
                if board[j+k][i] != value -1 :
                    flag = False
                    break
            if flag == False:
                res = False
                break
            for k in range(l):
                check[j+k] = True
            value = value-1
            continue
    if res:
        ans+=1
print(ans)