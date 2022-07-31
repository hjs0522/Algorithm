def main():
    x,y = map(int,input().split())
    z = (y*100)//x
    #99프로는 변화 할 수 없기에 
    if z >= 99:
        print(-1)
        return
    
    ans =0
    left = 1
    right = x
    
    while(left <= right):
        mid = (left+right)//2
        #앞으로 계속 이기기만 하기 때문에 z보다 승률이 작거나 같으면 답이 될 수 없다.
        if(y+mid)*100 //(x+mid) <= z:
            left= mid+1
        else:
        #승률을 변화 시키는 가장 작은 값을 ans에 저장
            ans = mid
            right = mid-1
    print(ans)
    
main()