def main():
    h,w = map(int,input().split())
    board = list(map(int,input().split()))
    maxValue = max(board)
    maxIdx = board.index(maxValue)
    
    ans = 0
    height = 0
    for i in range(maxIdx+1):
        height = max(height,board[i])
        ans+= height - board[i]
    
    height = 0
    for i in range(w-1,maxIdx,-1):
        height = max(height,board[i])
        ans+= height - board[i]
        
    return ans

print(main())