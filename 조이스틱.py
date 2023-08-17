def solution(name):
    answer = 0
    #한 바퀴를 다 도는 경우
    min_move = len(name)-1
    for i,char in enumerate(name):
        answer += min(ord(char)-ord('A'),ord('Z')- ord(char) +1)
        next = i+1
        while next< len(name) and name[next] == 'A':
            next+=1
        #가장 긴 연속된 'A'를 제외한 모든 문자열을 다 순회해야 함 -> 그렇기에 가장 긴 연속된 'A'랑 만나는 두 끝 문자열의 위치에서 짧게 가는 법을 구하면 됨
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    answer += min_move
    return answer