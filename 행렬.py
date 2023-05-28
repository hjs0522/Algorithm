def reverse(y, x, a):
    for i in range(y, y+3):
        for j in range(x, x+3):
            a[i][j] = abs(1-a[i][j])


def check(n, m, a, b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False

    return True


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input())) for i in range(n)]
    b = [list(map(int, input())) for i in range(n)]
    cnt = 0

    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                reverse(i, j, a)
                cnt += 1

    if check(n, m, a, b):
        print(cnt)
    else:
        print("-1")


main()


"""
하나의 큐에서 추출하고, 추출된 원소를 다른큐에 집어 넣는 작업을 통해 각 큐의 합이 같도록 만든다.
이때 필요한 작업의 최소 횟수를 구하고자 합니다.
한 번의 pop과 한 번의 insert가 합쳐서 작업을 1회 수행한 것으로 간주

"""

def solution(queue1, queue2):
    answer = 0
    if (sum(queue1)+sum(queue2)) % 2 ==1:
        print(-1)
    while True:
        if sum(queue1) == sum(queue2):
            print(answer)
        elif sum(queue1[1:])<sum(queue2[1:]):
            value = queue2.pop()
            queue1.append(value)
        else:
            value = queue1.pop()
            queue2.append(value)