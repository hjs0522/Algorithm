from copy import deepcopy
from itertools import product

def turn(board,r,c,n):
    for dr,dc in [(-1,0),(0,1),(1,0),(0,-1),(0,0)]:
        if 0 <= r+dr < len(board) and 0<= c+dc < len(board[0]):
            board[r+dr][c+dc] = (board[r+dr][c+dc]+n)%4
def finished(board):
    for x in board[-1]:
        if x!=0:
            return False
    return True

def solution(clockHands):
    board = clockHands
    length = len(board)

    answer = float('inf')
    for ns in product([0,1,2,3],repeat=length):
        cnt = 0
        newboard = deepcopy(board)

        for c,n in zip(range(length),ns):
            turn(newboard,0,c,n)
            cnt+=n

        for r in range(1,length):
            for c in range(length):
                if (x:= newboard[r-1][c]) !=0:
                    turn(newboard,r,c,(4-x)%4)
                    cnt+= (4-x)%4
        if finished(newboard):
            answer = min(answer,cnt)
    return answer

print(solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]))