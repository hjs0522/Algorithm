from collections import defaultdict
def solution(n, words):
    answer = []
    dic = defaultdict(int)
    end = ''
    for idx,word in enumerate(words):
        if word.startswith(end) or end=='':
            end = word[-1]
        else:
            return [idx%n+1,idx//n+1]
        if dic[word] != 0:
            return [idx%n+1,idx//n+1]
        dic[word] = 1

    return [0,0]