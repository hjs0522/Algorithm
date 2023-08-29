def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    stack = [(x,y,'')]
    while stack:
        x,y,path = stack.pop()
        if len(path) == k and (x,y) == (r,c):
            answer = path
            break
        remain,shortest_path = k-len(path),abs(x-r)+abs(y-c)
        if remain < shortest_path or remain%2 != shortest_path%2:
            continue
        if x>1:
            stack.append((x-1,y,path+'u'))
        if y<m:
            stack.append((x,y+1,path+'r'))
        if y>1:
            stack.append((x,y-1,path+'l'))
        if x<n:
            stack.append((x+1,y,path+'d'))
    return answer