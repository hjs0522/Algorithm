n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
    
type = [[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)],[(0,0),(0,1),(1,0),(1,1)],
[(0,0),(1,0),(2,0),(2,1)],[(0,0),(1,0),(0,1),(0,2)],[(0,0),(0,1),(1,1),(2,1)],[(1,0),(1,1),(1,2),(0,2)],
[(0,1),(1,1),(2,1),(2,0)],[(0,0),(1,0),(1,1),(1,2)],[(0,0),(1,0),(2,0),(0,1)],[(0,0),(0,1),(0,2),(1,2)],
[(0,0),(1,0),(1,1),(2,1)],[(0,1),(0,2),(1,0),(1,1)],[(0,0),(0,1),(1,1),(1,2)],[(0,1),(1,0),(1,1),(2,0)],
[(0,0),(0,1),(0,2),(1,1)],[(0,0),(1,0),(1,1),(2,0)],[(0,1),(1,0),(1,1),(2,1)],[(0,1),(1,0),(1,1),(1,2)]]
def check(type):
    one,two,three,four = type
    max_result = 0
    for i in range(n):
        for j in range(m):
            if i+one[0] >= n or i+two[0] >= n or i+three[0] >= n or i+four[0]>=n:
                continue
            if j+one[1] >=m or j+two[1] >=m or j+three[1] >=m or j+four[1] >=m:
                continue
            
            max_result = max(max_result,board[i+one[0]][j+one[1]] + board[i+two[0]][j+two[1]] + board[i+three[0]][j+three[1]] + board[i+four[0]][j+four[1]])
    return max_result

ans = 0
for t in type:
    ans = max(check(t),ans)
print(ans)