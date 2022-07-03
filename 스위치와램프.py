"""
상도는 n개의 스위치와 m개의 램프
가장 처음에 램프는 모두 꺼져있다.
스위치를 누르면 램프의 전원이 켜짐, 끌수는 없음
n-1개의 스위치를 눌러서 모든 램프를 켤 수 있는지 알아보자
"""

def powerOff(switch,lamp,idx):
    flag = True
    for i in range(len(switch[idx])):
        lampIdx = switch[idx][i]
        lamp[lampIdx] -=1
        
        if lamp[lampIdx] <= 0:
            flag = False
    for i in range(len(switch[idx])):
        lampIdx = switch[idx][i]
        lamp[lampIdx] +=1
    return flag
    
def check(n,switch,lamp):
    for i in range(n):
        if powerOff(switch,lamp,i):
            return 1
    
    return 0
    
def main():
    n,m = map(int,input().split())
    switch = [[] for i in range(n)]
    lamp = [0 for i in range(m+1)]
    for i in range(n):
        #첫번째 정수는 스위치와 연결된 램프의 수, 이후 연결된 램프의 번호가 공백으로 구분 
        lampInfo = list(map(int,input().split()))
        for j in range(lampInfo[0]):
            switch[i].append(lampInfo[j+1])
            lamp[lampInfo[j+1]] +=1
    return check(n,switch,lamp)
print(main())
    