import functools
def add(x,y):
    return x+y

def outer(x):
    def inner(y):
        return x+y
    return inner

a = functools.partial(add,2)
print(a(3))
print(outer(2))

def fill1(temperatures):
    total,count = 0,0
    for t in temperatures:
        if t is not None:
            total+=t
            count +=1
    avg = total/count
    for t in temperatures:
        if t is None:
            t= avg

def fill2(temperatures):
    print(sum(temperatures))
    print(len(temperatures))
    avg = sum(temperatures)/len(temperatures)
    for i in range(len(temperatures)):
        if temperatures[i] is None:
            temperatures[i] = avg

def fill3(temperatures):
    good = [t for t in temperatures if t]
    avg = sum(good)/len(good)
    for i,t in enumerate(temperatures):
        temperatures[i] = t or avg

def fill4(temperatures):
    good = [t for t in temperatures if t is not None]
    avg = sum(good)/len(good)
    temperatures = [t or avg for t in temperatures]
    
def fill5(temperatures):
    good = [t for t in temperatures if t is not None]
    avg = sum(good)/len(good)
    temperatures[:] = [t if t is not None else avg for t in temperatures]
temperatures = [2,3,4,None,5,None,None,0]
fill3(temperatures)
print(temperatures)