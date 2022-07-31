def main():
    w= int(input())
    h = int(input())
    final = list(input())
    start = sorted(final)
    
    ladder = []
    
    idx = 0
    for i in range(h):
        ladder.append(input())
        if ladder[i][0] =='?':
            idx = i
    
    for i in range(idx):
        for j in range(w-1):
            if ladder[i][j] == '-':
                start[j],start[j+1]= start[j+1],start[j]
    
    for i in range(h-1,idx,-1):
        for j in range(w-1):
            if ladder[i][j] == '-':
                final[j],final[j+1] = final[j+1],final[j]
    ans = []
    for i in range(w-1):
        if start[i] == final[i]:
            ans.append('*')
        elif start[i+1] == final[i] and start[i] == final[i+1]:
            ans.append('-')
            start[i],start[i+1] = start[i+1],start[i]
        else:
            print("x"*(w-1))
            return
    print("".join(ans))
    
main()