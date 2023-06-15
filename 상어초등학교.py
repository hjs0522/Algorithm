"""
교실은 n*n크기
학교에 다니는 학생의 수는 n**2명
선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다.
한칸에는 학생 한 명의 자리만 있을 수 있고,
|r1-r2| + |c1 - c2| =1을 만족하면 두 칸이 (r1,c1)과 (r2,c2)를 인접한다고 한다.

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함
2. 1.을 만족하는 칸이 여러 개이면, 인접한 칸중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은칸으로, 열의 번호가 가장 작은칸으로 자리를 정함
"""

from collections import defaultdict, deque

def main():
    n = int(input())
    order = deque()
    favorDict = defaultdict(list)
    
    for i in range(n**2):
        inputList = list(map(int,input().split()))
        order.append(inputList[0])
        for j in range(4):
            favorDict[inputList[0]].append(inputList[j+1])
    
    seat = [[-1] * n for _ in range(n)]
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for i in range(len(order)):
        GfavorCnt = 0
        GemptyCnt = 0
        
        #가장 위에 있는 빈칸위치 저장
        flag = False
        for y in range(n):
            for x in range(n):
                if seat[y][x] == -1:
                    loc = [y,x]
                    flag = True
                    break
            if flag:
                break
        
        for y in range(n):
            for x in range(n):
                #빈칸을 찾음
                if seat[y][x] != -1:
                 continue
                favorCnt = 0
                emptyCnt = 0
                #찾은 빈칸의 주변에 선호하는 사람이 있는지, 빈칸은 몇개인지 계산
                for k in range(4):
                    newY = y+dy[k]
                    newX = x +dx[k]
                    if newY>=0 and newY< n and newX>=0 and newX <n:
                        if seat[newY][newX] in favorDict[order[i]]:
                            favorCnt+=1
                        elif seat[newY][newX] == -1:
                            emptyCnt += 1
                #선호하는 사람이 더 많다면 자리저장
                if GfavorCnt < favorCnt:
                    GfavorCnt = favorCnt
                    GemptyCnt = emptyCnt
                    loc = [y,x]
                #선호하는 사람의 수가 같은 경우 빈칸이 더 많은 곳 저장
                elif GfavorCnt == favorCnt:
                    if GemptyCnt < emptyCnt:
                        GemptyCnt = emptyCnt
                        loc = [y,x]
        seat[loc[0]][loc[1]] = order[i]
    
    ans = 0
    for y in range(n):
        for x in range(n):
            cnt = 0
            for k in range(4):
                newY = y+dy[k]
                newX = x +dx[k]
                if newY>=0 and newY< n and newX>=0 and newX <n:
                    if seat[newY][newX] in favorDict[seat[y][x]]:
                        cnt+=1
            if cnt ==1:
                ans+=1
            elif cnt == 2:
                ans+=10
            elif cnt == 3:
                ans+=100
            elif cnt == 4:
                ans+=1000
    print(ans)

main()