from collections import defaultdict
def solution(dirs):
    answer = 0
    dic = defaultdict(int)
    x,y = 0,0
    for d in dirs:
        nx,ny = x,y
        if d =='U':
            if ny<5:
                ny+=1
                if dic[(x,y,nx,ny)] ==0:
                    dic[(x,y,nx,ny)] +=1
                    answer+=1
        elif d == 'D':
            if ny>-5:
                ny-=1
                if dic[(nx,ny,x,y)] == 0:
                    dic[(nx,ny,x,y)] += 1
                    answer+=1
        elif d == 'R':
            if nx<5:
                nx+=1
                if dic[(x,y,nx,ny)] ==0:
                    dic[(x,y,nx,ny)] +=1
                    answer+=1
        elif d=='L':
            if nx>-5:
                nx-=1
                if dic[(nx,ny,x,y)] == 0:
                    dic[(nx,ny,x,y)] += 1
                    answer+=1
        x,y = nx,ny
    return answer