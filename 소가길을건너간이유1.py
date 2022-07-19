"""
소의 위치를 n번 관찰 하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다.
소를 10마리 가지고 있으므로 소의 번호는 1이상 10이하의 정수
소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1중 하나
이 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자
"""

from collections import defaultdict


def main():
    n = int(input())
    dict = defaultdict(lambda: -1)
    ans = 0
    for i in range(n):
        num,loc = map(int,input().split())
        if dict[num] == -1:
            dict[num] = loc
        elif dict[num] != loc:
            ans+=1
            dict[num] =loc
    print(ans)

main()