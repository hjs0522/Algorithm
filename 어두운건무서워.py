import sys
input = sys.stdin.readline

def main():
    row, cul, num = map(int, input().split())
    board = []
    for i in range(row):
        board.append(list(map(int, input().split())))

    for i in range(num):
        y1, x1, y2, x2 = map(int, input().split())
        sum = 0
        for j in range(y1, y2+1):
            for k in range(x1, x2+1):
                sum += board[j-1][k-1]

        print(sum//((y2-y1+1)*(x2-x1+1)))


main()
