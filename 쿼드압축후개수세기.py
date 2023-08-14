def solution(arr):
    answer = [0,0]
    n = len(arr)
    
    def quard(x,y,n):
        num = arr[x][y]
        
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j] != num:
                    n//=2
                    quard(x,y,n)
                    quard(x,y+n,n)
                    quard(x+n,y,n)
                    quard(x+n,y+n,n)
                    return
                
        answer[num] += 1
    quard(0,0,n)
    return answer

