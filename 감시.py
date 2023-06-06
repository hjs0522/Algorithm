import sys
input = sys.stdin.readline
from copy import deepcopy

n,m = map(int,input().split())

graph = []

#하,우,상,좌
dx = [0,1,0,-1]
dy = [1,0,-1,0]


#1번 한 방향 4가지
#2번 직선 2가지
#3번 수직 4가지
#4번 ㅏㅗㅓㅜ 4가지
#5번 전방향 1가지
cctv = []

#데이터 받아오기
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        if a[j] != 0 and a[j] != 6:
            #cctv번호와 위치, 방향을 저장
            #dfs과정에서 방향을 1씩 더하므로 -1부터해야 1더했을때 0부터 시작
            cctv.append([a[j],i,j,-1])
    graph.append(a[:])
    
#cctv번호에 따른 방향을 종류별로 추출    
def dfs(index,cctv):
    if index == len(cctv):
        graph_copy = deepcopy(graph)
        check_graph(cctv,graph_copy)
        return
    
    #4가지 방향을 모두 따지는 경우
    if cctv[index][0] == 1 or cctv[index][0] == 3 or cctv[index][0] == 4:
        for _ in range(4):
            cctv[index][3] += 1
            dfs(index+1,cctv)
        cctv[index][3] = -1
            
    #2가지 방향만 따지는 경우           
    elif cctv[index][0] == 2:
        for _ in range(2):
            cctv[index][3] += 1
            dfs(index+1,cctv)
        cctv[index][3] = -1   
            
    #방향 관계 없는 경우            
    elif cctv[index][0] == 5:
        cctv[index][3] += 1
        dfs(index+1,cctv)
        cctv[index][3] = -1              
            
 


#cctv의 번호,위치,방향 리스트를 입력받아 감시범위를 그리는 함수
def check_graph(cctv,graph_copy):
    for i in range(len(cctv)):
        cctv_num, x, y, dir = cctv[i]
        
        #1이면 지정된 방향으로만
        if cctv_num == 1:
            cctv_linedrow([x,y],dir,graph_copy)
            
        #2이면 지정된 방향과 반대방향으로
        elif cctv_num == 2:
            cctv_linedrow([x,y],dir,graph_copy)
            cctv_linedrow([x,y],(dir+2)%4,graph_copy)
            
        #3이면 지정된 방향과 수직방향으로
        elif cctv_num == 3:
            cctv_linedrow([x,y],dir,graph_copy)
            cctv_linedrow([x,y],(dir+1)%4,graph_copy)
            
        #4이면 지정된 방향에서 좌우로
        elif cctv_num == 4:
            cctv_linedrow([x,y],dir,graph_copy)
            cctv_linedrow([x,y],(dir+1)%4,graph_copy)
            cctv_linedrow([x,y],(dir-1)%4,graph_copy)
            
        #5이면 모든방향
        elif cctv_num == 5:
            for j in range(4):
                cctv_linedrow([x,y],j,graph_copy)

        
    find_non_cctv_area(graph_copy)


#cctv의 종류와 상관없이 위치와 방향만으로 직선의 감시영역을 표시하는 함수    
def cctv_linedrow(postion,dir,graph):
    nx = postion[0] + dx[dir]
    ny = postion[1] + dy[dir]
    while True:
        #영역 이내일때
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                #감시영역은 7로 표기
                graph[nx][ny] = 7
            #벽만나면 진행 멈춤
            elif graph[nx][ny] == 6:
                break
        #영역 벗어나도 멈춤
        else:
            break
                
        nx += dx[dir]
        ny += dy[dir]
        
    
#저장된 데이터에 맞게 적용, 결과 도출
#결과의 최대값은 64(n,m의 최대값이 8)
result = 64
    
    
#사각지대의 개수를 찾는 함수    
def find_non_cctv_area(graph):
    global result
    result_ = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result_ += 1
                
    result = min(result, result_)
    
    
dfs(0,cctv)
print(result)