import sys
input = sys.stdin.readline


def check(x, level, k):
    for i in range(len(x)):
        if k < 0:
            return False
        
        if x[i] < level:
            k -= level - x[i]
            if k<0:
                return False
        else:
            return True


def main():
    n, k = map(int, input().split())
    x = []
    for i in range(n):
        x.append(int(input()))
    x.sort()
    left = x[0]
    right = x[0]+k
    ans = 0
    while(left <= right):
        mid = (left+right)//2
        # check함수를 통과 한 경우 mid레벨 까지는 가능 하다는 것이다.
        if check(x, mid, k):
            ans = mid
            left = mid+1
        else:
            right = mid-1

    print(ans)


main()
