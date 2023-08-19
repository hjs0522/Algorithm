def convert(num,base):
    temp = '0123456789ABCDEF'
    q,r = divmod(num,base)
    if q == 0:
        return temp[r]
    else:
        return convert(q,base)+temp[r]
def solution(n, t, m, p):
    answer = ''
    cnt = 0
    res = ''
    while True:
        res += convert(cnt,n)
        cnt+=1
        if len(res) >= (t-1)*m+p:
            break
    for i in range(p-1,len(res),m):
        if len(answer) == t:
            break
        answer+=res[i]
    return answer