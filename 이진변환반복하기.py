def solution(s):
    answer = []
    cnt_remove_0 = 0
    cnt = 0
    while True:
        len_s = len(s)
        s = s.replace('0','')
        cnt_remove_0 += len_s - len(s)
        s = bin(len(s))[2:]
        cnt+=1
        if s == '1':
            break
    return [cnt,cnt_remove_0]