from collections import deque,defaultdict
def solution(msg):
    answer = []
    msg = deque(msg)
    dic = defaultdict(int)
    for i in range(26):
        dic[chr(i+65)] = i+1
    q = deque()
    next_num = 27
    while msg:
        q.append(msg.popleft())
        word = ''.join(q)
        if dic[word] == 0:
            dic[word] = next_num
            next_num+=1
            answer.append(dic[word[:-1]])
            for i in range(len(word)-1):
                q.popleft()
            
    if q:
        word = ''.join(q)
        answer.append(dic[word])
    return answer