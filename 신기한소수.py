N = int(input())

def isPrime(num):
    if num < 2:
        return False
        
    for i in range(2,int(num**(0.5))+1):
        if num%i ==0:
            return False
    
    return True

def dfs(num):
    if len(str(num)) == N:
        print(num)
        return
        
    for i in range(1,10):
        temp = num*10+i
        if isPrime(temp):
            dfs(temp)
    
dfs(2)
dfs(3)
dfs(5)
dfs(7)
    

            