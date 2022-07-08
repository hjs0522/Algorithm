"""
벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 초밥 하나를 추가로 무료 제공
만약 이 번호에 적힌 초밥이 벨트에 없는 경우 새로 만들어 제공

벨트 상태, 초밥의 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호가 주어졌을때 손님이 먹을 수 있는 초밥 가짓수의 최댓값
"""


from collections import defaultdict

def main():
    n,d,k,c = map(int,input().split())
    chobab = [int(input()) for _ in range(n)]
    #현재 먹은 초밥에 대한 정보를 저장하는 딕셔너리
    eat = defaultdict(int)
    #연속해서 k개를 무조건 먹을 것이므로 c는 먹는다고 가정
    eat[c] = 1
    cnt = 1
    
    #우선 앞에서부터 k개를 연속해서 먹는경우
    for i in range(k):
        #딕셔너리에 없는 경우 아직 먹지 않은 것이기에 cnt +=1
        if eat[chobab[i]] == 0:
            cnt +=1
        eat[chobab[i]] += 1
        
    ans = cnt
    #k번째 초밥 부터 연속해서 k개의 초밥을 먹는 경우를 고려
    for i in range(k,n+k -1):
        #맨 앞쪽에 있는 것을 뺀다
        eat[chobab[i-k]]-=1
        if eat[chobab[i-k]] == 0:
            cnt-=1
        #뒤에 초밥을 먹은 경우
        eat[chobab[i%n]] +=1
        if eat[chobab[i%n]] == 1:
            cnt+=1
        ans = max(cnt,ans)
    print(ans)
main()