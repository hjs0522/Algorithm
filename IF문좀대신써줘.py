"""
전투력 10000 이하는 weak
10000 초과 ~100000이하는 normal
100000초과 1000000 이하는 strong

캐릭터의 전투력에 맞는 칭호를 출력하는 프로그램을 작성

첫번째 줄에는 칭호의 개수 n, 칭호를 출력해야 하는 캐릭터들의 개수 m
두번째 줄부터는 n개의 줄에 각 칭호의 이름을 나타내는 길이 1이상, 11이하 영어 대문자로 구성된 문자열과 해당 칭호의 전투력 상한값 주어짐
n+2번째 줄부터는 m개의 각 줄에는 캐릭터의 전투력을 나타내는 음이 아닌 정수가 주어진다.

m개의 줄에 걸쳐 캐릭터의 전투력에 맞는 칭호를 입력 순서대로 출력한다.
어떤 캐릭터의 전투력으로 출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력
"""

import sys
input = sys.stdin.readline

def main():
    
    n,m = map(int,input().split())
    queue = []
    for i in range(n):
        title,power = input().split()
        power = int(power)
        queue.append([title,power])
    
    for i in range(m):
        inputPower = int(input())
        left,right = 0,n-1
        mid = (left+right)//2
        while(left<=right):
            if inputPower> queue[mid][1]:
                left = mid +1
            else:
                right= mid - 1
            mid = (left+right)//2
        mid = left
        print(queue[mid][0])
        
main()
        