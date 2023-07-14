from itertools import combinations

def dfs(depth):
    global ans
    #총 15번의 경기가 있으므로 모든 경기가 끝난 경우
    if depth == 15:
        ans = 1
        for res in result_split:
            #경기 결과가 말이 안 되면
            if res.count(0) != 3:
                ans = 0
                break
        return
        
    winner,loser = games[depth]
    # 승 무 패
    for x,y in ([0,2],[1,1],[2,0]):
        if result_split[winner][x] > 0 and result_split[loser][y] > 0:
            result_split[winner][x] -=1
            result_split[loser][y] -= 1
            dfs(depth+1)
            result_split[winner][x] +=1
            result_split[loser][y] += 1
            
            
        
            

#경기 할 수 있는 경우의 수
games = list(combinations(range(6),2))

for _ in range(4):
    result = list(map(int,input().split()))
    #각 팀마다 승 무 패 순으로 저장
    result_split = [result[i:i+3] for i in range(0,18,3)]
    ans = 0
    dfs(0)
    print(ans,end=' ')
print()