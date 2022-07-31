from collections import defaultdict


def main():
    while True:
        n,m = map(int,input().split())
        if n==0 and m == 0:
            return
        
        order = defaultdict(int)
        for i in range(n):
            orderList = list(map(int,input().split()))
            for j in range(m):
                order[orderList[j]] +=1
        order[max(order,key = order.get)] = 0
        maxValue = order[max(order,key = order.get)]
        ans = []
        for key in order:
            if order[key] == maxValue:
                ans.append(key)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()
main()