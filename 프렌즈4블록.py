def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
def solution(m, n, board):
    answer = 0
    board = rotate(board)
    result = []
    while True:
        for i in range(len(board)-1):
            for j in range(len(board[0])-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] !=0:
                    result.extend([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])
        result = list(set(result))
        answer += len(result)
        if len(result) == 0:
            break
        for (i,j) in result:
            board[i][j] =0
        result = []
        for i in range(len(board)):
            cnt = 0
            stack = []
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    cnt+=1
                    continue
                if board[i][j] !=0:
                    stack.append(board[i][j])
                    continue
            stack.extend([0 for k in range(cnt)])
            board[i] = stack
    return answer
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))