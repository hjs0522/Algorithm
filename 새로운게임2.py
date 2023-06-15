import sys
input = sys.stdin.readline

n,k = map(int,input().split())

graph = []

#0은 흰색, 1은 빨간색, 2는 파란색
for _ in range(n):
    graph.append(list(map(int, input().split())))

token_postion = []
#그래프 위치에 쌓여있는 상태를 나타내는 행렬
token_graph = [[[]for _ in range(n)] for _ in range(n)]

for i in range(k):
    #말의 행번호, 열번호, 이동방향
    x,y,dir = map(int, input().split())
    token_graph[x-1][y-1].append(i)
    token_postion.append([x-1,y-1,dir])

#1,2,3,4이므로 0번은 빈칸으로 0
#방향을 반대로 하기위해 -1,-2,-3,-4,순으로 반대방향이 되도록 작성
dx = [0,0,0,-1,1,-1,1,0,0]
dy = [0,1,-1,0,0,0,0,1,-1]


count = 0
game_clear = False

while True:
    #1000번을 넘길경우 -1 출력한뒤 멈춤
    if count > 1000:
        print(-1)
        break
    #게임이 클리어 됐으면 턴수만큼 출력하고 멈춤
    if game_clear:
        print(count)
        break
    
    count += 1
    
    #모든 토큰에 대해서/ 현재 움직이는 토큰은 i
    for i in range(k):
        x,y,dir = token_postion[i]
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        #범위 밖이거나 파란색이면 방향 반대로 해서 한칸 전진
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
            dir *= -1
            token_postion[i][2] *= -1
            
            #방향 바꿔서 이동좌표 갱신
            nx = x + dx[dir]
            ny = y + dy[dir]
            
            #반대방향 한칸 전진시 범위 밖 or 그 칸이 파란색이면 안함
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
                #마지막 이동한 위치의 말의 개수를 파악하기 위해 nx,ny가 사용되므로 
                #안움직이더라도 nx,ny가 현재위치라고 갱신해줌
                nx,ny = x,y
            #흰색인 경우
            elif graph[nx][ny] == 0:
                #해당칸에 있는 토큰들에 대해서
                for j in range(len(token_graph[x][y])):
                    #움직이려는 토큰 번호에서부터
                    if token_graph[x][y][j] == i:
                        #끝까지
                        for _ in range(len(token_graph[x][y])-j):
                            #토큰 그래프에서 옮기고, 토큰포지션 최신화
                            move_token = token_graph[x][y].pop(j)
                            token_graph[nx][ny].append(move_token)
                            token_postion[move_token][0] = nx
                            token_postion[move_token][1] = ny
                        break
 
            #빨간색인 경우
            elif graph[nx][ny] == 1:
                #해당칸에 있는 토큰들에 대해서
                for j in range(len(token_graph[x][y])):
                    #움직이려는 토큰 번호에서부터
                    if token_graph[x][y][j] == i:
                        #끝까지 횟수만큼
                        for _ in range(len(token_graph[x][y])-j):
                            #토큰 그래프의 뒤에서부터 옮기고, 토큰포지션 최신화
                            move_token = token_graph[x][y].pop(-1)
                            token_graph[nx][ny].append(move_token)
                            token_postion[move_token][0] = nx
                            token_postion[move_token][1] = ny
                        break
                
        
        #흰색인 경우
        elif graph[nx][ny] == 0:
            #해당칸에 있는 토큰들에 대해서
            for j in range(len(token_graph[x][y])):
                #움직이려는 토큰 번호에서부터
                if token_graph[x][y][j] == i:
                    #끝까지
                    for _ in range(len(token_graph[x][y])-j):
                        #토큰 그래프에서 옮기고, 토큰포지션 최신화
                        move_token = token_graph[x][y].pop(j)
                        token_graph[nx][ny].append(move_token)
                        token_postion[move_token][0] = nx
                        token_postion[move_token][1] = ny
                    break
 
        #빨간색인 경우
        elif graph[nx][ny] == 1:
            #해당칸에 있는 토큰들에 대해서
            for j in range(len(token_graph[x][y])):
                #움직이려는 토큰 번호에서부터
                if token_graph[x][y][j] == i:
                    #끝까지 횟수만큼
                    for _ in range(len(token_graph[x][y])-j):
                        #토큰 그래프의 뒤에서부터 옮기고, 토큰포지션 최신화
                        move_token = token_graph[x][y].pop(-1)
                        token_graph[nx][ny].append(move_token)
                        token_postion[move_token][0] = nx
                        token_postion[move_token][1] = ny
                    break
                    
        #현재 움직인 칸에 말이 4개 이상 쌓였으면 게임 클리어
        if len(token_graph[nx][ny]) >= 4:
            game_clear = True
            break